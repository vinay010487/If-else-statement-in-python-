z=str(z)

def equality_check(x,y,z):
  if x==y or x==int(z) or y==int(z):
  #print('they are equal')
    return True
  else:
    return False

equality_check(2,1,'2')