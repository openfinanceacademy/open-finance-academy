---
layout: default
title: Financial technology and open finance
permalink: /knowledge/financial-technology-and-open-finance/
glossary_terms:
  open-finance: what-open-finance-means
  open-banking: open-banking-and-data-portability
  data-portability: open-banking-and-data-portability
  consent: open-banking-and-data-portability
  api: apis-and-financial-data-standards
  data-standard: apis-and-financial-data-standards
  interoperability: apis-and-financial-data-standards
  sandbox: apis-and-financial-data-standards
  data-aggregator: data-aggregators-screen-scraping-and-standardized-access
  screen-scraping: data-aggregators-screen-scraping-and-standardized-access
  digital-identity: digital-identity-and-authentication
  credential: digital-identity-and-authentication
  authentication: digital-identity-and-authentication
  strong-customer-authentication: digital-identity-and-authentication
  cybersecurity: cybersecurity-basics-for-financial-apps
  encryption: cybersecurity-basics-for-financial-apps
  data-breach: cybersecurity-basics-for-financial-apps
  robo-advisor: financial-applications-automation-and-responsible-ai
  algorithm: financial-applications-automation-and-responsible-ai
  automation: financial-applications-automation-and-responsible-ai
  algorithmic-transparency: financial-applications-automation-and-responsible-ai
  generative-ai: financial-applications-automation-and-responsible-ai
  model-risk: financial-applications-automation-and-responsible-ai
description: "Learn how open banking, financial APIs, account connections, and automated tools work, including consent, privacy, security, and practical tradeoffs."
---

# Financial technology and open finance

Learn how apps connect to your accounts, what "open banking" and "open finance" actually mean, how to weigh convenience against privacy and security, and what automated financial tools can and cannot do for you.

[← All knowledge areas]({{ '/knowledge/' | relative_url }}) · [Glossary]({{ '/glossary/' | relative_url }})

No technical background is needed. [Banking, credit, and lending]({{ '/knowledge/banking-credit-and-lending/' | relative_url }}) and [Financial law, ethics, and consumer protection]({{ '/knowledge/financial-law-ethics-and-consumer-protection/' | relative_url }}) are useful companions, since data sharing and account access sit alongside privacy and consumer-protection questions. New finance terms are **bold**, explained on first use, and linked to the glossary, which links back to each explanation.

### Example assumptions

The dollar amounts and fee comparisons are invented teaching examples, not current pricing from any specific provider. Descriptions of particular apps, banks, or products are illustrative, not endorsements or warnings about any real company.

Rules on data sharing, consent, and required security measures vary significantly by country. U.S.-specific examples are labeled and use official sources checked September 14, 2026. Numbered references are listed at the end of the page.

## In this lesson

