---
layout: default
title: Quantitative finance and financial data
permalink: /knowledge/quantitative-finance-and-financial-data/
glossary_terms:
  quantitative-finance: what-quantitative-finance-does
  dataset: what-quantitative-finance-does
  model: what-quantitative-finance-does
  probability: describing-uncertainty-with-probability
  expected-value: describing-uncertainty-with-probability
  expected-loss: describing-uncertainty-with-probability
  return: summarizing-data-with-typical-values
  mean: summarizing-data-with-typical-values
  median: summarizing-data-with-typical-values
  variance: measuring-spread-and-extreme-outcomes
  standard-deviation: measuring-spread-and-extreme-outcomes
  normal-distribution: measuring-spread-and-extreme-outcomes
  risk: measuring-spread-and-extreme-outcomes
  correlation: how-variables-move-together
  correlation-coefficient: how-variables-move-together
  linear-regression: how-variables-move-together
  diversification: how-variables-move-together
  time-series: patterns-over-time-and-forecasting
  trend: patterns-over-time-and-forecasting
  seasonality: patterns-over-time-and-forecasting
  forecast: patterns-over-time-and-forecasting
  overfitting: patterns-over-time-and-forecasting
  inflation: patterns-over-time-and-forecasting
  data-quality: data-you-can-trust-and-work-you-can-repeat
  survivorship-bias: data-you-can-trust-and-work-you-can-repeat
  look-ahead-bias: data-you-can-trust-and-work-you-can-repeat
  reproducibility: data-you-can-trust-and-work-you-can-repeat
  backtesting: testing-models-and-knowing-their-limits
  model-risk: testing-models-and-knowing-their-limits
  benchmark: testing-models-and-knowing-their-limits
  stress-testing: testing-models-and-knowing-their-limits
---

# Quantitative finance and financial data

Learn how numbers, probability, and simple models help answer financial questions, how to summarize and question data, and where the answers stop being trustworthy.

[← All knowledge areas]({{ '/knowledge/' | relative_url }}) · [Glossary]({{ '/glossary/' | relative_url }})

No programming or advanced mathematics is needed. Familiarity with percentages helps; [Money and financial fundamentals]({{ '/knowledge/money-and-financial-fundamentals/' | relative_url }}) introduces them alongside interest, returns, and risk. New finance and data terms are **bold**, explained on first use, and linked to the glossary. Each glossary entry links back to its explanation here.

### Example assumptions

Every dataset, price, return, and probability below is an invented teaching example, not market data or a forecast of any real investment. Unless a section says otherwise, ignore fees and taxes, and treat displayed results as rounded to the precision shown. "Percentage points" means the plain difference between two percentages: a move from 1% to 3% is a rise of 2 percentage points.

## In this lesson

