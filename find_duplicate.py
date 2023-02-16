import itertools, collections
def main(lista=range(100)):
	value=1
	return next(filter(value.__gt__,map(lista.count,lista)),None)

if __name__ == '__main__':
	print(main((1,2,3,4,5,6,7,8,9,10,2,3,4,5,6,7,8,6,4,32)))