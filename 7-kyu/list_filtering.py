"""
Kata: List Filtering
Nivel: 7 kyu
Enlace: https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
Descripción: Crea una función que tome una lista de enteros no negativos y cadenas, y devuelva una nueva lista con las cadenas filtradas.
"""

def filter_list(l):
  new_list = []
  for item in l:
    if type(item) != str:
      new_list.append(item)
  return new_list

if __name__ == "__main__":
    test_cases = [[1, 2, 'a', 'b'], [1, 'a', 'b', 0, 15], [1, 2, 'aasf', '1', '123', 123]]
    expected = [[1, 2], [1, 0, 15], [1, 2, 123]]
    
    for i, val in enumerate(test_cases):
        result = filter_list(val)
        print(f"Test {i+1}: {val} -> {result} | {'✅' if result == expected[i] else '❌'}")