1. [What quantitative finance does](#what-quantitative-finance-does)
2. [Describing uncertainty with probability](#describing-uncertainty-with-probability)
3. [Summarizing data with typical values](#summarizing-data-with-typical-values)
4. [Measuring spread and extreme outcomes](#measuring-spread-and-extreme-outcomes)
5. [How variables move together](#how-variables-move-together)
6. [Patterns over time and forecasting](#patterns-over-time-and-forecasting)
7. [Data you can trust and work you can repeat](#data-you-can-trust-and-work-you-can-repeat)
8. [Testing models and knowing their limits](#testing-models-and-knowing-their-limits)
9. [Check your understanding](#check-your-understanding)

## What quantitative finance does

An insurer estimates next year's claims. A lender asks which borrowers might miss payments. A saver asks how long a lump sum might last. All three are turning financial questions into questions about numbers.

**[Quantitative finance]({{ '/glossary/' | relative_url }}#quantitative-finance)** means using mathematics, statistics, and computing to investigate financial questions, price instruments, and manage risk. The raw material is a **[dataset]({{ '/glossary/' | relative_url }}#dataset)**: an organized collection of related values, such as a table of monthly prices. The main tool is a **[model]({{ '/glossary/' | relative_url }}#model)**: a simplified description of a situation used to estimate, explain, or test something.

A city map is a useful comparison. A map leaves out almost everything about a city, yet helps you navigate because what it leaves out rarely matters for finding a street. A model works the same way: it is useful when what it leaves out does not matter for the question at hand, and dangerous when it does.

Two habits separate careful number work from misleading number work, and they run through this lesson: check the data before trusting it, and test claims honestly before relying on them.

## Describing uncertainty with probability

Flip a fair coin. You cannot say which side lands up, but you can say each side is equally likely. A **[probability]({{ '/glossary/' | relative_url }}#probability)** measures how likely an event is on a scale from 0 (impossible) to 1 (certain), often written as a percentage. A fair coin lands heads with probability 0.5, or 50%. That is not a promise that two flips give one head; it describes what to expect on average over many flips.

Money questions rarely come with coin-flip certainty, so we attach estimated probabilities to possible outcomes and compute an average over them. The **[expected value]({{ '/glossary/' | relative_url }}#expected-value)** is the probability-weighted average of all possible outcomes: multiply each outcome by its probability, then add the results.

**Worked example (invented).** An investment costs $100 today. After one year, only two outcomes are possible: it is worth $120 with probability 0.5, or $90 with probability 0.5.

- 0.5 × $120 = $60
- 0.5 × $90 = $45
- Expected value: $60 + $45 = **$105**, an expected gain of $5.

In any single year you receive $120 or $90, never $105. The expected value describes the average over many repeats of the same situation. Compare it with a savings account paying a certain $103: the uncertain investment has the higher expected value, but the account cannot return $90. Expected value summarizes the average; it stays silent about the spread of outcomes, which the next two sections measure. Insurers apply the same arithmetic to costs: an **[expected loss]({{ '/glossary/' | relative_url }}#expected-loss)** is a probability-weighted average loss used when pricing coverage.

Outside textbooks, probabilities are usually estimated from data or judgment rather than known. Treat the estimate as an ingredient that can be wrong, not a fact.

## Summarizing data with typical values

Raw columns of numbers are hard to read, so we summarize them. Suppose an invented fund's monthly **[return]({{ '/glossary/' | relative_url }}#return)** — its gain or loss over each month, as a percentage — looked like this:

| Month | Return |
| --- | ---: |
| 1 | +2% |
| 2 | −1% |
| 3 | +3% |
| 4 | 0% |
| 5 | +1% |

The **[mean]({{ '/glossary/' | relative_url }}#mean)**, also called the average, is the sum divided by the count: (2 − 1 + 3 + 0 + 1) ÷ 5 = 5 ÷ 5 = **1% per month**.

The **[median]({{ '/glossary/' | relative_url }}#median)** is the middle value when the data are placed in order: −1%, 0%, **+1%**, +2%, +3%. Two values sit below it and two above.

Now suppose month 3 had been +13% instead of +3%. The mean becomes (2 − 1 + 13 + 0 + 1) ÷ 5 = 15 ÷ 5 = **3%**, while the median stays at **1%**. One extreme month pulled the mean up by 2 percentage points and left the median unmoved. Report both when they tell different stories, and ask which one a writer chose when you see only an "average."

## Measuring spread and extreme outcomes

Two funds can share the same 1% average month while one barely moves and the other swings wildly. Spread is measured in two steps. First, take each value's difference from the mean and square it, which removes the sign:

| Month | Return | Difference from mean (1%) | Squared difference |
| --- | ---: | ---: | ---: |
| 1 | +2% | +1 | 1 |
| 2 | −1% | −2 | 4 |
| 3 | +3% | +2 | 4 |
| 4 | 0% | −1 | 1 |
| 5 | +1% | 0 | 0 |

The **[variance]({{ '/glossary/' | relative_url }}#variance)** is the average of those squared differences: (1 + 4 + 4 + 1 + 0) ÷ 5 = 10 ÷ 5 = **2**, in the awkward units of "squared percent." Taking the square root returns to the original units: the **[standard deviation]({{ '/glossary/' | relative_url }}#standard-deviation)** is √2 ≈ **1.41%**. A larger standard deviation means wider typical swings around the mean. Some tools divide by the count minus one instead of the count, giving 2.5 and about 1.58% for the same data; both conventions measure the same idea, so consistency matters more than the choice when comparing datasets.

If data follow the symmetric, bell-shaped pattern called the **[normal distribution]({{ '/glossary/' | relative_url }}#normal-distribution)**, a rule of thumb says about 68% of values fall within one standard deviation of the mean and about 95% within two. With a mean of 1% and a standard deviation of 1.41%, that suggests roughly 68% of months between −0.41% and +2.41%. Treat this as a rough guide only: real return series tend to produce extreme months more often than the bell curve predicts, and standard deviation does not capture every kind of **[risk]({{ '/glossary/' | relative_url }}#risk)**. A fund can look calm for years precisely because its losses arrive rarely and all at once. For deeper reading, see the [NIST/SEMATECH e-Handbook of Statistical Methods](https://www.itl.nist.gov/div898/handbook/).

## How variables move together

Do two investments rise and fall together? **[Correlation]({{ '/glossary/' | relative_url }}#correlation)** describes a tendency for two measures to move together to some degree. The **[correlation coefficient]({{ '/glossary/' | relative_url }}#correlation-coefficient)** compresses that tendency into one number between −1 and 1. Spreadsheet functions such as CORREL compute it; here is the intuition on invented monthly returns:

| Month | Fund X | Fund Y (always 2 × Fund X) | Fund Z (exact mirror) | Fund W |
| --- | ---: | ---: | ---: | ---: |
| 1 | −2% | −4% | +2% | +1% |
| 2 | −1% | −2% | +1% | −1% |
| 3 | +1% | +2% | −1% | −1% |
| 4 | +2% | +4% | −2% | +1% |
| **Correlation with Fund X** | | **+1** | **−1** | **0** |

A coefficient of +1 means perfectly aligned straight-line movement, −1 means perfect opposition, and 0 means no straight-line relationship at all. Real portfolios almost always sit between the extremes.

Two warnings matter more than the formula. First, correlation is not causation: two bank shares may fall together because a third force, such as an interest-rate change, moves both. Second, correlations change over time and often rise toward 1 during market-wide sell-offs, exactly when spreading money across holdings is most needed. **[Diversification]({{ '/glossary/' | relative_url }}#diversification)** relies on holdings being less than perfectly correlated; combining holdings with a coefficient of +1 provides no smoothing at all.

A related question asks *how much* one measure moves when another moves. **[Linear regression]({{ '/glossary/' | relative_url }}#linear-regression)** fits a straight line, written y = a + b × x, to past data. Suppose an invented benchmark returned 1%, 2%, and 3% over three months while a fund returned 2.5%, 4.5%, and 6.5%. The exact line is y = 0.5 + 2 × x: an intercept of 0.5% and a slope of 2, meaning the fund tended to move about 2% for each 1% move in the benchmark. Three months of invented data prove nothing about the future; the line summarizes a past relationship that can weaken or break.

## Patterns over time and forecasting

A **[time series]({{ '/glossary/' | relative_url }}#time-series)** is a sequence of observations recorded in time order, such as monthly **[inflation]({{ '/glossary/' | relative_url }}#inflation)** readings or a portfolio's monthly values. Two recurring features shape such series. A **[trend]({{ '/glossary/' | relative_url }}#trend)** is a persistent general direction; **[seasonality]({{ '/glossary/' | relative_url }}#seasonality)** is a pattern that repeats at known times, such as stronger retail sales in certain months.

Suppose a small business earned $10,000 in January, $11,000 in February, and $12,000 in March. Three simple **[forecasts]({{ '/glossary/' | relative_url }}#forecast)** for April:

| Method | Rule | April forecast |
| --- | --- | ---: |
| Naive | Repeat the latest month | $12,000 |
| Recent average | Average the last three months | $11,000 |
| Trend extension | Continue the +$1,000 monthly trend | $13,000 |

April's actual revenue is $11,500. The errors (actual minus forecast) are −$500 for the naive forecast, +$500 for the average, and −$1,500 for the trend. No method "won"; one month proves nothing. Forecasting methods are judged by their errors over many months, not one.

The temptation with more data is to build an ever more complicated rule that matches the past perfectly. That is **[overfitting]({{ '/glossary/' | relative_url }}#overfitting)**: fitting the noise along with the pattern, so the rule fails on the next new month. Prefer simple rules you can explain, and keep some data untouched for testing, as the final section describes.

## Data you can trust and work you can repeat

Every calculation above is only as good as its inputs. **[Data quality]({{ '/glossary/' | relative_url }}#data-quality)** covers how accurate, complete, consistent, and timely a dataset is for the use you have in mind. Imagine downloading a dataset of fund returns and finding months missing for some funds, one fund recorded in dollars while the rest are in thousands of dollars, and several duplicated rows. Each flaw silently changes any average or correlation computed from it.

Two flaws cannot be spotted in the numbers themselves. **[Survivorship bias]({{ '/glossary/' | relative_url }}#survivorship-bias)** arises when the data include only survivors: a fund database that omits funds that closed makes average past returns look better than what investors actually experienced. **[Look-ahead bias]({{ '/glossary/' | relative_url }}#look-ahead-bias)** arises when an analysis uses information that would not have been available at the time being studied, such as testing a historical strategy with final, revised statistics rather than the figures published on the day. Official statistics are often revised after first release; the St. Louis Fed's [ALFRED archive](https://alfred.stlouisfed.org) preserves the vintages, showing what was known when.

**[Reproducibility]({{ '/glossary/' | relative_url }}#reproducibility)** is the habit that makes your work checkable: anyone, including future you, should get the same result from the same data and steps. Keep the raw download unchanged, make changes through a script rather than untracked edits, and record sources and retrieval dates alongside the result.

## Testing models and knowing their limits

**[Backtesting]({{ '/glossary/' | relative_url }}#backtesting)** evaluates how a strategy or model would have performed on historical data. Consider an invented market's six monthly returns: +2%, −1%, +3%, −2%, +1%, +2%. A friend proposes a timing rule: only hold the investment in a month that follows an up month.

| Month | Market return | Rule says invested? | Strategy return |
| --- | ---: | --- | ---: |
| 1 | +2% | No signal yet | 0% |
| 2 | −1% | Yes (month 1 was up) | −1% |
| 3 | +3% | No | 0% |
| 4 | −2% | Yes | −2% |
| 5 | +1% | No | 0% |
| 6 | +2% | Yes | +2% |

Compounding month by month, simply holding the investment turns $100 into about $105.01 (+5.0%), while the rule turns it into about $98.96 (−1.0%). The rule avoided months 3 and 5 but missed the gains in months 3 and 6, and was fully exposed to both falling months it entered. Here the comparison baseline — holding throughout — is the **[benchmark]({{ '/glossary/' | relative_url }}#benchmark)**, and the rule lost to it.

Even a winning backtest would prove little. Six months is a tiny sample; the rule may have been chosen *because* it fit this particular past; and fees and taxes, ignored here, would lower the rule's result further. Honest evaluation also means testing periods the rule was not designed on and applying **[stress testing]({{ '/glossary/' | relative_url }}#stress-testing)**: examining outcomes under severe assumptions rather than average ones.

The broader lesson is **[model risk]({{ '/glossary/' | relative_url }}#model-risk)**: the possibility of loss or poor decisions because a model is wrong, built on flawed data, or used where it does not fit. Banks face formal expectations for managing it — see the [US Federal Reserve's guidance on model risk management](https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm) — and the same question serves any user of models: what would make this model wrong, and how would I notice?

## Check your understanding

Try these before reading the answers:

1. An uncertain outcome pays $30 with probability 0.6 and loses $20 with probability 0.4. What is its expected value, and does it rule out losing $20?
2. For the dataset 4, 6, 10, 20, calculate the mean and the median. Which one did the value 20 pull toward itself?
3. Two funds both averaged 1% per month, with standard deviations of 0.8% and 2.5%. Which swung more widely, and does the answer by itself promise a larger future loss for either fund?
4. Two funds have a correlation coefficient of −0.9. What does that suggest about how they move, and does it prove one causes the other's moves?
5. A friend designs a trading rule on 2016–2025 data, tests it on the same years, and uses a fund database that omits funds that closed. Name two distinct problems with the test.

### Answers

1. **$10.** Expected value is 0.6 × $30 + 0.4 × (−$20) = $18 − $8 = $10. It is a long-run average: any single play can still lose $20, so the expected value does not remove the risk.
2. **Mean 10, median 8.** The sum is 40, divided by 4 values. Ordered, the middle two are 6 and 10, averaging 8. The mean was pulled toward 20; it sits above three of the four values, while the median still marks the middle.
3. **The fund with 2.5% standard deviation swung more widely around its 1% average.** But standard deviation summarizes past spread; neither figure by itself promises a particular future loss, and it says nothing about rare extreme events.
4. **They have strongly tended to move in opposite directions.** A coefficient near −1 indicates strong opposition, but correlation alone cannot prove causation; both funds might respond to some third influence.
5. **Any two of these three:** designing and testing on the same data invites overfitting; omitting closed funds is survivorship bias, which inflates historical results; and if the test used final revised figures rather than what was published at the time, that is look-ahead bias.

## Terms introduced in this lesson

Use these links to revisit definitions. Each glossary entry has a link back to its explanation above.

{% assign lesson_terms = site.data.glossary | sort: 'term' %}
{% for term in lesson_terms %}{% if page.glossary_terms[term.id] %}
- [{{ term.term }}]({{ '/glossary/' | relative_url }}#{{ term.id }})
{% endif %}{% endfor %}

## Keep learning

Apply these ideas to portfolios in [Investing and portfolio management]({{ '/knowledge/investing-and-portfolio-management/' | relative_url }}), and to the statistics that move markets in [Economics and the financial system]({{ '/knowledge/economics-and-the-financial-system/' | relative_url }}). [Financial technology and open finance]({{ '/knowledge/financial-technology-and-open-finance/' | relative_url }}) covers how financial data moves between systems through APIs and shared data standards.

Planned deeper lessons for this area include time-series econometrics, simulation methods, and data visualization. They are not published yet.
