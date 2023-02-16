def insertionsort(A):
	i=1
	while i<len(A):
		j=i
		while j > 0 and A[j-1] > A[j]:
			A.insert(j,A.pop(j-1))
			j-=1
		i+=1


def main():
	x=[6,5,3,1,8,7,2,4]
	insertionsort(x)
	print(x)

if __name__ == '__main__':
	main()