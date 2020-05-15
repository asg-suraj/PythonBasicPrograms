MIN_DRIVING_AGE = 18


def allowed_driving(name, age):
    """Print '{name} is allowed to drive' or '{name} is not allowed to drive'
       checking the passed in age against the MIN_DRIVING_AGE constant"""
    if age>= MIN_DRIVING_AGE:
        print (name+' is allowed to drive')
    else:
        print (name+' is not allowed to drive')

    
name= input()
try:
	age=int(input())
except Exception as e:
	raise



allowed_driving(name , age)