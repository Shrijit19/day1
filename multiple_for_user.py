name=input("Name of your figure:")
len=int(input("Length/height/radius of your figure:"))
brt=float(input("Breadth/base of your figure..if your fig is a circle enter 3.14:"))
def area(name,len,brt):
	if name=="triangle":
		ar=0.5*len*brt
		print(ar)
	elif name=="circle":
		ar=len*len*brt
		print(ar)
	elif name=="quadrilateral":
		ar=len*brt
		print(ar)
	else:
		print("name error")
a= area(name,len,brt)
print(a)
print("THANK YOU")