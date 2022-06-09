import random
r = random.randint(1,100)
count = 0
while True:
	count = count + 1
	m = input('請猜數字: ')
	m = int(m)
	if r == m:
		print('你猜對了!')
		print('已經猜了', count, '次了')
		break
	elif r > m:
		print('比答案小')
	elif r < m:
		print('比答案大')
	print('已經猜了', count, '次了')
		
