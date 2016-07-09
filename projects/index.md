---
layout: page
title: Projects
excerpt: "List of projects I've worked on."
search_omit: true
---

<ul class="post-list">
{% for post in site.categories.projects %} 
  <li><article><a href="{{ site.url }}{{ post.url }}">{{ post.title }} <span class="entry-date"><time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}</time></span></a></article></li>
{% endfor %}
</ul>
