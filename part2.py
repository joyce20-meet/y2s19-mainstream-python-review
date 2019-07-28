# Part 2 of the Python Review lab.
def encode1(a):
        if a > 1:
                for i in range(2,a):
                        if a%i ==0:
                              return False
                        
                return True        
                

def encode(x, y):
        while not encode1(x):
                x += 1
        while not encode1(y):
                y += 1
        if 1< y <250 and 500<x<1000:
                return (x*y)
	

	else:
		print("Invalid input: Outside range")
		return (None)
f5 = encode(700,500)
print(f5)	

def decode(coded_message):
        for i in range (2,250):
                if not encode(y):
                        continue
                if coded_message /y ==0:
                        x = coded_message / y
                        if (encoded(int(x)) and 500<x<1000:
                            return(x,y)

	
