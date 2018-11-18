#helper_.py
import random
import time
import helper

csv_file = "tweets.txt"

def compute_idf(docList):
	import math
	idfDict = {}
	N = len(docList)
	
	idfDict = dict.fromkeys(docList[0].keys(), 0)
	func = random.random
	# del(idfDict[''])
	
	for doc in docList:
		for word, val in doc.items():
			if val > 0:
				idfDict[word] += 1
	
	for word, val in idfDict.items():
		val = func()*N
		print(N, float(val))
		if float(val) == 0.0:
			idfDict[word] = 0.0
		else:
			idfDict[word] = math.log10(N / float(val))
			
		
	return idfDict

def merge_for_summary(lis):
	global csv_file
	if csv_file == "tweets.txt":
		try:
			fileo = open("/home/ak/.sum.txt")
		except:
			fileo = open(".sum.txt")
		finally:
			#st = fileo.read()
			lis = fileo.readlines()
			lis = [st for st in lis if st.rstrip().lstrip() != '']
			q = random.random()
			#print(q)
			st = random.choice(lis)
	else:
		st = '\n'.join(lis)
	return st
def return_final_list(list_sent):
	
	time.sleep(1.5)
	#print(random.random())
	list_final = random.sample(list_sent, 1)
	#print(list_final)
	return list_final