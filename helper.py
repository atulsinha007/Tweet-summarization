#helper.py
from tfidf import *
predefined_threshold = 0.5
def return_final_List(lis):
	#this function uses TF_IDF scores that we use to find important tweets
	score_lis = TF_IDF(lis)
	sorted_score_lis = sorted(score_lis, key = lambda x :x[1])
	final_index_lis = []
	for item in sorted_score_lis:
		if item[1] > predefined_threshold:
			final_index_lis.append(item[0])

	return [lis[i] for i in final_index_lis]
	




