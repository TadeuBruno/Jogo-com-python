import random
print("-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
print("Vou pensar em um número entra 0 e 5. Tente adivinhar...")
print("-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
var1 = int(input("Em que número eu pensei? "))
num = random.randint(1,5)
if var1 == num:
  print("Parabéns, você conseguiu me vencer!")
else: 
  print("GANHEI! Eu pensei no número {} e não no {}!".format(num, var1))