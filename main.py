import re
import csv
from operator import itemgetter
from collections import defaultdict

content_words = ['kerala', 'flood', 'injured', 'dead', 
				'missing', 'live', 'infrastructure', 
				'collapse', 'livestock', 'building', 
				'casuality', 'food', 'keralaflood', 'died',
				'destroyed', 'death', 'deaths', 'damaged', 'hundreds', 
				'thousands', 'bridges', '#keralaflood']


def isNum(s):
	try:
		int(s)
		float(s) # for int, long, float and complex
	except ValueError:
		return False

	return True

csv_file = "tweets.txt"
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


def segregation(tweets):
	dic = {}
	for tweet in tweets:
		dic[tuple(tweet)] = 0
		for token in tweet:
			if token.lower() in set(content_words):
				dic[tuple(tweet)] += 1
	finalized_tweets = []
	for x in tweets:
		if dic[tuple(x)] > 2:
			finalized_tweets.append(x)
	return finalized_tweets



def main():
	tweets = loadtext(csv_file)
	# print(tweets)
	# print("-------------------------\n\n")
	tweets = tokenize(tweets)
	# print(tweets)
	# print(len(tweets))
	# print("-------------------------\n\n")
	useful_tweets, non_useful_tweets = content_based_segregation(tweets)
	# print(useful_tweets)
	# print(len(useful_tweets))
	# print("-------------------------\n\n")
	useful_tweets = list(useful_tweets)
	useful_tweets = segregation(useful_tweets)

	# print(useful_tweets)
	# print(len(useful_tweets))





if __name__ == '__main__':
	main()