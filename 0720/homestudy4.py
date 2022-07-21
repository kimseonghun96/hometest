#주의 - print 함수와 return의 차이점
# print를 사용하면 호출될 때마다 값이 출력됨(주로 테스트를 위해 사용)
# 데이터 처리를 위해서는 return 사용

# return은 항상 하나의 값만 반환한다. 두개 이상의 값을 반환하는 방법은?
'''
반환 값을 튜플로 사용
def minus_and_product(x, y):
    return x - y, x * y
y = minus_and_product(4, 5)
print(y)
print(type(y))
'''
#함수 반환 정리
#return x -> none(void)
#return o -> 하나를 반환 ,  여러개를 원하면, Tuple활용
#똑바로 읽어도 거꾸로 읽어도 같은 단어를 찾는 함수
'''
word_list = ['우영우', '기러기', '별똥별', '파이썬']
def is_palindrome(word_list):
    palindrome_list = []
    for word in word_list:
        if word == word[::-1]:
          palindrome_list.append(word)
        return palindrome_list
print(is_palindrome(word_list))
'''

# 함수의 입력
# parameter : 함수를 정의할 때, 함수 내부에서 사용되는 변수
# Argument : 함수를 호출 할 때, 넣어주는 값
'''
def function(hma): #parameter : ham
    return ham

function('spam') #argument : 'spam'
'''

#가변 인자(*args)와 가변 키워드 인자 (**kwargs) 동시 사용 예시
#가변 인자와 가변 키워드 인자를 함께 사용할 수 있음
'''
def print_family_name(*parents, **pets):
    print("아버지 :", parents[0])
    print("어머니 :", parents[1])
    if pets:
        print("반려동물들..")
        for title, name in pets.items():
            print('{} : {}'.format(title, name))

print_family_name('아부지', '어무이', dog = '멍멍이', cat = '냥냥이' )
'''

