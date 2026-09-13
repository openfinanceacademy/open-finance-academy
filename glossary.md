---
layout: default
title: Glossary
permalink: /glossary/
---

# Glossary

Plain-language definitions of the terms introduced in our knowledge library. Follow a reference to see a term explained with examples.

The glossary grows as we publish lessons. [Explore the knowledge areas]({{ '/knowledge/' | relative_url }}).

{% assign terms = site.data.glossary | sort: 'term' %}
{% assign reference_pages = site.pages | sort: 'title' %}

## Find a term

{% for term in terms %}
- [{{ term.term }}](#{{ term.id }})
{% endfor %}

{% for term in terms %}
## {{ term.term }}
{: #{{ term.id }} }

{{ term.definition }}

**In the knowledge library:**

{% for reference in reference_pages %}{% assign section = reference.glossary_terms[term.id] %}{% if section %}
- [{{ reference.title }} — {{ section | replace: '-', ' ' }}]({{ reference.url | relative_url }}#{{ section }})
{% endif %}{% endfor %}
{% endfor %}
