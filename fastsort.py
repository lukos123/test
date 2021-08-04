import random

def spshort(arr):
	if len(arr) <2:
		return arr
	else:
		pilot = arr[0]
		m=[]
		b=[]
		for i in arr[1:]:
			if i <= pilot:
				m.append(i)
			else:
				b.append(i)
		f =spshort(m) + [pilot] +spshort(b)
		return f

A=[]

for i in range(5):
	A.append(random.randint(0,100))
print(A)


#print(A)

