#!/bin/bash
# Name: get_data.sh
# Author: Mark den Ouden
# Date: 08-03-2023
# This file collects data from the Dutch Twitter Corpus from karora

# Login to karora
read -p "Please enter your student ID: " userID
ssh $userID@karora.let.rug.nl

# Collect all tweets from march 2019
zless /net/corpora/twitter2/Tweets/2019/03/201903??.out.gz | /net/corpora/twitter2/tools/tweet2tab text >> tweets_201903_13.txt

# Copy found corpus from karora to your own computer
scp s5356865@karora.let.rug.nl:tweets_201903_13.txt .