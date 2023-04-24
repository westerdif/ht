#두 정수를 입력받는다.
x = int(input('정수를 입력하시오 : '))
y = int(input('정수를 입력하시오 : '))

#계산식대로 
if x>y : 
    if y!=0 :
        print("{} // {} = {}".format(x,y,x//y))
    else:
        print("y의 값이 0 입니다.")
elif x<y:
    print("{} + {} = {}".format(x,y,x+y))
else:
    print("{} + {} = {}".format(x,y,x+y))

