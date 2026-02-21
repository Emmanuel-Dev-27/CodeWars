"""
Kata: Calculating with Functions
Nivel: 5 kyu
Enlace: https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39
Descripción: Implementa funciones para realizar operaciones matemáticas básicas.
"""
def zero(func=None):
  return func(0) if func else 0
def one(func=None): 
  return func(1) if func else 1
def two(func=None): 
  return func(2) if func else 2
def three(func=None): 
  return func(3) if func else 3
def four(func=None): 
  return func(4) if func else 4
def five(func=None): 
  return func(5) if func else 5
def six(func=None): 
  return func(6) if func else 6
def seven(func=None): 
  return func(7) if func else 7
def eight(func=None): 
  return func(8) if func else 8
def nine(func=None): 
  return func(9) if func else 9

def plus(num): 
  return lambda x: x + num
def minus(num): 
  return lambda x: x - num
def times(num): 
  return lambda x: x * num
def divided_by(num): 
  return lambda x: x // num

if __name__ == "__main__":
  test_case = []
  test_case.append(three(plus(four())))
  test_case.append(five(minus(three())))
  test_case.append(two(times(four())))
  test_case.append(seven(divided_by(two())))
  expected = [7, 2, 8, 3]
  for i, val in enumerate(test_case):
    result = val
    print(f"Test {i+1}: '{val}' -> '{result}' | {'✅' if result == expected[i] else '❌'}")