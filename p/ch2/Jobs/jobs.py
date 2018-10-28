#!/usr/bin/env python3

# Darius Jones
# COMP 354
# quick implemetation of job scheduling

def jobScheduling(jobs):

	listn = sorted(jobs)
	maxDeadline = max(jobs, key = lambda item:item[1])[1]

	jobs = listn[::-1]
	schedule = [ (0,0) for i in range(maxDeadline)]

	time = len(schedule) - 1
	total = 0

	for (profit, deadline) in jobs:
		if schedule[time] == (0,0) and time <= maxDeadline:
			schedule[time] = ((profit, deadline))
			total += profit
			time -= 1
	return total, schedule




def main():


	#(profit, deadline)
	jobs = [(35,3), (30,4), (25,4), (20,2), (15,3), (12,1), (5,2)]
	p1, s1 = jobScheduling(jobs)

	print("The schedule is ", s1)
	print("The profit is %d" %(p1))

	#(profit, deadline)
	jobs = [(10,1), (10,1), (8,2), (8,2), (4,6), (4,6), (4,6),(4,6)]
	p1, s1 = jobScheduling(jobs)

	print("The schedule is ", s1)
	print("The profit is %d" %(p1))


	pass

if __name__ == "__main__":
	main()