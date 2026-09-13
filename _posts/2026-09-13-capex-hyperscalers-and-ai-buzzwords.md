---
layout: default
title: "CAPEX, Hyperscalers, and the Buzzwords Behind the AI Spending Boom"
date: 2026-09-13
permalink: /blog/capex-hyperscalers-and-ai-buzzwords/
description: "A plain-language guide to AI infrastructure spending, from capital expenditures and cloud giants to inference costs and free cash flow."
---

Read a technology earnings headline today and you might encounter something like this: *Hyperscalers are increasing CAPEX to meet inference demand, despite pressure on free cash flow.* In ordinary language: giant technology companies are buying more computing infrastructure to run AI, leaving less cash after those purchases. The vocabulary sounds complicated. The underlying question is familiar: will an expensive purchase earn enough to justify its cost?

You do not need an accounting or technology background to follow the story. Start with a bakery.

## CAPEX: buying the oven

**CAPEX**, short for **capital expenditures**, means spending to buy, build, or improve assets that a business expects to use over multiple years. For a bakery, that could be a new oven. For a technology company, it could be servers, networking equipment, or a data center: a facility housing computers and the power and cooling systems that keep them running.

**OPEX**, short for **operating expenses**, covers the costs of running the business. Flour, electricity, and staff wages keep the bakery working. Electricity, maintenance, and many staffing costs keep a data center working. Precise accounting treatment depends on what a cost relates to; for example, some construction labor becomes part of an asset's cost.

