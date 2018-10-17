def main():
	try:
		b=0
		n=int(input())
		while(n!=0):
			n=n/2
			if n==1:
				b=1
				break
		if b!=1:
			print('no')
		else :
			print('yes')
	except:
		print('invalid')
main()
