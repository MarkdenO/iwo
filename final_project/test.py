# !/bin/python3
import sys
import re
from collections import Counter


def filter_retweets(corpus):
    """This function removes retweets from the corpus"""
    corpus_without_retweets = []
    for tweet in corpus[:10]: 
        if tweet[0:2] != 'RT': 
            corpus_without_retweets.append(tweet)
    return corpus_without_retweets


def filter_links(corpus): 
    """This function removes any link in the tweet and replaces it with an empty string."""
    new_corpus = []
    links_re = re.compile('https:[A-Za-z/\.].*')
    for line in corpus:
        new_corpus.append(links_re.sub('', line))
    return new_corpus
    
    
def count_interpunction(corpus):
    """Counts the amount of interpunction marks used per tweet"""
    interpunction = ('.', ',', '/', '!', '?', '\'', '\"', '(', ')', ';', ':', '-')
    counted_interpunction = Counter()
    for tweet in corpus:
        for character in tweet:
            if character in interpunction:
                counted_interpunction[character] += 1
    return counted_interpunction                        


def main(): 
    infile = open(sys.argv[1], 'r', encoding='utf8')
    corpus = infile.readlines()
    infile.close()
    
    print(corpus[:10])
    
    corpus_without_retweets = filter_retweets(corpus)
    print("\n\n New corpus: \n", corpus_without_retweets)
    
    corpus_without_links = filter_links(corpus)
    num_of_interpunction = count_interpunction(corpus_without_links)
    print(num_of_interpunction)
    
if __name__ == "__main__":
    main()