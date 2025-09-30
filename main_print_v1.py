#변수 선언
name = "AliceBB"
age = 45
score = 95.5
apple = "apple"

# 1. 기본출력
print("Hello, Python!")

# 2. 여러 값 출력
print("Name:", name, "Age:", age, "Score:", score)

# 3. f-string {}안에 변수 입력
print(f"My name is {name}, I am {age} years old, score: {score}")

# 4. format()함수
# 4-1. 순서대로 {} 안에 변수 입력
print("My name is {}, I am {} years old, score: {}".format(name, age, score))
# 4-2. {}안에 순서를 나타내는 숫자를 넣어 #4-1. 보다 유동적으로 입력 가능
print("My name is {0}, age {1}, score {2}".format(name, age, score))
# 4-3. : 포맷지정자의 시작, .2 소수점 아래 2자리까지 표시
print("Score with 2 decimals: {:.2f}".format(score))

# 5. %s : 문자열(string) 자리 표시자, %d : 정수(integer) 자리 표시자, %.1f : 부동소수점(float), 소수점 아래 1자리까지 표시
print("Name: %s, Age: %d, Score: %.1f" % (name, age, score))

# 6. \n 줄바꿈
print("This is line 1\nThis is line2")

#7. 자동줄바꿈을 공백 한 칸으로 바꿈
print("Hello", end=" ")
print("World!")
# 7-1. \t 는 들여쓰기
print("Hello\tWorld")
print('It\'s fine')
print("2025", "09", "23", sep="-")
# 7-3. 연습
print("My name is", name, sep="-")

data = {"name": name, "age":age, "score": score}

print("Date:", data)

print(f"Next year age: {age + 1}")
print(f"Score (rounded): {round(score)}")

print(f"""
Student Info:
- Name : {name}
- Age  : {age}
- Score: {score:.2f}
""")