The financial statements record these purchases differently. A long-lived equipment purchase generally starts as an asset on the **balance sheet**, which reports what a business owns and owes. **Depreciation** then allocates its cost over its estimated useful life as an expense. The cash payment and the expense can therefore happen on different schedules. The [SEC's guide to financial statements](https://www.sec.gov/about/reports-publications/investorpubsbegfinstmtguide) explains how assets, expenses, depreciation, and cash movements fit together.

That timing difference is central to the AI spending debate.

## How a profitable business can still spend more cash than it generates

Imagine a small computing business buys **$12 million of servers**, paid entirely in cash at the start of the year. These are invented teaching figures. Assume the servers enter service immediately, last four years, and have no resale value. Ignore taxes, borrowing, leases, other assets, and delays between billing and payment. All customer revenue is collected, and all running costs are paid, during the year.

| Item | Calculation | First-year amount |
| --- | --- | --- |
| Customer revenue | Cash collected from customers | $10 million |
| Running costs | Electricity, staff, and other operating payments | $6 million |
| Operating cash flow | $10 million − $6 million | $4 million |
| Annual depreciation | $12 million ÷ 4 years | $3 million |
| Operating profit | $10 million − $6 million − $3 million | $1 million |
| Cash left after server purchases | $4 million − $12 million | **−$8 million** |

The business reports a $1 million operating profit, but it needs $8 million from existing cash or new financing to cover the year's cash shortfall.

**Operating cash flow** is cash generated or used by the business's operating activities. **Free cash flow**, often abbreviated **FCF**, commonly means operating cash flow minus cash capital expenditures. Companies can define this measure differently, so check their calculation; it is not a standardized accounting subtotal. For an example of a disclosed definition, see [HubSpot's annual report](https://www.sec.gov/Archives/edgar/data/1448056/000119312523181414/d460451dars.pdf).

Negative free cash flow during construction does not, by itself, establish that an investment is bad. The business buys capacity now and hopes to earn from it later. The question is whether future cash generation will cover that purchase, future replacement equipment, and an adequate return for the people financing it.

Useful-life estimates matter too. Under the same simplified assumptions, spreading the $12 million over six years would mean $2 million of annual depreciation and $2 million of operating profit. The original cash payment would still be $12 million. A longer accounting life improves reported annual profit without making the equipment cheaper.

## Hyperscalers: the companies buying ovens by the warehouse

**Hyperscalers** operate enormous computing systems designed to expand as demand grows. Amazon Web Services (AWS), Microsoft Azure, and Google Cloud are familiar examples. Their **cloud** services let customers rent computing, storage, and other capabilities over a network rather than own all the equipment themselves. [IBM's explanation of hyperscale](https://www.ibm.com/think/topics/hyperscale) describes this approach and the major providers.

Financial commentary sometimes uses the label more broadly to include companies such as Meta, which runs enormous infrastructure for its own services. There is no single universal basket of “hyperscaler stocks.” When a headline adds up their spending, check which companies it includes.

The business models also differ. A cloud provider can sell computing capacity to another company. An advertising platform can use computing internally to improve recommendations or advertising. Both may buy AI servers, but the path from hardware to revenue is different.

And one company's CAPEX can become another company's sales: the infrastructure buyer pays an equipment supplier. Those are two views of the same transaction, so adding both figures together would overstate spending by final customers.

## Why the CAPEX headlines need footnotes

For a concrete example, Microsoft reported **$31.9 billion of capital expenditures in its fiscal third quarter of 2026**, the quarter ended March 31. Its earnings discussion also explained that finance leases affect the timing of reported capital expenditures. A **finance lease** is an arrangement accounted for in a way similar to financing an asset purchase: the asset and an obligation are recorded, while payments occur over time. Microsoft's CAPEX measure can therefore include equipment whose full cost was not paid in cash that quarter. [Source: Microsoft's FY2026 third-quarter earnings call](https://www.microsoft.com/en-us/investor/events/fy-2026/earnings-fy-2026-q3).

Before comparing two headline numbers, check:

- **The period:** one quarter, a calendar year, or a company's fiscal year?
- **The status:** spending already incurred or management's forecast, often called **guidance**?
- **The definition:** cash purchases only, or a measure including finance leases?
- **The scope:** all infrastructure, or an explicitly identified AI portion?

Higher spending also creates later expenses. In its fourth-quarter 2025 earnings discussion, Alphabet reported that annual depreciation rose from $15.3 billion in 2024 to $21.1 billion in 2025, and warned that infrastructure investment would increase depreciation and operating costs such as energy. Those are historical figures illustrating the mechanism, rather than a current spending forecast. [Source: Alphabet's Q4 2025 earnings call](https://abc.xyz/investor/events/event-details/2026/2025-Q4-Earnings-Call-2026-Dr_C033hS6/default.aspx).

## Compute, GPUs, training, and inference

**Compute** means computing resources used to do work. In an AI discussion, that usually involves processors, memory, and connected machines. A **GPU**, or graphics processing unit, is a processor well suited to doing many calculations in parallel. GPUs are widely used for AI, alongside other chips designed for particular workloads. [IBM Research describes how GPUs and storage support AI inference](https://research.ibm.com/blog/accelerating-ai-inference-with-ibm-storage-scale).

Two activities explain much of the demand:

- **Training** adjusts an AI model's internal parameters using data so it can learn patterns.
- **Inference** runs a trained model on new input: answering a question, generating an image, or making a prediction.

Training requires resources to develop the model; inference requires resources each time people use it. A popular service can therefore carry a large ongoing computing bill after training is finished. [IBM's guide to AI inference](https://www.ibm.com/think/topics/ai-inference) explains the distinction.

For text models, a **token** is a unit of text, such as a word or part of a word. Tokens are commonly used to measure usage and set prices. **Cost per token** is one way to discuss serving efficiency, but a cheaper token does not necessarily mean a cheaper completed task: a system might use more tokens or attempt more steps. Speed and the amount of work a system can handle also affect serving economics. [Source: IBM's guide to large language model inference](https://www.ibm.com/think/topics/llm-inference).

## The next layer of buzzwords

Once the equipment is installed, attention shifts to how much work it does and who pays for that work.

| Term | Plain-language meaning | The financial question |
| --- | --- | --- |
| **Utilization** | How much available capacity is actually being used. | Are expensive machines serving paying demand or sitting idle? |
| **Monetization** | Turning a product or capability into revenue. | Does usage produce additional sales, or is it included in an existing subscription? |
| **Unit economics** | Revenue and costs for one defined unit, such as a completed task. | What remains after serving that task, and which costs have been counted? |
| **ROI: return on investment** | A comparison of an investment's benefit with its cost. | Over what period, with which costs, and based on measured results or forecasts? |

Consider another invented example. A service charges $1 per completed task and incurs $0.40 in direct serving costs. It has $0.60 left to cover everything else. If competition pushes the price down to $0.50 while serving costs fall to $0.25, that amount drops to $0.25. Better technical efficiency can coexist with worse economics per sale.

**Agentic AI** adds another wrinkle. This describes systems that can take multiple steps and use tools to pursue a task, rather than just return a single answer. That can create useful automation, but the economic unit worth measuring may be a *successfully completed job*, including retries and human review. [IBM Research's discussion of monitoring AI agents](https://research.ibm.com/blog/ibm-agentops-ai-agents-observability) explains why tracking their actual behavior matters.

## Power is part of the business model

An installed server needs electricity, cooling, and a working grid connection before it can produce useful output. The International Energy Agency highlights grid constraints and the geographic concentration of data-center demand in its [Energy and AI report](https://www.iea.org/reports/energy-and-ai/executive-summary).

Headlines often describe projects in **megawatts (MW)** or **gigawatts (GW)**, units of power; one gigawatt equals 1,000 megawatts. These describe a rate of energy use or power capacity. **Megawatt-hours (MWh)** measure energy over time. A facility drawing a constant 100 MW for 24 hours would consume 2,400 MWh.

An announced one-gigawatt project is therefore not evidence that one gigawatt of computing infrastructure is already operating. Read for construction milestones, available grid power, and when customers can actually use the capacity.

## Read the next headline as a business question

When someone says “hyperscaler CAPEX is accelerating,” follow the money: who is buying, what are they buying, when do they pay, and how will the equipment earn its keep?

The optimistic case is that demand fills the new capacity and customers pay enough to cover both running costs and investment. The skeptical case is that construction outruns demand, prices fall, or equipment needs replacement before it earns an adequate return. Neither outcome follows automatically from a bigger spending announcement.

The vocabulary becomes useful when it helps you connect a purchase today with the cash it may generate tomorrow. An impressive server count is the beginning of that investigation.

Continue with [money and financial fundamentals]({{ '/knowledge/money-and-financial-fundamentals/' | relative_url }}) for the basics of money, or browse the [Open Finance Academy blog]({{ '/blog/' | relative_url }}) for more explainers.
