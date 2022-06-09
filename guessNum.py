import random
r = random.randint(1,100)
count = 0
while True:
	count = count + 1
	m = input('請猜數字: ')
	m = int(m)
	if r == m:
		print('你猜對了!')
		break
	elif r > m:
		print('比答案小')
		print('已經猜了'+ str(count) +'次了')
	elif r < m:
		print('比答案大')
		print('已經猜了'+ str(count) +'次了')
		
