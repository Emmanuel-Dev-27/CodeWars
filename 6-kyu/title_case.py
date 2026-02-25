"""
Kata: Title Case
Nivel: 6 kyu
Enlace: https://www.codewars.com/kata/5202ef17a402dd033c000009
Descripción: Convierte una cadena a formato título.
"""

def title_case(title, minor_words=''):
    if title == "":
        return ""
    
    minor_words = minor_words.lower().split()
    title = title.lower().split()
    
    for i in range(len(title)):
        if i == 0 or title[i] not in minor_words:
            title[i] = title[i].capitalize()
    
    return " ".join(title)

if __name__ == "__main__":
    tests = [
        ("the quick brown fox jumps over the lazy dog", "The Quick Brown Fox Jumps Over The Lazy Dog"),
        ("the quick brown fox jumps over the lazy dog", "The Quick Brown Fox Jumps Over The Lazy Dog"),
    ]
    for i, (title, expected) in enumerate(tests):
        result = title_case(title)
        print(f"Test {i+1}: title='{title}' | Resultado: {result} | {'✅' if result == expected else '❌'}")