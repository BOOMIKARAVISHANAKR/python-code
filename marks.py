tamil=int(input('enter the tamil mark=',))
english=int(input('enter the english mark=',))
maths=int(input('enter the maths mark=',))
science=int(input('enter the science mark=',))
social=int(input('enter the social mark=s',))
if(tamil>=35):
    if(english>=35):
        if(maths>=35):
            if(science>=35):
                if(social>=35):
                    print('you are all pass')
                elif(social<35):
                    print('you fail at social')
            elif(science<35):
                print('you fail at science')
        elif(maths<35) :
            print('you fail at maths')
    elif(english<35):
        print('you fail at english')
elif(tamil<35):
    print('you fail at tamil')
else:
    print('you are fail')                                    