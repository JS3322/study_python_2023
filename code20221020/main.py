print("hello python")

#변수
int10 = 10
stringName = "김준석"
booleanCheck = True
print(int10)
print(stringName)
print(booleanCheck)

#List
nameList = ["김준석", "이준석", "박준석", 1, False]
print(nameList[3])

#dictionary(key:value)
userList = {}
userList['age'] = 25
userList['name'] = "김준석"
userList['accountCheck'] = False
print(userList)
print(userList.get('age'))
userList['age'] = 21
print(userList.get('age'))

#if
if True:
    print('ifStart')
checkIf = False
if checkIf:
    print('Flase')
else:
    print('True')

#for
number10 = []
add = 0
for i in range(1, 11):
    add = add + i


for i in range(10):
    print(i)

a1 = [(1,2), (3,4), (5,6)]
for (first, last) in a1:
    print(first + last)

#function
def add(x, y, z):
    return x + y + z
print(add(1,4,5))

#default Function
a = "Good morning, man"
a.upper() # - 대문자로 바꿔줍니다.



a.lower() #  소문자로 바꿔줍니다.
a.count('m') # m이 몇개나 있는지 세줍니다.


a = "Life is too short"
a.replace("Life", "Your height")


a = "I regret what I did to you"
a.split()  # split은 문자열을 나누는 함수다.  값을 넣지 않으면 공백으로 잘라줍니다
['I', 'regret', 'what', 'I', 'did', 'to', 'you']

d = "home,mother,sweet"
d.split(",")
['home', 'mother', 'sweet']


a.swapcase() # 대문자와 소문자를 바꾸어준다.


str(3) # str은 문자열로 만들어주는 함수이다. str(3)을 실행하면 문자열이 된다.

len("hi") # 길이를 알려주는 함수이다.

