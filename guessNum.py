import random
r = random.randint(1,100)

while True:
	m = input('請猜數字: ')
	m = int(m)
	if r == m:
		print('你猜對了!')
		break
	elif r > m:
		print('比答案小')
		
	elif r < m:
		print('比答案大')
		
