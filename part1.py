# Part 1 of the Python Review lab.

def hello_world():
	return("hello world")

def greet_by_name(name):
        return("hello"+ " " + name)
	

def encode(x):
	return(x * 3953531 )
def decode(y):
        return(y/3953531)

f1=hello_world()

	
f2 =greet_by_name("Joyce")
f3 = encode(2)
f4 = decode(767)
print(f1)
print(f2)
print(f3)
print(f4)
if( f1 == "hello world") :
        print("passed")
else:
        print("failed")
if (f2 == "hello" +"Joyce"):
            print("passed")
else:
        print("failed")
if (f3 == 2*3953531):
            print("passed")
else:
        print("failed")

        
        


