---
layout: default
title: Blockchain and decentralized finance
permalink: /knowledge/blockchain-and-decentralized-finance/
glossary_terms:
  blockchain: understand-the-shared-record
  blockchain-node: understand-the-shared-record
  consensus-mechanism: understand-the-shared-record
  blockchain-finality: understand-the-shared-record
  proof-of-stake: understand-the-shared-record
  crypto-wallet: separate-wallets-from-custody
  private-key: separate-wallets-from-custody
  recovery-phrase: separate-wallets-from-custody
  custody: separate-wallets-from-custody
  self-custody: separate-wallets-from-custody
  smart-contract: understand-smart-contracts-and-fees
  decentralized-finance: understand-smart-contracts-and-fees
  defi-protocol: understand-smart-contracts-and-fees
  gas: understand-smart-contracts-and-fees
  crypto-token: ask-what-a-token-represents
  stablecoin: ask-what-a-token-represents
  tokenization: ask-what-a-token-represents
  decentralized-exchange: trade-through-a-pool
  automated-market-maker: trade-through-a-pool
  liquidity-pool: trade-through-a-pool
  price-impact: trade-through-a-pool
  slippage: trade-through-a-pool
  impermanent-loss: trade-through-a-pool
  collateral: borrow-against-collateral
  liquidation: borrow-against-collateral
  blockchain-oracle: find-the-remaining-dependencies
  blockchain-bridge: find-the-remaining-dependencies
  protocol-governance: find-the-remaining-dependencies
  smart-contract-security-audit: find-the-remaining-dependencies
description: "Learn how blockchains, wallets, smart contracts, and decentralized trading and lending work, with examples of transactions, collateral, returns, and risks."
---

# Blockchain and decentralized finance

Learn how blockchain transactions work, what a wallet controls, and how decentralized trading and lending change financial risks rather than removing them.

[← All knowledge areas]({{ '/knowledge/' | relative_url }}) · [Glossary]({{ '/glossary/' | relative_url }})

No prior blockchain knowledge is needed. New terms are **bold**, explained on first use, and linked to the glossary, which links back to their explanations here. Familiarity with [Money and financial fundamentals]({{ '/knowledge/money-and-financial-fundamentals/' | relative_url }}) is helpful but not required.

All token names, balances, prices, rates, and thresholds in the calculations are invented. Dollar values mean U.S. dollars. Examples ignore taxes and fees except where stated, assume no additional deposits or withdrawals, and identify their time periods. Named networks and protocols illustrate mechanisms, not recommendations. Their documentation was checked on **13 September 2026**; implementations, parameters, and legal treatment can change. No wallet or real-money transaction is needed to complete this lesson.

## In this lesson

