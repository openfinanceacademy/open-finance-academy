#!/usr/bin/env python3
"""Recompute inline arithmetic in lesson Markdown using only stdlib.

Finds statements shaped like "$100 × 1.05 = $105", "(1.05 ÷ 1.03) − 1 =
about 1.94%", or chained "fee = $1.74 + $0.30 = $2.04" in source Markdown,
evaluates every segment, and checks that consecutive segments agree within
the rounding implied by their decimal places. Fails on any mismatch so
worked examples cannot drift silently. Prose and table-only arithmetic
without an equals sign is not covered; review those by hand.
"""

import argparse
import ast
import operator
import re
from pathlib import Path

NUMBER = r'[−-]?[$€£¥₹]?\d[\d,]*(?:\.\d+)?…?%?'
OPERATOR = r'(?:[×÷−]|\s[*/+-]\s)'
TERM = rf'\(*{NUMBER}\)*'
SEGMENT = rf'{TERM}(?:\s*{OPERATOR}\s*{TERM})*'
APPROX = r'(?:about|roughly|approximately|≈)\s*'
STATEMENT = re.compile(rf'({SEGMENT})((?:\s*=\s*(?:{APPROX})?{SEGMENT})+)')
APPROX_TEST = re.compile(APPROX)

OPERATIONS = {
    ast.Add: operator.add, ast.Sub: operator.sub,
    ast.Mult: operator.mul, ast.Div: operator.truediv,
    ast.USub: operator.neg, ast.UAdd: operator.pos,
}


def evaluate(node):
    if isinstance(node, ast.Expression):
        return evaluate(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return float(node.value)
    if isinstance(node, ast.BinOp) and type(node.op) in OPERATIONS:
        return OPERATIONS[type(node.op)](evaluate(node.left), evaluate(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in OPERATIONS:
        return OPERATIONS[type(node.op)](evaluate(node.operand))
    raise ValueError('unsupported syntax')


def segment_value(text):
    """Evaluate one side of an equality; returns (value, decimals, has_percent)."""
    cleaned = text.replace('×', '*').replace('÷', '/').replace('−', '-')
    cleaned = re.sub(r'[$€£¥₹,…]', '', cleaned)
    has_percent = '%' in cleaned
    decimals = max((len(m) for m in re.findall(r'\.(\d+)', cleaned)), default=0)
    cleaned = re.sub(r'(\d+(?:\.\d+)?)%', r'(\1/100)', cleaned)
    value = evaluate(ast.parse(cleaned.strip(), mode='eval'))
    if has_percent:
        decimals += 2
    return value, decimals, has_percent


def matches(left, right, decimals, percent, approximate):
    tolerance = (1.0 if approximate else 0.5) * 10 ** -decimals + 1e-9
    if abs(left - right) <= tolerance:
        return True
    # "$300 ÷ $1,000 × 100 = 30%": accept percentage points against a % figure.
    return percent and abs(left - right * 100) <= tolerance * 100


def check_file(path, verbose):
    failures, checked = [], 0
    for line_number, line in enumerate(path.read_text().splitlines(), start=1):
        if '=' not in line:
            continue
        plain = line.replace('**', '')
        for match in STATEMENT.finditer(plain):
            segments = [s for s in re.split(r'=', match.group(0)) if s.strip()]
            if len(segments) < 2 or not re.search(OPERATOR, match.group(0)):
                continue
            values = []
            for segment in segments:
                approximate = bool(APPROX_TEST.match(segment.strip()))
                body = APPROX_TEST.sub('', segment, count=1)
                try:
                    values.append(segment_value(body) + (approximate,))
                except (ValueError, SyntaxError, ZeroDivisionError):
                    values = None
                    break
            if values is None:
                if verbose:
                    print(f'{path}:{line_number}: skipped: {match.group(0).strip()}')
                continue
            checked += 1
            for (left, _, _, _), (right, decimals, percent, approx) in zip(values, values[1:]):
                if not matches(left, right, decimals, percent, approx):
                    failures.append(
                        f'{path}:{line_number}: "{match.group(0).strip()}" — '
                        f'{left:.6g} does not equal stated {right:.6g}')
    return checked, failures


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('paths', nargs='*', default=['knowledge'],
                        help='Markdown files or directories to scan (default: knowledge/)')
    parser.add_argument('--verbose', action='store_true',
                        help='List statements that looked numeric but could not be parsed')
    args = parser.parse_args()

    files = []
    for raw in args.paths:
        path = Path(raw)
        files.extend(sorted(path.rglob('*.md')) if path.is_dir() else [path])

    total, failures = 0, []
    for path in files:
        checked, found = check_file(path, args.verbose)
        total += checked
        failures.extend(found)

    if failures:
        raise SystemExit('\n'.join(failures))
    print(f'Verified {total} inline calculations across {len(files)} files.')


if __name__ == '__main__':
    main()
