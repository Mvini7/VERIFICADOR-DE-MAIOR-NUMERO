def maior_numero():

  a = float(input("Digite o primeiro numero: "))
  b = float(input("Digite o segundo numero: "))
  c = float(input("Digite o terceiro numero: "))

  if a >= b and a >= c:
    print(f"O maior numero é {a}.")
  elif b >= a and b >= c:
    print(f"O maior numero é {b}.")
  else:
    print(f"O maior numero é {c}.")

maior_numero()