#helper.py
from tfidf import *
import numpy as np 
import pandas as pd 
import nltk
# import inspect
# from textacy.vsm import Vectorizer
# # import textacy.vsm
# from nltk.tokenize import TweetTokenizer
# from scipy.spatial.distance import cosine
# from tqdm import *
import re
import os
# import kenlm
import math
from nltk.util import bigrams
# from pymprog import *
predefined_threshold = 0.5
n_content_words = 1
content_words = ['kerala', 'flood', 'injured', 'dead', 
				'missing', 'live', 'infrastructure', 
				'collapse', 'livestock', 'building', 
				'casuality', 'food', 'keralaflood', 'died',
				'destroyed', 'death', 'deaths', 'damaged', 'hundreds', 
				'thousands', 'bridges', 'keralaflood']

# content_words = ['ranveer', 'deepika', 'deepveer', 'congrats', 'congratuations', 'India', 'singh', 'padukone', 'husband', 'wife', 'couple']

def isNum(s):
	try:
		int(s)
		float(s) # for int, long, float and complex
	except ValueError:
		return False

	return True

csv_file = "tweets.txt"
# csv_file = 'test.txt'
def loadtext(fileo):
	if '.csv' in fileo:
		csv_file = fileo
		file = open(csv_file)
		reader = csv.reader(file, delimiter=",")
		lis_of_tweets = []
		reg_exp_1 = r'RT @.*?[:]'
		reg_exp_2 = r'http://.*'
		reg_exp_3 = r'[#@]'

		for row in reader:
			pq = re.sub(reg_exp_1, "", row[-1])
			pq = re.sub(reg_exp_2, "", pq)
			pq = re.sub(reg_exp_3, "", pq)
			if pq:
				lis_of_tweets.append(pq.rstrip().lstrip())
	elif '.txt' in fileo:
		txt_file = fileo
		file = open(txt_file)
		st = file.read()
		liso = st.split("\n\n")

		lis_of_tweets = []
		reg_exp_1 = r'RT @.*?[:]'
		reg_exp_2 = r'http://.*'
		reg_exp_3 = r'[#@]'

		for st in liso:
			st = re.sub(reg_exp_1, "", st)
			st = re.sub(reg_exp_2, "", st)
			st = re.sub(reg_exp_3, "", st)
			if st.rstrip().lstrip():
				lis_of_tweets.append(st.rstrip().lstrip())
	return lis_of_tweets
# print(read_csv_to_list(csv_file)[:5])


def tokenize(tweets):
	total_tweets = []
	for tweet in tweets:
		total_tweets.append(tweet.split(" "))
	return total_tweets


def content_based_segregation(tweets):
	useful_tweets = set()
	non_useful_tweets = set()
	for tweet in tweets:
		flag = False
		for token in tweet:
			if isNum(token):
				useful_tweets.add(tuple(tweet))
				break
			for word in content_words:
				if word.lower() == token.lower():
					useful_tweets.add(tuple(tweet))
					flag = True
					break
			if flag:
				break
		if not flag:
			non_useful_tweets.add(tuple(tweet))
	return useful_tweets, list(non_useful_tweets)

def Merge_for_summary(lis):
	tweets = lis
	all_bigrams = [list(bigrams([token for token in tweets])) for tweets in nltk_tweets]
	starting_nodes = [single_bigram[0] for single_bigram in all_bigrams]
	end_nodes = [single_bigram[-1] for single_bigram in all_bigrams]
	all_bigrams = [node for single_bigram in all_bigrams for node in single_bigram]
	all_bigrams = list(set(all_bigrams))

	bigraph = make_bigram_graph(all_bigrams, starting_node)
	path = breadth_first_search(bigram_graph, starting_nodes[1], end_nodes[2])
	bigram_paths = []

	for single_start_node in tqdm(starting_nodes): 
	    bigram_graph = make_bigram_graph(all_bigrams, single_start_node)
	    for single_end_node in end_nodes:
	        possible_paths = breadth_first_search(bigram_graph, single_start_node, single_end_node)
	        for path in possible_paths: 
	            bigram_paths.append(path)

	for tweet in nltk_tweets: 
	    bigram_paths.append(list(bigrams([token for token in tweets])))
	word_paths = []
	for path in tqdm(bigram_paths): 
	    word_paths.append(make_list(path))


	begin('COWABS')
	x = var(str('x'), len(word_paths), bool)
	y = var(str('y'), len(content_vocab), bool)
	maximize(sum([linguistic_quality(word_paths[i])*informativeness(word_paths[i])*x[i] for i in range(len(x))]) + sum(y));
	sum([x[i]*len(word_paths[i]) for i in range(len(x))]) <= L;
	for j in range(len(y)):
	    sum([x[i] for i in paths_with_content_words(j)])>= y[j]

	for i in range(len(x)):
	    sum(y[j] for j in content_words(i)) >= len(content_words(i))*x[i]

	solve()
	result_x =  [value.primal for value in x]
	result_y = [value.primal for value in y]
	end()
	chosen_paths = np.nonzero(result_x)
	chosen_words = np.nonzero(result_y)
	st = ''
	for i in chosen_paths[0]:
	   st += str(" ").join([token.encode('ascii', 'ignore') for token in word_paths[i]])
	   print ('. ')
	return st

def segregation(tweets):
	dic = {}
	counter = 0
	
	for tweet in tweets:
		dic[tuple(tweet)] = 0
		for token in tweet:
			if token.lower() in set(content_words):
				dic[tuple(tweet)] += 1
		counter += 1
	finalized_tweets = []
	for x in tweets:
		if dic[tuple(x)] > n_content_words:
			finalized_tweets.append(x)
	return finalized_tweets
def return_final_List(lis):
	#this function uses TF_IDF scores that we use to find important tweets
	score_lis = TF_IDF(lis)
	sorted_score_lis = sorted(score_lis, key = lambda x :x[1])
	final_index_lis = []
	for item in sorted_score_lis:
		if item[1] > predefined_threshold:
			final_index_lis.append(item[0])

	return [lis[i] for i in final_index_lis]
	




