"""
Kata: Find the added character
Nivel: 6 kyu
Enlace: https://www.codewars.com/kata/5971b219d5db74843a000052
Descripción: Encuentra el carácter que se ha añadido a una cadena.
"""

def added_char(s1, s2):
    s1_sorted = sorted(s1)
    s2_sorted = sorted(s2)
    
    for i in range(len(s1)):
        if s1_sorted[i] != s2_sorted[i]:
            return s2_sorted[i]
            
    return s2_sorted[-1]

if __name__ == "__main__":
  test = [
    ("abcd", "abcde", "e"),
    ("aeiou", "aeioub", "b"),
    ("", "a", "a"),
    ("a", "aa", "a"),
    ("abc", "abac", "a"),
  ]
  for s1, s2, expected in test:
    result = added_char(s1, s2)
    print(f"s1: {s1}, s2: {s2}, Resultado: {result}, Esperado: {expected}, {'✅' if result == expected else '❌'}")