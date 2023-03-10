# Variation in usage of punctuation on Twitter

By: Mark den Ouden (s5356865)

## Content
- get_twitter_data.sh (a shellscript that downlaods twitter data from karora.let.rug.nl)
- punctuation_counter.py (a python program that counts the occurences of '?', '!' and '.')
- README.md 

The used Twitter data is not uploaded to GitHub due to it's large size.
The instructions in get_twitter_data.sh get you the same dataset as used in this research. 

## Background information
It is already known that some days are more popular to tweet than other days, M.J. Rust et al. [1] showed that Twitter is used more during (summer) holidays.
But they did not do any research on the content of those tweets. 
There are also differences known between different gender and usage of punctuation [2]. 
This could means the usage of punctuation is not the same for everyone, then why should it be the same everytime?


## Research Question and Hypothesis
RQ: How does the usage of periods, exclamation- and question marks change over the day and over the year?

H: The usage of periods, exclamation-and question marks changes over the day and over the year.
This is because people feel differently during the day and the year. 
During summer people are more enthusiastic and therefore they might use more exclamation marks than during winter. 

## Contingency Matrix
DV's: Frequency of exclamation marks, question marks and periods. 
IV's: Months (jan-dec)

## Methods

Twitter Data: For this research, a collection of dutch Twitter data is used.
It is extracted from the inhouse Twitter corpus of Dutch Tweets from the University of Groningen.
To collect this Twitter data, a .sh file is used. 
All dutch Tweets from every month of 2022 between 13:00 and 14:00 are collected. 

Regular Expressions: To filter the Twitter data, a python module that uses regular expressions is used. 
This module deletes all retweets and links from the data collection and it counts all occurences of periods, exclamation marks and question marks.

# References
[1] Eugene Leypunskiy, Emre K??c??man, Mili Shah, Olivia J. Walch, Andrey Rzhetsky, Aaron R. Dinner, Michael J. Rust,
Geographically Resolved Rhythms in Twitter Use Reveal Social Pressures on Daily Activity Patterns,
Current Biology,Volume 28, Issue 23, 2018, Pages 3763-3775.e5, ISSN 0960-9822, https://doi.org/10.1016/j.cub.2018.10.016.

[2] Waseleski, Carol, Gender and the Use of Exclamation Points in Computer-Mediated Communication: An Analysis of Exclamations Posted to Two Electronic Discussion Lists, Journal of Computer-Mediated Communication, J Comput Mediat Commun, 2017, https://doi.org/10.1111/j.1083-6101.2006.00305.x