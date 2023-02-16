def binarysearch(A,T):
	l=0
	r=len(A)-1
	while l<=r:
		m=(l+r)//2
		if A[m]<T:
			l=m+1
		elif A[m]>T:
			r=m-1
		else:
			return m
	return 'unsucessfull'

def main():
	sequence=range(0,100)
	binarysearch(sequence,50)

if __name__ == '__main__':
	main()