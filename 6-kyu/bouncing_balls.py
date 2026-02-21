"""
Kata: Bouncing Balls
Nivel: 6 kyu
Enlace: https://www.codewars.com/kata/5544c7a5cb454edb3c000047
Descripción: Calcula cuántas veces una madre verá pasar una pelota frente a su ventana después de caer desde una altura 'h'.
"""

def bouncing_ball(h, bounce, window):
  if h <= 0 or bounce <= 0 or bounce >= 1 or window >= h:
    return -1
  count = 0
  while h > window:
    count += 1
    h *= bounce
    if h > window:
      count += 1
  return count

if __name__ == "__main__":
    # h, bounce, window
    tests = [(3, 0.66, 1.5), (30, 0.66, 1.5), (3, 1, 1.5)]
    expected = [3, 15, -1]
    
    for i, (h, b, w) in enumerate(tests):
        result = bouncing_ball(h, b, w)
        print(f"Test {i+1}: h={h}, b={b}, w={w} | Resultado: {result} | {'✅' if result == expected[i] else '❌'}")