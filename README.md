#here z explictly define as String 
z=str(z)

#Created a function with 3 parameters where one of 
#them are String and rest of two are integers

def equality_check(x,y,z):
 
#now making z behave as it is integer 
  if x==y or x==int(z) or y==int(z):
     return True
  else:
    return False

equality_check(2,1,'2')
