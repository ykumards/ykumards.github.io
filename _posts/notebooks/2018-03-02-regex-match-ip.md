---
layout: post
title: Match an IP address
description: "How to match an IP address in a text using regex"
category: tech-notes
tags: [python, regex, text]
---
Sometimes we'd need to match IP addresses in a text, probably to extract them or filter them out. I faced this while working on the Kaggle's Toxic Comments challenge, many of the texts end with an IP address. If you're trying extract features like "number of sentences in the comment", these IPs could mess the count. 


```python
import re

text = "And please don't remove the template from the talk page since I'm retired now.89.205.38.27"
ip = re.compile(r'[0-9]+(?:\.[0-9]+){3}')
print(re.sub(ip, ' <IP> ', text))
```

    And please don't remove the template from the talk page since I'm retired now. <IP> 


This code replaces the IP with the tag `<IP>`. The filter is not fool-proof though, it sometimes lets in invalid ip addresses.


```python
adversarial_text = "And please don't remove the template from the talk page since I'm retired now.0.00.999.9999"
print(ip.findall(adversarial_text))
```

    ['0.00.999.9999']


This is not a problem for my use case, but is an issue if we're say, verifying the entry in a form. The regex info webpage has some solutions for this [here](https://www.regular-expressions.info/ip.html).
