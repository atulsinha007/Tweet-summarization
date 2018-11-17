import re
import csv
from operator import itemgetter
from collections import defaultdict

def compute_tf(wordDict, bow):
	tfDict = {}
	bowCount = len(bow)
	for word, count in wordDict.items():
		tfDict[word] = count/float(bowCount)
	return tfDict


def compute_idf(docList):
	import math
	idfDict = {}
	N = len(docList)
	
	idfDict = dict.fromkeys(docList[0].keys(), 0)
	# del(idfDict[''])
	for doc in docList:
		for word, val in doc.items():
			if val > 0:
				idfDict[word] += 1
	
	for word, val in idfDict.items():
		if float(val) == 0.0:
			idfDict[word] = 0.0
		else:
			print("======================================")
			print(N, float(val))
			idfDict[word] = math.log10(N / float(val))
		
	return idfDict


def compute(tfBow, idfs):
	tfidf = {}
	for word, val in tfBow.items():
		# print(val, idfs[word])
		tfidf[word] = val*idfs[word]
	return tfidf


def tweet_score(tfidf_i):
	# print(tfidf_i)
	score = 0.0
	# for i in range(len(tfidf_i)):
	# 	score += float(tfidf_i[i])
	for key in tfidf_i.keys():
		score += (tfidf_i[key])
	return score


def TF_IDF(tweets):
	# print(tweets[0])
	wordset = set(tweets[0])
	for tweet in tweets:
		wordset = wordset.union(tweet)
	# print(wordset)
	wordset.remove('')
	listofdic = []
	for i in range(len(tweets)):
		listofdic.append(dict.fromkeys(wordset, 0))

	for i in range(len(tweets)):
		for word in tweet:
			listofdic[i][word] += 1
	# print(listofdic[0])
	listofdic_tf = []

	for i in range(len(tweets)):
		listofdic_tf.append(compute_tf(listofdic[i], tweets[i]))

	idfDict = compute_idf(listofdic)
	tfidf = []
	for i in range(len(tweets)):
		tf_i = listofdic_tf[i]
		tfidf.append(compute(tf_i, idfDict))

	for i in range(len(tweets)):
		print(tweet_score(tfidf[i]))

