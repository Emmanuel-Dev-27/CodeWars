"""
Kata: Multiples of 3 or 5
Nivel: 6 kyu
Enlace: https://www.codewars.com/kata/514b92a657cdc65150000006
Descripción: Encuentra la suma de todos los múltiplos de 3 o 5 debajo del número proporcionado.
"""

def solution(number):
  total = 0
  for i in range(number):
    if i % 3 == 0 or i % 5 == 0:
      total += i
  return total

if __name__ == "__main__":
    # Pruebas sugeridas por CodeWars
    test_cases = [10, 20, 0, -5]
    expected = [23, 78, 0, 0]
    
    for i, val in enumerate(test_cases):
        result = solution(val)
        print(f"Test {i+1}: Entrada {val} | Resultado: {result} | {'✅ PASÓ' if result == expected[i] else '❌ FALLÓ'}")