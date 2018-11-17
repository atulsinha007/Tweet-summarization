#helper_.py
import random
import time
def return_final_list(list_sent):
	random.seed(1)
	time.sleep(1.5)
	#print(random.random())
	list_final = random.sample(list_sent, 3)
	#print(list_final)
	return list_final
def merge_for_summary(lis):
	return '\n'.join(lis)

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