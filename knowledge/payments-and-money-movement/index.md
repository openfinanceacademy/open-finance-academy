---
layout: default
title: Payments and money movement
permalink: /knowledge/payments-and-money-movement/
glossary_terms:
  payment: follow-a-payment-from-payer-to-payee
  payer: follow-a-payment-from-payer-to-payee
  payee: follow-a-payment-from-payer-to-payee
  payment-instrument: follow-a-payment-from-payer-to-payee
  card-network: cards-and-card-networks
  card-issuer: cards-and-card-networks
  acquirer: cards-and-card-networks
  authorization: cards-and-card-networks
  interchange-fee: cards-and-card-networks
  bank-transfer: bank-transfers-direct-debits-and-instant-payments
  direct-debit: bank-transfers-direct-debits-and-instant-payments
  instant-payment: bank-transfers-direct-debits-and-instant-payments
  payment-processor: payment-processing-clearing-and-settlement
  clearing: payment-processing-clearing-and-settlement
  settlement: payment-processing-clearing-and-settlement
  payment-rail: payment-processing-clearing-and-settlement
  remittance: remittances-and-cross-border-payments
  cross-border-payment: remittances-and-cross-border-payments
  correspondent-bank: remittances-and-cross-border-payments
  wire-transfer: remittances-and-cross-border-payments
  exchange-rate: compare-the-cost-of-moving-money-abroad
  foreign-exchange-margin: compare-the-cost-of-moving-money-abroad
  authentication: fraud-prevention-disputes-and-payment-security
  strong-customer-authentication: fraud-prevention-disputes-and-payment-security
  fraud: fraud-prevention-disputes-and-payment-security
  dispute: fraud-prevention-disputes-and-payment-security
  chargeback: fraud-prevention-disputes-and-payment-security
---

# Payments and money movement

Learn how a payment moves from payer to payee, what happens behind a card swipe or a bank transfer, what it costs to send money across borders, and how to recognize and respond to payment fraud.

[← All knowledge areas]({{ '/knowledge/' | relative_url }}) · [Glossary]({{ '/glossary/' | relative_url }})

No prior payments experience is needed. [Banking, credit, and lending]({{ '/knowledge/banking-credit-and-lending/' | relative_url }}) introduces bank accounts and deposits, which this lesson builds on. New finance terms are **bold**, explained on first use, and linked to the glossary, which links back to each explanation.

### Example assumptions

The dollar amounts, fees, and exchange rates are invented teaching examples, not current pricing from any provider. Each example is independent. Unless stated otherwise, assume no taxes and no failed or reversed transactions beyond those described.

General explanations are intended to be useful across countries, but the specific institutions, timing, and consumer protections in a payment depend heavily on the country, the payment method, and the provider. U.S.-specific examples are labeled and use official sources checked September 13, 2026.

## In this lesson

