#whileloop1.py
d=0
while d<101:
	squared=d**2
	print(d,squared," ",end="")
	d=d+1
	if(d%5==0):
		print()
