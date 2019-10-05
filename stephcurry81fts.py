import random 

numSims = 1000000
numStreaks = 0
numShots = 130

for i in range(numSims):
	gotStreak = 0
	makesStreak = 0 
	for j in range(numShots):
		if(random.random() < 0.903):
			makesStreak += 1 
		else:
			makesStreak = 0 
		if(makesStreak == 81):
			gotStreak = 1 
	if(gotStreak == 1):
		numStreaks += 1 

print(numStreaks/numSims * 100)




