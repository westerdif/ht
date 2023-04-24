#정수를 입력받는다.
num = int(input('정수를 입력하시오 : '))

#만약 정수가 네 자리 수 이상이라면
if len(str(num)) >= 4:
    print("{}은 네 자릿 수 이상입니다." .format)
    
else:
    print("{}은 네 자릿수 이하 입니다." .format(num))