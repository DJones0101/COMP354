# Darius Jones
# 10/30/0218
# QuickSort


import random

def quickSort(sequnce):

    if len(sequnce) < 2:

        return sequnce

    else:
        pivot = random.choice(sequnce)
        lessThanPivot = [index for index in sequnce if index < pivot]
        equalToPivot = [index for index in sequnce if index == pivot]
        greaterThanPivot = [index for index in sequnce if index > pivot]
        return quickSort(lessThanPivot) + equalToPivot + quickSort(greaterThanPivot)


def main():
	seq = [15,27,14,38,26,55,46,65,85,]

	print(f"Unsorted list {seq}")
	print(f"Sorted list {quickSort(seq)}")

if __name__ == "__main__":
	main()