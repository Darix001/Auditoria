#Find the duplicated items on a sequence

def main(lista):
	vistos = set()
	dups = []
	for item in lista:
    		if item in vistos:
        		dups.append(x)
		else:
			vistos.add(x)
        		

if __name__ == '__main__':
	print(main((1,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,6,4,32)))
