#test code for flexible while
from FlexibleLoop import FlexibleWhile
import time

######## EXAMPLE 1: GENERAL USAGE ########
a = 0
b = 10

def before(): #define a function to be run before each condition check
    global a, b #you can use global a and b like this, or use the start_vals argument for a closed loop.
    a += 1
    b -= 1
    return a, b

def condition(a, b): #define the condition of the while loop, using the variables processed before
    return a < 5 and b > 5

print("Test 1")
# Using the FlexibleWhile as an iterator
for a,b in FlexibleWhile(before_func=before, cond_func=condition):
    print(f"Current values: a={a}, b={b}")
    if a == 3:
        print("Good value, continuing...")
        continue
    if b == 8:
        print("Eh, close enough")
        break
      
print("Test 1 ended")


######## EXAMPLE 2: LAMBDA USE ########

print("\n Test 2")
starttime = time.time()    
for timer in FlexibleWhile(before_func=     lambda: time.time()-starttime, #you can use lambda to make it easier
                           cond_func=       lambda timer: timer < 5, #gets the timer value from the before_funcs output
                           max_iterations=  10, #the loop will break after 10 iterations max
                           on_max_iterations=lambda: print("Max iterations reached")): #function to call if max_iterations is reached
    print(timer)
    time.sleep(1)

print("Loop 2 ended")


######### EXAMPLE 3: TIMEOUT ##########

print("\n Test 3")
for a,b in FlexibleWhile(before_func=   lambda a,b: (a+1,b+2), #example function
                         cond_func=     None, #this (or omitting cond_func alltogether) is the same as "while true:"
                         start_vals =   (0,0), #Starting vars of a and b. Must be a tuple even if you have a single var.
                         timeout=       1,
                         on_timeout=    lambda: print("Timeout reached")): #timeout in seconds. will break out if reached.
    print(a,b)
    time.sleep(0.1) 

print("Loop 3 ended")

######### EXAMPLE 3: CHANGING VARS WITHIN LOOP ##########
print("\n Test 4")

#you can get the class
MyLoop = FlexibleWhile(before_func  = lambda v: v*v, #square the v
                       cond_func    = lambda v: v!=-999, #an impossible condition
                       start_vals   = (2,), #must be a tuple, even for a single value
                       timeout      = 2,
                       on_timeout   = lambda v: print(f"\nTimeout of {MyLoop.timeout} seconds reached with a value of {v} in {MyLoop.iterations} iterations"))
                   
for v in MyLoop:
    print(f"{v} at {MyLoop.time_elapsed:.2f}")
    if v > 256:
        print(f"slow down buckaroo {v} is too high")
        MyLoop.values = (2,) #"v=2" will not set the internal value. You must use this. Remember to use tuples.
    time.sleep(0.1)
    
print(f"Loop 4 ended with {v}")
