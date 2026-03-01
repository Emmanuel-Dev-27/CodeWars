"""
Kata: Basic Calculator
Nivel: 7 kyu
Enlace: https://www.codewars.com/kata/5296455e4fe0cdf2e000059f
Descripción: Realiza operaciones aritméticas básicas.
"""

def calculate(num1, operation, num2):
  if operation == "+":
    return num1 + num2
  elif operation == "-":
    return num1 - num2
  elif operation == "*":
    return num1 * num2
  elif operation == "/":
    if num2 == 0:
      return None
    return num1 / num2
  else:
    return None

if __name__ == "__main__":
    tests = [
        (2, "+", 3, 5),
        (2, "-", 3, -1),
        (2, "*", 3, 6),
        (2, "/", 3, 0.6666666666666666),
    ]
    for i, (num1, operation, num2, expected) in enumerate(tests):
        result = calculate(num1, operation, num2)
        print(f"Test {i+1}: num1={num1}, operation={operation}, num2={num2} | Resultado: {result} | {'✅' if result == expected else '❌'}")