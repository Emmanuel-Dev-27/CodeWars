"""
Kata: Give me a Diamond
Nivel: 6 kyu
Enlace: https://www.codewars.com/kata/5503013e34137eeeaa001648
Descripción: Crea un diamante de asteriscos de tamaño n.
"""

def diamond(n):
    if n % 2 == 0 or n < 0:
        return None
    
    diamond = ""
    for i in range(1, n + 1, 2):
        diamond += " " * ((n - i) // 2) + "*" * i + "\n"
    for i in range(n - 2, 0, -2):
        diamond += " " * ((n - i) // 2) + "*" * i + "\n"
    return diamond

if __name__ == "__main__":
    tests = [
        (1, "*\n"),
        (3, " *\n***\n *\n"),
        (5, "  *\n ***\n*****\n ***\n  *\n"),
    ]
    for i, (n, expected) in enumerate(tests):
        result = diamond(n)
        print(f"Test {i+1}: n={n} | Resultado: {result} | {'✅' if result == expected else '❌'}")