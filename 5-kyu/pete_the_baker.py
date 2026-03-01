"""
Kata: Pete, the Baker
Nivel: 5 kyu
Enlace: https://www.codewars.com/kata/525c65e51bf619685c000059
Descripción: Calcula cuántos pasteles puedes hacer con los ingredientes disponibles.
"""

def cakes(recipe, available):
  for ingredient in recipe:
    if ingredient not in available:
      return 0
    if available[ingredient] < recipe[ingredient]:
      return 0
  
  max_cakes = float('inf')

  for ingredient in recipe:
    max_cakes = min(max_cakes, available[ingredient] // recipe[ingredient])
  return max_cakes


if __name__  == "__main__":
  tests = [
    ({"flour": 500, "sugar": 200, "eggs": 1}, {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}, 2),
    ({"apples": 3, "flour": 300, "sugar": 150, "milk": 100, "oil": 100}, {"sugar": 500, "flour": 2000, "milk": 2000}, 0)
  ]
  for i, (recipe, available, expected) in enumerate(tests):
    result = cakes(recipe, available)
    print(f"Test {i+1}: recipe={recipe} | available={available} | Resultado: {result} | {'✅' if result == expected else '❌'}")