# Darius Jones
# 10/27/2018 
# Longest Monotone Subsequnce


def lms(sequnce):
		
	R = dict()
	R[0] = 1
	length = len(sequnce)

	for j in range(length):
		maximum = 0
		for i in range(j):
			if R[i] > maximum and (sequnce[i] <= sequnce[j]):
				maximum = R[i]
		R[j] = (maximum + 1)

	return R

def lmsd(sequnce, differnce):
		
	R = dict()
	R[0] = 1
	length = len(sequnce)

	for j in range(length):
		maximum = 0
		for i in range(j):
			if R[i] > maximum and abs(sequnce[i] - sequnce[j]) <= differnce:
				maximum = R[i]
		R[j] = (maximum + 1)

	return R

def buildSubsequnce(sequnce, differnce=None):
	''' Takes in the sequnce (list), and returns a LMS list '''

	#this holds the array of results
	if differnce == None:
		R = lms(sequnce)
	else:
		R = lmsd(sequnce,differnce)
	# (index, length)
	values = [(index, length) for (index, length) in R.items()]
	print(f"Index and Length : {values}")
	print(f"The sequnce : {sequnce}")

	results = []
	oldlenght = 0
	for i in range(len(values)):
		index, lenght = max(values, key=lambda x : x[1])
		if oldlenght != lenght and sequnce[index] not in results:
			print(f"The max value is {sequnce[index]}, The max lenght is {lenght}")
			results.append(sequnce[index])
			oldlenght = lenght
		values.remove((index,lenght))


	results = results[::-1]
	print(f"The results : {results}")
	return results



def main():

	seq1 = [4,6,5,9,1,]
	ar1 = buildSubsequnce(seq1)


	print("-" * 50)
	print("\n")
	seq2 = [15,27,14,38,26,55,46,65,85,]
	ar2 = buildSubsequnce(seq2)


	print("-" * 50)
	print(f"Problem 4.4 page 72")
	print("\n")
	seq3 = [7,6,1,4,7,8,20,]
	ar3 = buildSubsequnce(seq3,1)

	print("-" * 50)
	print("\n")
	seq4 = [23,4,56,7,-3]
	ar4 = buildSubsequnce(seq4)



	



if __name__ == "__main__":
	main()