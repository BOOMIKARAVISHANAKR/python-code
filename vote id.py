age=int(input('enter the age=',))
if(age>=18):
    print('you eligible for vote')
else:
    print('you not eligible for vote')
    print('you need to wait {}year'.format(18-age))    