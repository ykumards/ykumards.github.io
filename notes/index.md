---
layout: page
title: Random Ramblings
excerpt: "Collection of notes which are too short to be a blog post."
search_omit: true
---

<ul class="post-list">
{% for post in site.categories.notes %} 
  <li>
  	<article>
  		<a href="{{ site.url }}{{ post.url }}"> 
  			<span class="entry-date">
  				<time datetime="{{ post.date | date_to_xmlschema }}">{{ post.date | date: "%B %d, %Y" }}
  				</time>
  			</span>
  			{{ post.title }}
  		</a>
  	</article>
  </li>
{% endfor %}
</ul>
