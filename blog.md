---
layout: default
title: Blog
permalink: /blog/
description: "Read community posts about finance, financial technology, economic developments, and the ideas shaping more accessible financial systems."
seo_title: "Finance and Financial Technology Blog"
---

# Blog

Notes, ideas, and updates from the Open Finance Academy community.

<div class="post-list">
  {% for post in site.posts %}
    <article class="post-preview">
      <p class="post-date">{{ post.date | date: "%B %-d, %Y" }}</p>
      <h2><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h2>
      {{ post.excerpt }}
      <p><a href="{{ post.url | relative_url }}">Read more</a></p>
    </article>
  {% endfor %}
</div>
