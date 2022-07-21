''' 조건문
a = 5
if a > 5:
    print('5 초과')
else:
    print('5 이하')
'''

'''
num = int(input()) # int를 붙이지 않으면 문자열 그대로 되기 때문에 int를 붙여 숫자로 만듬
if num % 2 == 1:
    print('홀수')
else:
    print('짝수')
'''

''' 복수조건문
dust = 80
if dust > 150:
    print('매우 나쁨')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
else:                           # 위의 모든 조건이 False인 경우
    print('좋음')
print('미세먼지 확인 완료')
'''


''' 중첩 조건문
dust = 500
if dust > 150:
    print('매우 나쁨')
    if dust > 300:                  #추가된 내용
        print('실내 활동을 자제하세요.')
elif dust > 80:
    print('나쁨')
elif dust > 30:
    print('보통')
elif dust >= 0:
    print('좋음')
else:             # 위의 모든 조건이 False인 경우
    print('값이 잘못 되었습니다')
'''
