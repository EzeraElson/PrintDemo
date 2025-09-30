# Python 기본 출력 및 문자열 포맷팅 예제

이 스크립트는 Python에서 다양한 방식으로 출력하는 기본 방법들을 예제로 보여줍니다.  
변수 선언부터 문자열 포맷팅, 여러 출력 옵션 등을 단계별로 설명합니다.

---

## 코드 설명

```python
# 변수 선언
name = "Alice"
age = 25
score = 95.5

# 1. 기본출력
print("Hello, Python!")

# 2. 여러 값 출력
print("Name:", name, "Age:", age, "Score:", score)

# 3. f-string {}안에 변수 입력
print(f"My name is {name}, I am {age} years old, score: {score}")

# 4. format() 함수
# 4-1. 순서대로 {} 안에 변수 입력
print("My name is {}, I am {} years old, score: {}".format(name, age, score))
# 4-2. {} 안에 순서를 나타내는 숫자 입력 (유동적 순서 지정 가능)
print("My name is {0}, age {1}, score {2}".format(name, age, score))
# 4-3. : 포맷지정자의 시작, .2 소수점 아래 2자리까지 표시
print("Score with 2 decimals: {:.2f}".format(score))

# 5. % 포맷팅
print("Name: %s, Age: %d, Score: %.1f" % (name, age, score))

# 6. \n 줄바꿈
print("This is line 1\nThis is line2")

# 7. 자동 줄바꿈을 공백 한 칸으로 바꿈
print("Hello", end=" ")
print("World!")
# 7-1. \t 는 들여쓰기(tab)
print("Hello\tWorld")
# 7-2. 특수문자 출력 예시 (작은 따옴표 escape)
print('It\'s fine')
# 7-3. 여러 값 출력 시 구분자 지정
print("2025", "09", "23", sep="-")
print("My name is", name, sep="-")

# 딕셔너리 출력
data = {"name": name, "age": age, "score": score}
print("Date:", data)

# 간단한 산술 연산 출력
print(f"Next year age: {age + 1}")
print(f"Score (rounded): {round(score)}")

# 여러 줄 문자열 출력 (f-string과 포맷팅 사용)
print(f"""
Student Info:
- Name : {name}
- Age  : {age}
- Score: {score:.2f}
""")
