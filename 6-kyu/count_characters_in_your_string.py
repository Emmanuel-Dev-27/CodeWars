"""
Kata: Count characters in your string
Nivel: 6 kyu
Enlace: https://www.codewars.com/kata/52efefcbcdf57161d4000091
Descripción: Cuenta la cantidad de veces que aparece cada carácter en una cadena.
"""

def count(s):
  if s == "":
    return {}

  r = {}

  for i in s:
    if i in r:
      r[i] += 1
    else:
      r[i] = 1

  return r

if __name__ == "__main__":
    tests = [("aba", {"a": 2, "b": 1}), ("", {}), ("indivisibility", {"i": 6, "n": 1, "d": 1, "v": 1, "s": 1, "b": 1, "l": 1, "t": 1, "y": 1})]
    for i, (s, expected) in enumerate(tests):
        result = count(s)
        print(f"Test {i+1}: s='{s}' | Resultado: {result} | {'✅' if result == expected else '❌'}")
