#음식 요금을 입력받는다.
cha = int(input('요금을 입력하시오 : '))

#부가세를 변수에 저장한다.
surtax = 1/10

#지불금액을 계산해 변수에 저장한다.
payment = cha + (cha * surtax)

#지불금액을 출력한다.
print("당신이 지불해야 되는 요금은 {:.1f}원입니다." .format(payment))