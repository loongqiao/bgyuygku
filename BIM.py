import types
h=input('height: ')
w=input('weight: ')
#print type(h)
#print type(w)
height=float(h)
weight=float(w)
bim=weight/(height*height)
if bim<=18.5:
    print('过轻')
elif 18.5<bim<25:
    print('正常')
elif 25<bim<28:
    print('过重')
elif 28<bim<32:
    print('肥胖')
else:
    print('严重肥胖')
