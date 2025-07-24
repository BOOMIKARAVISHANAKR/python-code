unit=int(input('Total amount of unit=',))
if(unit>500):
 total=unit*5
 print('enter the total amount=',total)
elif(unit>=350):
 total=unit*3.5
 print('enter the total amount=',total)
elif(unit>=200):
 total=unit*2.60
 print('enter the total amount=',total)
elif(unit>=100):
 total=unit*1.35
 print('enter the total amount=',total)
else:
 total=unit*.65
 print('enter the total amount=',total)    