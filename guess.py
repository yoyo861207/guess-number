import random
r = random. randint(1, 100)
count = 0
while True :
	count += 1 # count = count + 1
	num = input ('guess number')
	num = int(num)
	if num == r :
		print ('you guess right')
		break
	elif num > r : 
		print ('比答案大')
	elif num < r :
		print ('比答案小')
	print ('這是你猜的第',count,'次')