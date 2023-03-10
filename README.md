# Variation in usage of punctuation on Twitter

By: Mark den Ouden (s5356865)

## Content
- get_twitter_data.sh (a shellscript that downlaods twitter data from karora.let.rug.nl)
- punctuation_counter.py
- README.md

## Background information
It is already known that some days are more popular to tweet than other days, M.J. Rust et al. [1] showed that Twitter is used more during (summer) holidays.
But they did not do any research on the content of those tweets. 


## Research Question and Hypothesis
RQ: How does the usage of periods, exclamation- and question marks change over the day and over the year?

H: The usage of periods, exclamation-and question marks changes over the day and over the year.
This is because people feel differently during the day and the year. 
During summer people are more enthusiastic and therefore they might use more exclamation marks than during winter. 

## Methods

Twitter Data: For this research, a collection of dutch Twitter data is used.
It is extracted from the inhouse Twitter corpus of Dutch Tweets from the University of Groningen.
To collect this Twitter data, a .sh file is used. 

Regular Expressions: To filter the Twitter data, a python module that uses regular expressions is used. 
This module deletes all retweets and links from the data collection and it counts all occurences of periods, exclamation marks and question marks.

# References
Geographically Resolved Rhythms in Twitter Use Reveal Social Pressures on Daily Activity Patterns
