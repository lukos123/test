



def summ(list):
	if len(list) == 1:
		return list[0]
	elif len(list) == 0:
		return None
	else:
		pop = list.pop(0)
		return pop + summ(list)


L = []
while True:
	i = input(">>")
	if i != "":
		L.append(int(i))
	else:
		break
print(summ(L))






