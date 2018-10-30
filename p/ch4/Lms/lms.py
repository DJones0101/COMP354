# Darius Jones
# 10/27/2018 
# Longest Monotone Subsequnce



def lms(sequnce):
		
	result = dict()
	result[0] = 1
	length = len(sequnce)


	for index_j in range(length):
		maxCount = 0
		for index_i in range(index_j):
			if result[index_i] > maxCount and (sequnce[index_i] <= sequnce[index_j]):
				maxCount = result[index_i]

		result[index_j] = (maxCount + 1)

	 
	return result

def buildSubsequnce(sequnce):

	#this holds the array of results
	result =  lms(sequnce)
	#this is the max longest sequnce
	longestSeq = max(result,key =result.get)

	# The lms dictonary returns index : sequence length for that value, the index is
	# the index of the original list of values. If i reverse the the ordering to sequnce : index 
	# I can easily build the sequnce of values.

	result1 = dict()
	
	for index, length in result.items():
		result1[length] = index

	toReturn = []
	for length, index in list(result1.items())[::-1]:
		if longestSeq == length and :
			toReturn.append(sequnce[index])
			longestSeq -= 1


	return toReturn



		


		





	


def main():

	a1 = [4,6,5,9,1]
	#retval = lms(a1)
	a2 = buildSubsequnce(a1)
	print(a2)

	# print(a1)
	# for step, index in retval.items():
	# 	print("%d : %d " %(step,index))
	# print("-" * 50)

	# a2 = [15,27,14,38,26,55,46,65,85,]
	# retval1 = lms(a2)
	# print(a2)
	# for step, index in retval1.items():
	# 	print("%d : %d " %(step,index))


	# print("-" * 50)
	# a3 = [7,6,1,4,7,8,20]
	# retval2 = lms(a3)
	# print(a3)
	# for step, index in retval2.items():
	# 	print("%d : %d " %(step,index))

	# print("-" * 50)
	# a4 = [23,4,56,7,-3]
	# retval2 = lms(a4)
	# print(a4)
	# for step, index in retval2.items():
	# 	print("%d : %d " %(step,index))
	#print(retval)


	



if __name__ == "__main__":
	main()