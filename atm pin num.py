correct_pin="123456"
pin=int(input('enter the 6-digit pin number=',))
if correct_pin==pin:
    print('pin is correct. access granted')
else:
    print('pin is wrong.access invalid')
