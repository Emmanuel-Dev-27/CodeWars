"""
Kata: Stop gninnipS My sdroW!
Nivel: 6 kyu
Enlace: https://www.codewars.com/kata/5264d2b162488dc400000001
Descripción: Invierte las palabras que tengan 5 o más letras en una cadena dada.
"""

def spin_words(sentence):
  words = sentence.split()
  for i in range(len(words)):
    if len(words[i]) >= 5:
      words[i] = words[i][::-1]
  return ' '.join(words)

if __name__ == "__main__":
    test_cases = ["Hey fellow warriors", "This is a test", "This is another test"]
    expected = ["Hey wollef sroirraw", "This is a test", "This is rehtona test"]
    
    for i, val in enumerate(test_cases):
        result = spin_words(val)
        print(f"Test {i+1}: '{val}' -> '{result}' | {'✅' if result == expected[i] else '❌'}")