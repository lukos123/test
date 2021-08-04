def binary_search(list, item):
	low = 0
	hegh = len(list) -1

	while low<hegh:
		midl=int((low+hegh)/2)
		gues = list[midl]
		if gues == item:
			return gues
		elif gues > item:
			hegh = midl -1
		else:
			low =midl +1

	return "нет"


L = ['бг','ба','г','я','б','а']
L.sort()
	
print(L)






