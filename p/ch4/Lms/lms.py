# Darius Jones
# 10/27/2018 
# Longest Monotone Subsequnce

def lms(sequnce):
		
	result = [1]
	length = len(sequnce)


	for index_j in range(length):
		maxCount = 0
		for index_i in range(index_j):
			if result[index_i] > maxCount and (sequnce[index_i] <= sequnce[index_j]):
				maxCount = result[index_i]

		result.append(maxCount +1)

	#result = set(result) 
	return result


def main():

	retval = lms([4,6,5,9,1])
	print(retval)
	retval1 = lms([15,27,14,38,26,55,46,65,85,])
	print(retval1)



if __name__ == '__main__':
	main()