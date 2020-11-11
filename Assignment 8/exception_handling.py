#Handling zero division error
def divide(x, y): 
    try:  
        result = x // y 
        print("The result is :", result) 
    except ZeroDivisionError: 
        print("ERROR! \nYou are dividing by zero. ") 

divide(3,0)


#Raising error 
def raiserror(x):
	if x > 3:
		raise Exception('\nx should not exceed 3.\n The value of x was: {}'.format(x))


#Handling raised error
def handlerror(x):
    try:
        raiserror(x)
    except:
        print("\nERROR!\nValue of x is greater than 3.")
        
handlerror(5)