1. [Understand the shared record](#understand-the-shared-record)
2. [Separate wallets from custody](#separate-wallets-from-custody)
3. [Understand smart contracts and fees](#understand-smart-contracts-and-fees)
4. [Ask what a token represents](#ask-what-a-token-represents)
5. [Trade through a pool](#trade-through-a-pool)
6. [Borrow against collateral](#borrow-against-collateral)
7. [Measure returns in money you can use](#measure-returns-in-money-you-can-use)
8. [Find the remaining dependencies](#find-the-remaining-dependencies)
9. [Check your understanding](#check-your-understanding)

## Understand the shared record

Imagine several computers maintaining the same transaction history. They need a way to reject invalid payments and agree which valid transactions happened first.

A **[blockchain]({{ '/glossary/' | relative_url }}#blockchain)** is a shared digital record whose transactions are grouped into blocks linked using cryptographic techniques that make changes detectable. A **[node]({{ '/glossary/' | relative_url }}#blockchain-node)** is a computer running network software; its duties depend on the network and node type. A **[consensus mechanism]({{ '/glossary/' | relative_url }}#consensus-mechanism)** is the system participants use to agree on the accepted history and state of the network.

A typical payment follows these steps:

1. The sender authorizes a transaction.
2. The transaction is broadcast to the network.
3. Participants check it against the network's rules, including whether spending is authorized and funds are available.
4. It is included in a block and gains the network's required level of confirmation.

**[Finality]({{ '/glossary/' | relative_url }}#blockchain-finality)** describes when a transaction is treated as settled under the network's rules and security assumptions. A transaction appearing in a wallet is not necessarily final. Networks differ in timing and in how they handle competing histories or failures.

**[Proof of stake]({{ '/glossary/' | relative_url }}#proof-of-stake)** is a consensus approach in which participants commit network assets to help secure the system, with rewards and penalties under its rules. Ethereum uses this approach. Other networks use different mechanisms; they do not all share Ethereum's rules. See [Ethereum's technical introduction](https://ethereum.org/developers/docs/intro-to-ethereum/).

A blockchain can verify that a transaction follows its rules. It cannot, on that basis alone, establish that an investment is valuable or that a real-world claim is true.

## Separate wallets from custody

A **[crypto wallet]({{ '/glossary/' | relative_url }}#crypto-wallet)** is an application or device used to interact with blockchain accounts and authorize actions. The asset record is on the network, not a pile of coins inside the device.

A **[private key]({{ '/glossary/' | relative_url }}#private-key)** is secret cryptographic information used to authorize actions for an account. A **[recovery phrase]({{ '/glossary/' | relative_url }}#recovery-phrase)** is a sequence of words that many wallets use to recover keys. Anyone who obtains the relevant secret may be able to control the account. Some wallet designs instead use multiple keys or other recovery arrangements. See [Ethereum's account documentation](https://ethereum.org/developers/docs/accounts/) and [wallet overview](https://ethereum.org/wallets/).

**[Custody]({{ '/glossary/' | relative_url }}#custody)** concerns who holds or controls assets or the means of accessing them. With **[self-custody]({{ '/glossary/' | relative_url }}#self-custody)**, users control their own keys or authorization arrangements. With a custodial service, a provider controls access on their behalf.

| Arrangement | What to understand |
| --- | --- |
| Self-custody | How authorization and recovery work; losing all recovery methods may mean permanent loss of access. |
| Custodial service | Withdrawal conditions, security, legal ownership, and what happens if the provider fails. |

Self-custody does not protect against approving a malicious action. A token-spending approval may let an application transfer a specified amount of tokens later; it is different from simply viewing a balance. Never provide a recovery phrase to someone claiming to be support. Public blockchain activity can often be traced even when addresses do not display people's names.

## Understand smart contracts and fees

A **[smart contract]({{ '/glossary/' | relative_url }}#smart-contract)** is a program deployed on a blockchain that executes according to its code when invoked. It can implement rules for exchanging or lending assets. The name does not mean the code is intelligent, error-free, or necessarily a legally enforceable contract. See [Ethereum's smart-contract introduction](https://ethereum.org/developers/docs/smart-contracts/).

**[Decentralized finance]({{ '/glossary/' | relative_url }}#decentralized-finance)**, often shortened to **DeFi**, uses blockchain-based programs to provide financial functions such as trading and lending. A **[DeFi protocol]({{ '/glossary/' | relative_url }}#defi-protocol)** is the set of program rules and mechanisms through which such a service operates. A website is one way to access it; the website and the underlying contracts are different components.

On Ethereum, **[gas]({{ '/glossary/' | relative_url }}#gas)** measures the computational work a transaction uses. Its transaction fee depends on gas used and the effective price per gas unit. Fees are paid in ether, Ethereum's native asset, abbreviated ETH. See [Ethereum's gas documentation](https://ethereum.org/developers/docs/gas/).

For an invented transaction using 50,000 gas units at 0.00000002 ETH per unit:

- Network fee: 50,000 × 0.00000002 = **0.001 ETH**.
- At an assumed $2,000 per ETH: 0.001 × $2,000 = **$2**.

That fee pays for execution, not for the asset being purchased. Application charges can be additional. A failed execution can still consume gas and cost money even when the intended asset transfer does not complete. Other networks and scaling systems have different fee structures.

## Ask what a token represents

A **[token]({{ '/glossary/' | relative_url }}#crypto-token)** is a digital unit recorded on a blockchain that may represent access, a claim, voting power, or something else defined by its design. Holding one does not automatically establish ownership of a business or entitlement to income.

A **[stablecoin]({{ '/glossary/' | relative_url }}#stablecoin)** is a cryptoasset designed to track a reference value, commonly one dollar. Different designs rely on reserve assets, other cryptoassets, or market incentives. A target is not a guaranteed market price or an unconditional right to redeem for cash. Check who can redeem, with whom, and on what terms. See [Ethereum's stablecoin overview](https://ethereum.org/stablecoins/).

If 1,000 units bought for $1 each can later be sold for only $0.92 each, their sale value is **$920** before fees. The **$80 loss** is 8% of the original $1,000, despite an unchanged token count.

**[Tokenization]({{ '/glossary/' | relative_url }}#tokenization)** means representing an asset or claim with a digital token. If a token is said to represent gold, someone still needs to hold the gold, establish the holder's legal rights, and honor redemption. A transferable record alone does not resolve those obligations. The [Bank for International Settlements discusses tokenization and stablecoins](https://www.bis.org/publications/iii-anchoring-trust-money-innovation-beyond-stablecoins).

## Trade through a pool

A **[decentralized exchange]({{ '/glossary/' | relative_url }}#decentralized-exchange)** is a trading system using blockchain programs to execute exchanges. Some use an **[automated market maker]({{ '/glossary/' | relative_url }}#automated-market-maker)**, a mechanism that prices trades using a formula and assets held in a **[liquidity pool]({{ '/glossary/' | relative_url }}#liquidity-pool)**, a shared reserve available for trades.

Consider a simplified pool with 100 units of Token A and 1,000 units of Token B. Assume no trading fees, no other trades, and no deposits or withdrawals during the swap. Its rule keeps the product of its two balances constant:

100 × 1,000 = **100,000**.

A trader puts in 10 A. The new A balance is 110. To keep the product at 100,000:

1. New B balance: 100,000 ÷ 110 = about **909.09 B**.
2. B paid to the trader: 1,000 − 909.09 = about **90.91 B**.
3. Average execution price: 90.91 ÷ 10 = about **9.09 B per A**.

The initial marginal price—the rate for a very small trade—was 1,000 ÷ 100 = **10 B per A**. The trader does not receive 100 B because the trade itself changes the pool's balances and price. Calculations use full precision before rounding to two decimals. This is a teaching model of a constant-product pool, not a description of every decentralized exchange. See [Uniswap's explanation of pool mechanics](https://developers.uniswap.org/docs/get-started/concepts/how-uniswap-works).

**[Price impact]({{ '/glossary/' | relative_url }}#price-impact)** is the change in execution price caused by your own trade. **[Slippage]({{ '/glossary/' | relative_url }}#slippage)** is the difference between an expected execution result and the actual one, for example when other trades occur before yours. Terminology can overlap in trading interfaces. An output limit can cause an unacceptable trade to fail; it cannot make liquidity appear or necessarily avoid a network fee.

People supplying pool assets may receive trading fees but face changing asset balances. **[Impermanent loss]({{ '/glossary/' | relative_url }}#impermanent-loss)** describes a liquidity provider's shortfall relative to holding the deposited assets outside the pool as relative prices change, usually measured before fees. The name does not promise recovery. Fee income may or may not offset that shortfall. See [Uniswap's explanation of impermanent loss](https://support.uniswap.org/hc/en-us/articles/20904453751693-What-is-Impermanent-Loss).

## Borrow against collateral

**[Collateral]({{ '/glossary/' | relative_url }}#collateral)** is property pledged to support borrowing. Many DeFi lending systems require collateral worth more than the debt. **[Liquidation]({{ '/glossary/' | relative_url }}#liquidation)** in this context means a mechanism repays some or all of a risky loan in exchange for taking collateral under the protocol's rules, often with an additional charge to the borrower.

Assume collateral initially worth $2,000 supports $1,000 of debt. In this invented protocol, a position becomes eligible for liquidation when debt exceeds 75% of collateral value. Ignore interest, fees, and changes in the borrowed asset's dollar price.

| Collateral value | Debt divided by collateral | Above the 75% threshold? |
| --- | ---: | --- |
| $2,000 | $1,000 ÷ $2,000 = 50% | No |
| $1,500 | $1,000 ÷ $1,500 ≈ 66.67% | No |
| $1,200 | $1,000 ÷ $1,200 ≈ 83.33% | Yes |

The boundary is $1,000 ÷ 0.75 = about **$1,333.33** of collateral. The borrower can face liquidation while collateral is still worth more than the debt. Falling prices, growing interest, and changing protocol parameters can all affect the position. Actual liquidation timing and amounts depend on the system; the threshold does not promise a particular sale price. See [Aave's explanation of collateral health and liquidation](https://aave.com/help/borrowing/liquidations).

Borrowing is not income: the obligation remains. Supplying assets for others to borrow also creates risks, including losses or withdrawal delays if the system cannot recover enough collateral or make funds available.

## Measure returns in money you can use

Ask where any payout comes from: borrowers' interest, trading fees, newly issued tokens, or another source. A displayed rate can change and may depend on a reward token whose market price falls.

Suppose you supply 100 tokens worth $10 each, an initial value of **$1,000**. Over one year you receive five additional tokens and make no other transactions. At year-end all 105 tokens are worth $8 each:

- Final value: 105 × $8 = **$840**.
- Dollar change: $840 − $1,000 = **−$160**, or **−16%**.

A 5% increase in token count did not produce a positive dollar return. Fees and taxes would change the result further. The calculation is an assumed outcome, not a quoted yield.

Also ask whether a quoted annual figure assumes reinvesting rewards, whether principal can be withdrawn, and what can change the payout. The [BIS describes DeFi's financial and operational vulnerabilities](https://www.bis.org/publications/fsi-summary-financial-stability-risks-decentralised-finance-executive-summary).

## Find the remaining dependencies

Decentralization has several dimensions: who validates transactions, operates access points, supplies data, changes contracts, and controls assets. They can be distributed differently.

| Dependency | Why it matters |
| --- | --- |
| **[Oracle]({{ '/glossary/' | relative_url }}#blockchain-oracle)**: a mechanism supplying outside information to blockchain programs. | A lending program can act on a wrong or manipulated price. |
| **[Blockchain bridge]({{ '/glossary/' | relative_url }}#blockchain-bridge)**: a system connecting assets or messages across networks. | Users depend on its verification and asset-backing arrangements as well as each network. |
| **[Protocol governance]({{ '/glossary/' | relative_url }}#protocol-governance)**: the process for deciding changes to a protocol. | Voting power or emergency control may be concentrated in a few hands. |
| **[Smart-contract security audit]({{ '/glossary/' | relative_url }}#smart-contract-security-audit)**: a review of code for vulnerabilities within a stated scope. | It can find defects but cannot guarantee safety, especially after code changes. |

See the [BIS explanation of the oracle problem](https://www.bis.org/publications/bulletin-76-oracle-problem-and-future-defi), [Ethereum's bridge documentation](https://ethereum.org/developers/docs/bridges/), and [Ethereum's smart-contract security guidance](https://ethereum.org/developers/docs/smart-contracts/security/).

Before assessing a service, identify who can pause it, upgrade its code, freeze a token, or restrict withdrawals. Trace dependencies when one protocol accepts a token issued by another: a failure can spread. A public codebase and a governance vote do not establish that control is widely shared. The [BIS examines concentration in DeFi governance](https://www.bis.org/publications/defi-risks-and-decentralisation-illusion).

Legal rights and routes for complaints depend on the activity, parties, and jurisdiction. The label “decentralized” does not establish that an activity is exempt from law or that users have deposit protection or a right to reimbursement. Technical reversibility and legal remedies are separate questions.

## Check your understanding

Try these before reading the answers:

1. Does a wallet store the blockchain's asset record, and does self-custody remove the risk of approving a malicious transaction?
2. A transaction uses 80,000 gas units at 0.00000002 ETH per unit. At $2,000 per ETH, what is the network fee in ETH and dollars?
3. In the original 100 A / 1,000 B pool, a trader adds 25 A. With no fees or other activity, how much B comes out?
4. Under the lending example, debt remains $1,000 but collateral is worth $1,250. Is it above the liquidation threshold?
5. You start with 200 tokens worth $5 each and finish a year with 220 worth $4 each. What is the dollar return before fees and taxes?
6. A lending contract executes its code correctly using an incorrect external price. Which dependency failed, and why is correct execution insufficient?

### Answers

1. **The asset record is on the network; no.** The wallet manages interaction and authorization. Self-custody changes who controls access, but a harmful approval can still allow assets to be taken.
2. **0.0016 ETH, or $3.20.** 80,000 × 0.00000002 = 0.0016 ETH; multiply by $2,000. Application charges, if any, are additional.
3. **200 B.** The new A balance is 125. The required B balance is 100,000 ÷ 125 = 800. The trader receives 1,000 − 800 = 200 B, averaging 8 B per A.
4. **Yes.** $1,000 ÷ $1,250 = 80%, above the assumed 75%. Collateral exceeding debt does not rule out liquidation.
5. **−12%.** Starting value is 200 × $5 = $1,000; ending value is 220 × $4 = $880. The $120 loss divided by $1,000 is 12%, despite a 10% token-count increase.
6. **The oracle or its underlying data source.** A program can follow its rules accurately while using bad information. Network consensus does not establish that the external price is correct.

## Terms introduced in this lesson

Each definition links back to its explanation above.

{% assign lesson_terms = site.data.glossary | sort: 'term' %}
{% for term in lesson_terms %}{% if page.glossary_terms[term.id] %}
- [{{ term.term }}]({{ '/glossary/' | relative_url }}#{{ term.id }})
{% endif %}{% endfor %}

## Keep learning

Continue with [Financial markets and instruments]({{ '/knowledge/financial-markets-and-instruments/' | relative_url }}) for trading and leverage, [Financial technology and open finance]({{ '/knowledge/financial-technology-and-open-finance/' | relative_url }}) for data sharing and access, and [Financial law, ethics, and consumer protection]({{ '/knowledge/financial-law-ethics-and-consumer-protection/' | relative_url }}) for evaluating providers and resolving problems.

Further lessons are planned on consensus tradeoffs, scaling networks, stablecoin designs, liquidity-provider calculations, protocol governance, and jurisdiction-specific legal questions.
