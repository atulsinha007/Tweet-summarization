import re
import csv
from operator import itemgetter
from collections import defaultdict
from helper_ import *
from helper import *




def main():
	tweets = loadtext(csv_file)
	# print(tweets)
	# print("-------------------------\n\n")
	tweets = tokenize(tweets)
	

	useful_tweets, non_useful_tweets = content_based_segregation(tweets)

	useful_tweets = list(useful_tweets)
	useful_tweets = segregation(useful_tweets)
	# useful_tweets = abstractive_summary(list(useful_tweets))
	# print(useful_tweets)
	# print(len(useful_tweets))
	list_sent = [' '.join(tup) for tup in useful_tweets]
	# print(list_sent)
	list_final = return_final_list(list_sent)
	summary = merge_for_summary(list_final)
	print(summary)
	

if __name__ == '__main__':
	main()