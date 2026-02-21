"""
Kata: Which are in?
Nivel: 6 kyu
Enlace: https://www.codewars.com/kata/550554fd08b86f84fe000a58
Descripción: Dados dos arreglos de cadenas, devuelve un arreglo ordenado de las cadenas de a1 que son subcadenas de cadenas en a2.
"""

def in_array(array1, array2):
  result = []
  for word in array1:
    for string in array2:
      if word in string and word not in result:
        result.append(word)
  return sorted(result)

if __name__ == "__main__":
    a1 = ["arp", "live", "strong"]
    a2 = ["lively", "alive", "harp", "sharp", "armstrong"]
    expected = ["arp", "live", "strong"]
    
    result = in_array(a1, a2)
    print(f"Test: {result} | {'✅ PASÓ' if result == expected else '❌ FALLÓ'}")