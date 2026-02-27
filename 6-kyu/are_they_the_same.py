"""
Kata: Are they the same?
Nivel: 6 kyu
Enlace: https://www.codewars.com/kata/550498447451fbbd7600041c
Descripción: Comprueba si dos arrays son iguales.
"""
def comp(array1, array2):
    if array1 is None or array2 is None:
        return False
    
    array1_cuadrado = [x**2 for x in array1]

    return sorted(array1_cuadrado) == sorted(array2)


if __name__ == "__main__":
    tests = [
        ([121, 144, 19, 161, 19, 144, 19, 11], [121, 14641, 20736, 361, 25921, 361, 20736, 361], True),
    ]
    for i, (array1, array2, expected) in enumerate(tests):
        result = comp(array1, array2)
        print(f"Test {i+1}: array1={array1} | array2={array2} | Resultado: {result} | {'✅' if result == expected else '❌'}")