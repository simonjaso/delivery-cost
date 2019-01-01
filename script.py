

wgt=41.5
def bestship (wgt):
#figure out just ground
  if wgt<=2:
    return wgt*1.5+20
  elif wgt>2 and wgt<=6:
    return wgt*3+20
  elif wgt>6 and wgt<=10:
    return wgt*4+20
  elif wgt>10:
    return wgt*4.75+20
print(bestship(wgt))
x=bestship(wgt)
#now define premium
premium = 125 
#now define drone pricing
def drone (wgt):
  if wgt<=2:
    return wgt*4.5
  elif wgt>2 and wgt<=6:
    return wgt*9
  elif wgt >6 and wgt<=10:
    return wgt*12
  elif wgt >10:
    return wgt*14.25
print(drone(wgt))
y=drone(wgt)
print(premium)
def cheapest (x,y,premium):
  if x<y and x<premium:
    print("the cheapest method of shipping is ground and costs $"+str(x))
  if y<x and y<premium:
    print("the cheapest cost of shipping is drone and costs $"+str(y))
  if premium<x and premium<y:
    print("the cheapest method is premium and costs $"+str(premium))
print (cheapest(x,y,premium))
