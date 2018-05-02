# Python decorators are basically objects which are callable and are used to modify a function or a class during runtime.
# The way the Python decorator works is, the function (also called objects in Python given they are First class objects) is
# passed to a decorator (the one which is going to modify the original function behaviour) as an argument, the decorator 
# modifies the function and returns it. Here's an example where we have an original function which lets say finds square of a
# number and we want to modify the function so it returns a cube of a number.

def sqr_num(x):
  return x**2

# Now, we are going to modify this function during runtime to return a cube of a number and add an arbitary number to the result.

def decorator_function(original_function): # decorated function, the one resposible to modify the original function and return the modified version.
  
  def wrapper_function(x,y): # the real modification happens here, where we are finding the cube of a number and adding an arbitary number to the result.
    res = 0
    res = original_function(x)
    modified_result = res * x + y
    return modified_result
  return wrapper_function # this is the modified version of the function which is being returned.

@decorator_function
def sqr_num(x):
    return x**2

print(sqr_num(3,8)) # Observe that orginally the function sqr_num used to accept only one argument, and now post modification it accepts 2 arguments.