1. [What "open finance" means](#what-open-finance-means)
2. [Open banking and data portability](#open-banking-and-data-portability)
3. [APIs and financial data standards](#apis-and-financial-data-standards)
4. [Data aggregators, screen scraping, and standardized access](#data-aggregators-screen-scraping-and-standardized-access)
5. [Digital identity and authentication](#digital-identity-and-authentication)
6. [Cybersecurity basics for financial apps](#cybersecurity-basics-for-financial-apps)
7. [Financial applications, automation, and responsible AI](#financial-applications-automation-and-responsible-ai)
8. [AI-assisted financial-services workflows](#ai-assisted-financial-services-workflows)
9. [Check your understanding](#check-your-understanding)

## What "open finance" means

Priya uses a budgeting app that pulls in transactions from her checking account, a savings account at a different bank, and her retirement account, so she can see everything in one place instead of four separate logins.

**[Open finance]({{ '/glossary/' | relative_url }}#open-finance)** describes a broader set of arrangements that let a customer authorize third-party providers to access a wide range of their financial data — not only bank accounts, but potentially savings, investments, pensions, or insurance — and, in some cases, to initiate payments on the customer's behalf. **Open banking** is the narrower, more established version of this idea, focused specifically on bank account data and payments. Neither term describes a single global system: what is technically possible, legally required, and actually offered to customers differs by country and provider.[^1]

The core shift these terms describe is this: financial data that used to be locked inside one institution's own website or app can now, with the customer's authorization, be shared with other companies that build services on top of it.

## Open banking and data portability

**[Open banking]({{ '/glossary/' | relative_url }}#open-banking)** lets a customer authorize a third-party provider — like Priya's budgeting app — to view account information or initiate a payment directly from their bank account, instead of only using the bank's own app. **[Data portability]({{ '/glossary/' | relative_url }}#data-portability)** is the related idea that customers should be able to move their own data from one provider to another in a usable format, rather than being locked in because switching means losing your transaction history.

Access is not automatic. **[Consent]({{ '/glossary/' | relative_url }}#consent)** — a freely given, specific, and informed agreement to a particular use of data — is what authorizes a third party to connect. A well-designed consent flow tells you what data is being requested, for what purpose, for how long, and how to revoke access later. Granting an app access to view balances is a different decision from granting it the ability to move money, and a clear consent screen should distinguish the two.

**United States example:** In October 2024 the Consumer Financial Protection Bureau finalized its Personal Financial Data Rights rule (12 CFR Part 1033), which would require covered banks, credit unions, and other providers to make certain consumer financial data available, on request, to the consumer and to third parties they authorize, subject to privacy and security safeguards. The rule's status is not settled: in August 2025 the CFPB opened a new rulemaking to reconsider it, and the original rule has been challenged in court, so its requirements and compliance dates may change.[^2] Other countries have their own frameworks, with different scopes, timelines, and consumer rights; do not assume a right established in one country applies in another.

## APIs and financial data standards

Behind the scenes, Priya's budgeting app does not log into her bank's website the way she does. Instead, it connects through an **[API]({{ '/glossary/' | relative_url }}#api)** — an application programming interface, a defined way for one piece of software to request data or actions from another. The bank publishes rules for exactly what an authorized app can ask for and what response it will get back, rather than exposing its entire internal systems.

An API is far more useful when many institutions describe the same kind of data the same way. A **[data standard]({{ '/glossary/' | relative_url }}#data-standard)** is a published, shared specification for how financial data should be formatted, so that "account balance" or "transaction date" means the same structured thing across different banks and apps. **[Interoperability]({{ '/glossary/' | relative_url }}#interoperability)** is the resulting ability of different systems to exchange and use that data, or work together, without custom, one-off integration for every single pair of institutions.

Before a new API or data-sharing feature reaches every customer, a provider may test it in a **[sandbox]({{ '/glossary/' | relative_url }}#sandbox)**: a controlled testing environment, sometimes provided by a regulator, that lets new financial technology be tried out with limits — such as fake data or capped transaction sizes — before a wider launch. A sandbox reduces the risk of testing new features directly against real customer money and data.[^3]

## Data aggregators, screen scraping, and standardized access

Not every app that shows "all your accounts in one place" connects the same way. A **[data aggregator]({{ '/glossary/' | relative_url }}#data-aggregator)** is a service that collects account information from multiple financial institutions so it can be displayed together, and it can do this through standardized APIs or through older methods.

**[Screen scraping]({{ '/glossary/' | relative_url }}#screen-scraping)** is one such older method: the app automates the same login and web pages a customer would use themselves, rather than using a dedicated API. This often means giving the app your actual bank username and password, which it stores and reuses to log in on your behalf. This differs meaningfully from an API-based connection, where the bank issues the third party a limited, revocable form of access without ever handing over your login credentials.[^4]

| Access method | What is shared | What you can revoke |
| --- | --- | --- |
| API-based (open banking) | A scoped data or payment permission, granted through consent | The specific authorization, typically from the bank or an app-permissions screen, without changing your password |
| Screen scraping | Your actual login credentials, stored by the third party | Revoking access may require changing your bank password, since the third party held the original one |

Before connecting an account to any app, check which method it uses, what specifically it can see or do, and how to disconnect it later. A polished-looking app is not proof that it uses the safer method.

## Digital identity and authentication

Connecting these accounts still requires proving who you are. A **[digital identity]({{ '/glossary/' | relative_url }}#digital-identity)** is the set of electronic attributes and credentials used to verify a person online — it might combine an account username, a device, and a verified phone number. A **[credential]({{ '/glossary/' | relative_url }}#credential)** is any piece of information, such as a password, one-time code, or security key, used to prove identity or authorize access.

**[Authentication]({{ '/glossary/' | relative_url }}#authentication)** is the process of confirming that someone attempting a payment or accessing an account is who they claim to be. **[Strong customer authentication]({{ '/glossary/' | relative_url }}#strong-customer-authentication)**, required in some jurisdictions for many online payments — for example under the European Union's payment-services rules — combines at least two independent factors — something you know, like a password, and something you have, like a phone that receives a code.[^5] Requiring two independent factors means a stolen password alone is not enough to authenticate; an attacker would also need the second factor.

A well-designed connection to a third-party app should authenticate you directly with your bank or account provider — often redirecting you to your bank's own login screen — rather than asking you to type your bank password into the third-party app itself. If an app asks for your bank password directly, that is a sign it may be using screen scraping rather than a standardized, revocable API connection.

## Cybersecurity basics for financial apps

**[Cybersecurity]({{ '/glossary/' | relative_url }}#cybersecurity)** covers the practices and technology used to protect systems, networks, and data from unauthorized access, disruption, or damage. For an individual user, most of this happens behind the scenes, but a few concepts are useful to recognize.

**[Encryption]({{ '/glossary/' | relative_url }}#encryption)** scrambles data using a mathematical method so that only someone with the correct key can read it — it protects information both while it travels between your device and a server, and while it is stored. A **[data breach]({{ '/glossary/' | relative_url }}#data-breach)** is an incident where protected or sensitive data is accessed, disclosed, or used without authorization; encryption reduces, but does not eliminate, the harm a breach can cause, since a breach can still expose account numbers, names, or other details even if certain fields were encrypted.

The NIST Cybersecurity Framework is a widely referenced, voluntary framework that organizations use to structure how they identify, protect against, detect, respond to, and recover from cybersecurity risks; it is a reference for how institutions organize their defenses, not a guarantee that any specific provider has implemented it well.[^6] As a user, reasonable practices include using a unique password for financial accounts, enabling any available strong authentication, and promptly revoking access for apps you no longer use — an old, forgotten connection is still a live way into your data until you remove it.

## Financial applications, automation, and responsible AI

**[Automation]({{ '/glossary/' | relative_url }}#automation)** uses technology to perform a task with reduced or no ongoing human action, following predefined rules or triggers — an automatic transfer into savings on payday is a simple example. An **[algorithm]({{ '/glossary/' | relative_url }}#algorithm)** is the defined set of steps or rules a computer follows to perform a task, such as flagging a possibly fraudulent transaction or selecting investments for a portfolio.

A **[robo-advisor]({{ '/glossary/' | relative_url }}#robo-advisor)** is an automated service that builds or manages an investment portfolio using an algorithm, typically based on answers to a questionnaire about goals and risk tolerance, usually with limited or no ongoing human advisor involvement. This can lower costs compared with a traditional advisory relationship, but it also means fewer opportunities for a human to ask about circumstances the questionnaire did not anticipate.[^7]

Suppose Priya compares a robo-advisor charging a **0.25%** annual management fee against a traditional advisor charging **1%**, both managing a **$20,000** portfolio for a year, with no other differences assumed:

- Robo-advisor fee: $20,000 × 0.0025 = **$50**.
- Traditional advisor fee: $20,000 × 0.01 = **$200**.
- Difference: $200 − $50 = **$150** lower cost with the robo-advisor in this example.

A lower fee does not by itself mean the robo-advisor's recommended portfolio is better suited to Priya's actual goals; compare what each service actually does, not only its price. Review the [Investing and portfolio management lesson]({{ '/knowledge/investing-and-portfolio-management/' | relative_url }}) for how to evaluate a fund strategy independent of who or what selected it.

**[Algorithmic transparency]({{ '/glossary/' | relative_url }}#algorithmic-transparency)** is the degree to which the factors, data, and logic behind an automated decision can be explained or examined — this matters most when an algorithm affects access to money or credit, such as an automated loan denial or a fraud flag that freezes an account. Ask whether a decision can be explained in plain terms and whether there is a way to have it reviewed by a person; "the algorithm decided" is not, by itself, an adequate answer to why a specific decision was made.

## AI-assisted financial-services workflows

**[Generative AI]({{ '/glossary/' | relative_url }}#generative-ai)** is technology that produces new text, code, tables, or other content from patterns learned from data and instructions. In financial work, it can help draft a research note, inspect a spreadsheet, summarize a filing, or route an exception. The output can sound confident while still containing an invented fact, a missed footnote, or a calculation error.

The Claude for Financial Services repository is an example of this kind of software. It provides reference agents, skills, and connectors for professional workflows such as valuation, earnings analysis, reconciliation, and KYC screening. It is not a bank connection, investment product, or source of authoritative financial data. Some connectors require separate subscriptions or API keys, and the repository's managed-agent delegation features are identified as a research preview.[^8]

For a workflow that handles financial data, ask four questions before trusting the result:

1. **What data can it access?** Limit connectors and credentials to the records the task needs. A connector to a research service or internal drive may expose more information than the final report requires.
2. **Can each claim be traced?** Require the source document, date, and location for figures and conclusions. A link to a tool or model is not evidence for a particular number.
3. **What must a person verify?** Recalculate material figures, check formulas and units, inspect exceptions, and confirm the result against primary records. Treat this as **[model risk]({{ '/glossary/' | relative_url }}#model-risk)** — the possibility that a model's design, data, implementation, or use produces an unreliable outcome.
4. **What happens when it is wrong?** Keep an audit trail, provide a way to correct or escalate the output, and do not let an assistant alone approve onboarding, move money, post accounting entries, or make a binding investment decision.

These controls extend the earlier advice on **[cybersecurity]({{ '/glossary/' | relative_url }}#cybersecurity)**, **[data breaches]({{ '/glossary/' | relative_url }}#data-breach)**, and **[algorithmic transparency]({{ '/glossary/' | relative_url }}#algorithmic-transparency)**. The NIST AI Risk Management Framework is a useful organizational reference, but using a framework does not prove that a particular tool is safe or accurate.[^9]

## Check your understanding

Try these before reading the answers. Each numerical question is independent and uses the assumptions stated in that question.

1. What is the key difference between "open banking" and the broader term "open finance"?
2. An app asks you to type your actual bank username and password directly into its own login screen, rather than redirecting you to your bank's site. What access method does this suggest, and why does it matter?
3. Why does strong customer authentication typically require two different types of factors rather than two of the same type?
4. A robo-advisor charges a 0.40% annual fee and a traditional advisor charges 1.1%, both on a $15,000 portfolio for one year. What is the dollar difference in fees?
5. Does encryption make a data breach harmless?
6. Why might a shared data standard matter more as more banks and apps try to connect to each other, rather than for a single pair of institutions?
7. A loan application is declined by an automated system with no further explanation offered. What does algorithmic transparency suggest you should be able to ask for?
8. A financial-services AI assistant produces a polished valuation memo. What evidence should you request before relying on its figures?
9. Why should an AI assistant that flags a KYC issue route the case for review rather than approve or decline the customer by itself?

### Answers

1. **Open banking is the narrower, established version focused on bank accounts and payments; open finance extends the same idea to a wider range of financial data**, such as investments, pensions, or insurance, where such access exists.
2. **This suggests screen scraping rather than a standardized API connection.** It matters because the app now holds your actual bank credentials, rather than a limited, separately revocable permission, which usually means changing your bank password to fully cut off access later.
3. **Because relying on two factors of the same type doesn't add much protection if one method of attack can compromise both at once** — for example, two things you "know" could both be guessed or leaked in the same data breach, while something you know and something you separately possess are harder to obtain together.
4. **$105.** Robo-advisor fee: $15,000 × 0.004 = $60. Traditional advisor fee: $15,000 × 0.011 = $165. Difference: $165 − $60 = $105.
5. **No.** Encryption reduces what an attacker can read, but a breach can still expose unencrypted fields, metadata, or other details, and encrypted data can sometimes still be misused or later decrypted.
6. **Because without a shared standard, each new connection between a bank and an app may require custom, one-off work,** while a shared standard lets any compliant bank and any compliant app interoperate without building a separate integration for every pair.
7. **A plain-language explanation of the factors behind the decision, and a way to have the decision reviewed**, rather than only being told that an algorithm made the call.
8. **Traceable source documents and dates for each material claim, plus a check of the calculations, formulas, units, assumptions, and exceptions against primary records.** A confident-sounding draft is not evidence of accuracy.
9. **Because the result can be wrong or incomplete and the decision may carry legal or consumer consequences.** The assistant can organize evidence and apply a stated rules grid, but an authorized reviewer should resolve uncertainty and make the final decision.

## Terms introduced in this lesson

Follow these definitions to revisit their meaning and return to the explanations above.

{% assign lesson_terms = site.data.glossary | sort: 'term' %}
{% for term in lesson_terms %}{% if page.glossary_terms[term.id] %}
- [{{ term.term }}]({{ '/glossary/' | relative_url }}#{{ term.id }})
{% endif %}{% endfor %}

## Keep learning

Revisit [Financial law, ethics, and consumer protection]({{ '/knowledge/financial-law-ethics-and-consumer-protection/' | relative_url }}) for privacy rights, consent, and how to raise a data or security problem. [Payments and money movement]({{ '/knowledge/payments-and-money-movement/' | relative_url }}) covers how the underlying transfers and card payments this technology relies on actually move money.

[Blockchain and decentralized finance]({{ '/knowledge/blockchain-and-decentralized-finance/' | relative_url }}) currently lists planned topics on a different approach to moving and recording value.

### Planned follow-up lessons

- Reading an app's data-sharing permissions and revoking access safely
- Comparing regulatory approaches to open banking across countries
- Evaluating a robo-advisor's disclosures and underlying fund choices
- Recognizing account-takeover attempts and securing a compromised login

## References

[^1]: Financial Conduct Authority, "Call for Input: Open Finance" — <https://www.fca.org.uk/publications/calls-input/call-input-open-finance>
[^2]: Consumer Financial Protection Bureau, "Personal Financial Data Rights" — <https://www.consumerfinance.gov/personal-financial-data-rights/>
[^3]: Financial Conduct Authority, "Regulatory Sandbox" — <https://www.fca.org.uk/firms/innovation/regulatory-sandbox>
[^4]: Federal Reserve Bank of Kansas City, "Data Aggregators: The Connective Tissue for Open Banking" — <https://www.kansascityfed.org/research/payments-system-research-briefings/data-aggregators-the-connective-tissue-for-open-banking/>
[^5]: Commission Delegated Regulation (EU) 2018/389, "Regulatory technical standards for strong customer authentication" — <https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32018R0389>
[^6]: National Institute of Standards and Technology, "Cybersecurity Framework" — <https://www.nist.gov/cyberframework>
[^7]: U.S. Securities and Exchange Commission, Division of Investment Management, "IM Guidance Update 2017-02: Robo-Advisers" — <https://www.sec.gov/investment/im-guidance-2017-02.pdf>
[^8]: Anthropic, "Claude for Financial Services" repository — <https://github.com/anthropics/financial-services>
[^9]: National Institute of Standards and Technology, "AI Risk Management Framework" — <https://www.nist.gov/itl/ai-risk-management-framework>