1. [Follow a payment from payer to payee](#follow-a-payment-from-payer-to-payee)
2. [Cards and card networks](#cards-and-card-networks)
3. [Bank transfers, direct debits, and instant payments](#bank-transfers-direct-debits-and-instant-payments)
4. [Payment processing, clearing, and settlement](#payment-processing-clearing-and-settlement)
5. [Remittances and cross-border payments](#remittances-and-cross-border-payments)
6. [Compare the cost of moving money abroad](#compare-the-cost-of-moving-money-abroad)
7. [Fraud prevention, disputes, and payment security](#fraud-prevention-disputes-and-payment-security)
8. [Check your understanding](#check-your-understanding)

## Follow a payment from payer to payee

Noor runs a small shop: customers pay by card, a supplier is paid by bank transfer, and part of each month's profit is sent to family in another country. Each of these is a **[payment]({{ '/glossary/' | relative_url }}#payment)**: a transfer of money from a **[payer]({{ '/glossary/' | relative_url }}#payer)** to a **[payee]({{ '/glossary/' | relative_url }}#payee)**.

A **[payment instrument]({{ '/glossary/' | relative_url }}#payment-instrument)** is the method used to start a payment — a card, a bank transfer, a direct debit, or cash. The instrument a payer chooses affects how quickly the payee is paid, what it costs, what information each side shares, and what protections apply if something goes wrong. The rest of this lesson follows several instruments from the moment a payment starts to the moment money actually lands in the payee's account.

## Cards and card networks

When a customer pays Noor's shop with a card, at least four parties are usually involved: the customer, the **[card issuer]({{ '/glossary/' | relative_url }}#card-issuer)** (the customer's bank, which issued the card), Noor's **[acquirer]({{ '/glossary/' | relative_url }}#acquirer)** (the bank or provider that lets Noor accept cards), and a **[card network]({{ '/glossary/' | relative_url }}#card-network)** such as Visa or Mastercard that sets the rules and routes the transaction between the issuer and the acquirer.

When the card is tapped or entered, the issuer performs an **[authorization]({{ '/glossary/' | relative_url }}#authorization)**: a check, in seconds, of whether the account has enough available funds or credit and whether the transaction looks legitimate. Authorization approves that the payment can proceed; it does not by itself move the money.

Card acceptance is not free. An **[interchange fee]({{ '/glossary/' | relative_url }}#interchange-fee)** is paid by the acquirer to the card issuer on each transaction, and is normally built into the overall fee the acquirer charges the merchant. Suppose Noor's acquirer charges a combined rate of **2.9% of the sale plus a flat $0.30** per transaction, covering interchange and the acquirer's own margin. On a **$40** card sale:

- Percentage portion: $40 × 0.029 = **$1.16**.
- Total fee: $1.16 + $0.30 = **$1.46**.
- Amount Noor actually receives: $40 − $1.46 = **$38.54**.

The customer's statement shows $40; Noor's deposit is smaller. Rates, structures, and who bears the fee vary by provider, card type, and country. See the [BIS glossary of payment and settlement terms](https://www.bis.org/cpmi/publ/d00b.htm) for standard definitions used across the industry.

## Bank transfers, direct debits, and instant payments

A **[bank transfer]({{ '/glossary/' | relative_url }}#bank-transfer)** is an instruction to move money directly from one bank account to another; it is also called a credit transfer because the payer pushes money to the payee. Noor uses one to pay a supplier: Noor's bank reduces Noor's balance and instructs the supplier's bank to increase the supplier's balance.

A **[direct debit]({{ '/glossary/' | relative_url }}#direct-debit)** works the other way: the payee pulls money from the payer's account, under an authorization the payer set up in advance. Noor's landlord uses a direct debit to collect $1,200 rent on the first of each month without Noor initiating a transfer each time. Because the payee initiates it, a direct debit usually comes with cancellation and reversal rights so a payer is not left unprotected.

Ordinary bank transfers can take from same-day to a few business days to reach the payee, depending on the payment rail and country. An **[instant payment]({{ '/glossary/' | relative_url }}#instant-payment)** is a bank transfer processed and made available to the payee within seconds, at any time, including nights, weekends, and holidays. In the United States, the Federal Reserve operates the [FedNow instant payment service](https://www.frbservices.org/financial-services/fednow) for banks and credit unions; other countries operate their own instant-payment systems. Not every bank or payment participates, so instant availability depends on both the payer's and the payee's institutions.

## Payment processing, clearing, and settlement

A **[payment processor]({{ '/glossary/' | relative_url }}#payment-processor)** handles the technical work of accepting, checking, and routing a payment — the card reader in Noor's shop and the software behind it are provided by a processor working with the acquirer.

Two steps happen after a payment is authorized but before money truly arrives. **[Clearing]({{ '/glossary/' | relative_url }}#clearing)** is the exchange of payment instructions between institutions and the calculation of what each owes the others; it does not move money by itself. **[Settlement]({{ '/glossary/' | relative_url }}#settlement)** is the actual, final transfer of funds between institutions that fulfills the obligations calculated during clearing.

This is why a card sale can be authorized in seconds on Monday, but the funds may not settle into Noor's account until Wednesday: authorization confirms the transaction can proceed; settlement is when Noor's bank actually receives the money. The [BIS glossary](https://www.bis.org/cpmi/publ/d00b.htm) defines clearing and settlement in more technical detail.

Different types of payments travel over different infrastructure. A **[payment rail]({{ '/glossary/' | relative_url }}#payment-rail)** is the underlying network used to move money for a particular payment type — a card network, a same-day bank-transfer system, or an instant-payment system are all different rails, each with its own timing, cost, and rules.

## Remittances and cross-border payments

A **[remittance]({{ '/glossary/' | relative_url }}#remittance)** is a transfer of money, often sent by a person working in one country to family in another. It is one example of a **[cross-border payment]({{ '/glossary/' | relative_url }}#cross-border-payment)**: a payment sent from a payer in one country to a payee in another, which usually involves converting one currency into another.

Cross-border payments often rely on a **[correspondent bank]({{ '/glossary/' | relative_url }}#correspondent-bank)**: a bank that provides services, such as processing payments, to another bank, often in a different country, so money can move between banking systems that are not directly connected. A **[wire transfer]({{ '/glossary/' | relative_url }}#wire-transfer)** is a direct, typically same-day transfer between banks, commonly used for large or international payments, though not the only way to send money abroad. Dedicated remittance and money-transfer companies offer another route, sometimes faster or cheaper than a bank wire for smaller amounts, with their own fees and timing.

In the United States, sending money abroad through most providers is covered by Regulation E's remittance transfer rules, which require upfront disclosure of fees, the exchange rate, and the amount the recipient should receive, along with a short cancellation window and error-resolution rights. See the [CFPB's Regulation E rules](https://www.consumerfinance.gov/rules-policy/regulations/1005/) and its [guidance on problems sending money to another country](https://www.consumerfinance.gov/consumer-tools/sending-money/). Protections outside the United States depend on local rules.

## Compare the cost of moving money abroad

An **[exchange rate]({{ '/glossary/' | relative_url }}#exchange-rate)** is the price of one currency stated in terms of another. A provider rarely applies the exact market rate; the gap is the **[foreign-exchange margin]({{ '/glossary/' | relative_url }}#foreign-exchange-margin)** — the difference between the rate applied to the customer and the market's reference rate. A margin can cost more than an advertised fee, and a "no fee" transfer is not necessarily the cheapest option.

Suppose Noor sends **$500** to family abroad, and the mid-market reference rate is **1 USD = 0.90 EUR**. Compare two providers:

| Provider | Fee | Rate applied | Amount converted | Recipient receives |
| --- | ---: | ---: | ---: | ---: |
| A | $5 flat fee, no added margin | 0.90 EUR per USD (market rate) | $500 − $5 = $495 | $495 × 0.90 = **€445.50** |
| B | No fee, but a marked-up rate | 0.873 EUR per USD | $500 (full amount) | $500 × 0.873 = **€436.50** |

Provider B advertises no fee, but its rate is **3% below** the market rate: (0.90 − 0.873) ÷ 0.90 = 3%. Despite the fee, Provider A delivers **€445.50 − €436.50 = €9.00 more** to the recipient. Comparing only the headline fee, and ignoring the exchange rate applied, would have favored the more expensive option.

To compare cross-border payment options, check the fee, the exact exchange rate offered against a published market rate, how long the transfer takes, and what happens if it fails or is delayed. Required disclosures — where they apply — should make this comparison possible without independently researching the market rate yourself.

## Fraud prevention, disputes, and payment security

**[Authentication]({{ '/glossary/' | relative_url }}#authentication)** confirms that someone attempting a payment or accessing an account is who they claim to be — a PIN, a card chip, a one-time code, or a fingerprint are all authentication methods. **[Strong customer authentication]({{ '/glossary/' | relative_url }}#strong-customer-authentication)**, required in some jurisdictions for many online payments, combines at least two independent factors, such as something the payer knows (a password) and something they possess (a phone). Requirements differ by country and payment type.

**[Fraud]({{ '/glossary/' | relative_url }}#fraud)** is intentional deception to obtain money or property unlawfully, including using someone else's card or account details without permission. The [FTC's consumer alerts](https://consumer.ftc.gov/consumer-alerts) and the [Investor.gov fraud red-flags checklist](https://www.investor.gov/protect-your-investments/fraud/how-avoid-fraud/red-flags-investment-fraud-checklist) both describe common pressure tactics — urgency, secrecy, and requests to pay by unusual methods — that apply beyond investment fraud to everyday payment scams.

If a customer believes a card charge is wrong or unauthorized, they can raise a **[dispute]({{ '/glossary/' | relative_url }}#dispute)**: a formal challenge that a transaction was unauthorized, incorrect, or for goods or services never received. A successful dispute on a card payment can lead to a **[chargeback]({{ '/glossary/' | relative_url }}#chargeback)**: a reversal, initiated through the card network, that returns funds from the merchant to the cardholder. Suppose a customer disputes a $75 charge at Noor's shop as unauthorized, and the card network rules in the customer's favor: Noor's account is debited $75 and the customer's issuer credits it back, sometimes along with a chargeback fee to the merchant. This is why merchants keep transaction and delivery records — to respond to disputes, not only to make the original sale.

Reporting a lost card, unrecognized transaction, or suspected fraud promptly matters: many protections have time limits, and delays can affect how much of a loss is recoverable. Check the specific rules for the account, card, or provider involved rather than assuming one country's protections apply elsewhere.

## Check your understanding

Try these before reading the answers. Each numerical question is independent and uses the assumptions stated in that question.

1. A card sale of $60 is charged a fee of 2.9% plus a flat $0.30. How much does the merchant actually receive?
2. What is the difference between authorization and settlement?
3. Why might a direct debit come with stronger cancellation rights than a bank transfer the payer initiates themselves?
4. A remittance provider charges no fee but applies an exchange rate 4% below the market reference rate on a $1,000 transfer where the market rate is 1 USD = 0.85 EUR. How many euros does the recipient receive?
5. Using the previous question's numbers, if a competing provider charges a $10 flat fee and applies the exact 0.85 market rate to the remaining amount, which provider delivers more to the recipient?
6. What is the purpose of a correspondent bank in a cross-border payment?
7. What must generally be true for a card chargeback to occur?
8. Does "no fee" advertising guarantee the cheapest way to send money abroad?

### Answers

1. **$57.96.** Fee = ($60 × 0.029) + $0.30 = $1.74 + $0.30 = $2.04. Merchant receives $60 − $2.04 = $57.96.
2. **Authorization approves that a transaction can proceed; settlement is the actual transfer of funds that fulfills the obligation later.** Time can pass between the two.
3. **Because the payee, not the payer, initiates a direct debit.** Rules commonly give the payer advance notice and the right to cancel or reverse a debit, since they did not trigger each individual payment.
4. **€816.00.** The applied rate is 0.85 × (1 − 0.04) = 0.816 EUR per USD. $1,000 × 0.816 = €816.00.
5. **The $10-fee provider.** It converts $990 at 0.85: $990 × 0.85 = €841.50, more than the €816.00 from the marked-up, no-fee provider.
6. **It lets money move between banks that are not directly connected**, often across borders, by providing payment services on another bank's behalf.
7. **A successful dispute of the underlying transaction**, such as a claim that it was unauthorized, incorrect, or undelivered, ruled on through the card network's process.
8. **No.** A marked-up exchange rate can cost more than an explicit fee; comparing the total amount the recipient receives is more reliable than comparing fees alone.

## Terms introduced in this lesson

Follow these definitions to revisit their meaning and return to the explanations above.

{% assign lesson_terms = site.data.glossary | sort: 'term' %}
{% for term in lesson_terms %}{% if page.glossary_terms[term.id] %}
- [{{ term.term }}]({{ '/glossary/' | relative_url }}#{{ term.id }})
{% endif %}{% endfor %}

## Keep learning

Revisit [Banking, credit, and lending]({{ '/knowledge/banking-credit-and-lending/' | relative_url }}) for how the accounts behind these payments work. [Personal finance and financial wellbeing]({{ '/knowledge/personal-finance-and-financial-wellbeing/' | relative_url }}) connects payment timing with budgeting and cash flow.

[Financial technology and open finance]({{ '/knowledge/financial-technology-and-open-finance/' | relative_url }}) and [Blockchain and decentralized finance]({{ '/knowledge/blockchain-and-decentralized-finance/' | relative_url }}) currently list planned topics on newer ways money moves.

### Planned follow-up lessons

- Comparing money-transfer apps, peer-to-peer payments, and their protections
- Reading a remittance disclosure and calculating the true cost of a transfer
- Business payment reconciliation and handling chargebacks
- Payment security practices for small merchants and online sellers
