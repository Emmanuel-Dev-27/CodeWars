"""
Kata: Simple Pig Latin
Nivel: 5 kyu
Enlace: https://www.codewars.com/kata/520b9d2ad5c005041100000f
Descripción: Convierte una cadena a formato Pig Latin.
"""

def pig_it(text):
  if text == "":
    return ""
  result = []
  for word in text.split():
    if word.isalpha():
      result.append(word[1:] + word[0] + "ay")
    else:
      result.append(word)
  return " ".join(result)

if __name__ == "__main__":
    tests = [
        ("Pig Latin", "IgPay atinLay"),
        ("Hello world", "elloHay orldway")
    ]
    for i, (text, expected) in enumerate(tests):
        result = pig_it(text)
        print(f"Test {i+1}: text='{text}' | Resultado: {result} | {'✅' if result == expected else '❌'}")