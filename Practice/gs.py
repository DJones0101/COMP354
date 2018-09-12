## Darius Jones
## Comp354
## 9/12/2018


men = ['david','todd','kaleb']
women = ['yumi' , 'savannah' , 'kim']

pref = {
	'david' : [ 'yumi' , 'savannah' , 'kim' ],
	'todd' : [ 'savannah' , 'yumi' ,  'kim'],
	'kaleb' : [ 'yumi' , 'savannah' , 'kim'] ,
 	'yumi' : ['todd' , 'david', 'kaleb'] ,
 	'savannah' : [ 'david' , 'todd' , 'kaleb'] ,
 	'kim' : [ 'david' , 'todd' , 'kaleb']
}

for n in pref:
	pref[n].reverse()

rank = { 'yumi' : {  'david' : 2 , 'todd' : 1 , 'kaleb' : 3 } ,
		 'savannah' : { 'david' : 1 , 'todd' : 2 , 'kaleb' : 3 } ,
         'kim' : {  'david' : 1 , 'todd' : 2 , 'kaleb' : 3 }
         }

freemen = list(men)
numpartners = len(men)
S = {}

while freemen:

	m = freemen.pop()
	#if len(pref[m]) == 0:
		#continue

	w = pref[m].pop()

	if w not in S:
		S[w] = m
	else:
		mprime = S[w]
		if rank[w][m] < rank[w][mprime]:
			S[w] = m
			freemen.append(mprime)
		else:
			freemen.append(m)

print(S)













