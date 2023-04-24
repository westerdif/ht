#두 개의 숫자를 입력받는다.
num1 = int(input('숫자를 입력하시오 : '))
num2 = int(input('숫자를 입력하시오 : '))

#1.
total = num1 + num2

#만약 두 개의 숫자가 모두 짝수라면
#두 수를 더한 값을 출력
if num1 % 2 ==0 and num2 % 2 ==0:
    print(" 두 수를 더한 값은")
    print("{} + {} = {}" .format(num1, num2, total))
    
#아니고 만약에 두 숫자 중 하나가 홀수이면
#몇 번째 수를 짝수로 입력해야 하는지 출력

elif num1 / 2 == 1:
    print("첫 번째 수를 짝수로 입력하시오")
    
else:
    print("두 번째 수를 짝수로 입력하시오")