def func1(a , b): #Parameter Correspondence
   result = a - b
   print result
print "func1 first call"
func1(b=10,a=5) #keyword
print "func1 second call"
func1(10,5) #positional

def func2( a = 10, b = 5 ): #Formal Parameter Default Values
   result = a - b
   print result

print "func2 first call"
func2() #default values
print "func2 second call"
func2(3,2) #specified
print "func2 third call"
func2(3) #one default value

def func3( zeroes = [0] ): #Formal Parameter Default Values and Passing
   zeroes.append(0)
   print zeroes
print "func3 first call"
func3() #First call
print "func3 second call"
func3() #Second
print "func3 third call"
func3() #Third

def func4( *values ): #Variable number of actual parameters
   print len(values), "values: " , values, "in func4"

func4("1"), "after func4 first call" #1 value 
func4(3,5,0), "after func4 second call" #3 values

def func5( a ): #Parameter passing: doesn't effect arg of caller
   print a, id(a), "in func5"
   a = 2
   print a, id(a), "in func5"

func5(1)

def func6( array): #Parameter passing: doesn't effect arg of caller
   array = [0,0]
   print array, "in func6"

array = [1,2,3]
func6(array)
print array, "after func6 call"

def func7(array) : #Parameter passing: we copy its reference 
   array += [0,0]
   print array, "in func7"

array = [1,2,3]
func7(array), "after func7 first call"
print array

array = [1,2,3]
func7(array[:]) #SHALLOW COPY of array
print array, "after func7 second call"

