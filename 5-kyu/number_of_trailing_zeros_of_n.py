"""
Kata: Number of trailing zeros of n!
Nivel: 5 kyu
Enlace: https://www.codewars.com/kata/52f787eb172a8b4ae1000a34
Descripción: Calcula el número de ceros al final de n!.
"""

def zeros(n):
  count = 0
  while n >= 5:
    n //= 5
    count += n
  return count

if __name__ == "__main__":
  test = [
    (0, 0),
    (6, 1),
    (30, 7),
    (100, 24),
    (1000, 249),
    (100000, 24999),
    (1000000000, 249999998)
  ]
  for i, (n, expected) in enumerate(test):
    result = zeros(n)
    print(f"Test {i+1}: n={n} | Resultado: {result} | {'✅' if result == expected else '❌'}")