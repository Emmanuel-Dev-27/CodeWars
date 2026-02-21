"""
Kata: Duplicate Encoder
Nivel: 6 kyu
Enlace: https://www.codewars.com/kata/54b42f9314d9229fd6000d9c
Descripción: Convierte una cadena a una nueva cadena donde cada carácter se vuelve "(" si aparece una vez, o ")" si aparece más de una vez.
"""

def duplicate_encode(word):
  word = word.lower()
  result = ""
  for char in word:
    if word.count(char) > 1:
      result += ")"
    else:
      result += "("
  return result

if __name__ == "__main__":
    test_cases = ["din", "recede", "Success", "(( @"]
    expected = ["(((", "()()()", ")())())", "))(("]
    
    for i, val in enumerate(test_cases):
        result = duplicate_encode(val)
        print(f"Test {i+1}: '{val}' -> {result} | {'✅' if result == expected[i] else '❌'}")