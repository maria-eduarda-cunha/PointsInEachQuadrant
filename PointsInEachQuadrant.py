print("**** PARTE A ****")
import math

X = int(input("X origem: "))
Y = int(input("Y origem: "))

n = int(input("Quantidade de pontos: "))
i = 1
quadrante1 = 0
quadrante2 = 0
quadrante3 = 0
quadrante4 = 0

menor = float("inf")
maior = 0

p = 1
for z in range(n):
  print(f"Ponto #{p}")
  x = int(input("Coordenada x: "))
  y = int(input("Coordenada y: "))
    
  xtrans = x - X
  ytrans = y - Y
    
  if xtrans > 0 and ytrans > 0:
    quadrante1 += 1
  elif xtrans < 0 and ytrans > 0:
    quadrante2 += 1
  elif xtrans < 0 and ytrans < 0:
    quadrante3 += 1
  elif xtrans > 0 and ytrans < 0:
    quadrante4 += 1
    
  # distância euclidiana d=√(x2−x1)2+(y2−y1)2
  d = math.sqrt((xtrans**2) + (ytrans**2))
  if d < menor:
    menor = d
    ponto_menor = (x , y)
  if d > maior:
    maior = d
    ponto_maior = (x , y)
    
  if xtrans == 0 or ytrans == 0:
    print(f"Ponto ({x} , {y}) está sobre o eixo de coordenadas")
  elif x > X and y > Y:
    print(f"Ponto ({x} , {y}) no 1º quadrante.")
  elif x < X and y > Y:
    print(f"Ponto ({x} , {y}) no 2º quadrante.")
  elif x < X and y < Y:
    print(f"Ponto ({x} , {y}) no 3º quadrante.")
  elif x > X and y < Y:
    print(f"Ponto ({x} , {y}) no 4º quadrante.")
  p += 1

print(f"Ponto {ponto_menor} é o mais próximo, distância = {menor:.2f}.")
print(f"Ponto {ponto_maior} é o mais distante, distância = {maior:.2f}.")
print(f"Existe(m) {quadrante1} ponto(s) no 1º quadrante; {quadrante2} no 2º quadrante; {quadrante3} no 3º quadrante e {quadrante4} no 4º quadrante.")


print('''

**** PARTE B ****''')

X = int(input("X origem A: "))
Y = int(input("Y origem A: "))

tempo = int(input("Por quanto tempo o robô caminhará: "))

if tempo % 3 == 0:
  Xf = ((tempo / 3) * 2) + X
  Yf = (tempo / 3) + Y
if tempo % 3 == 1:
  tempo1 = tempo - 1
  Xf = ((tempo1 / 3) * 2) + X
  Yf = (tempo1 / 3) + Y + 1
if tempo % 3 == 2:
  tempo2 = tempo - 2
  Xf = ((tempo2 / 3) * 2) + X + 1
  Yf = (tempo2 / 3) + Y + 1
  
print(f"Ao final, o robô estará no ponto ({Xf:.0f},{Yf:.0f})")