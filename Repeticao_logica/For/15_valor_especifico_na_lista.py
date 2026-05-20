nomes = ["Ana", "Bruno", "Carla", "Daniel"]
acertos = []

while len(acertos) != len(nomes):
  palpite = input("---Adinhe  quem foram  os sorteados da turma: ---\n").strip()
  if palpite in  acertos:
         print("---Este acerto já foi contabilizado!---\n")
  elif palpite in nomes:
      acertos.append(palpite)
      print("---Acertou! Prossiga...\n")
  else:
         print("---Tente novamente!---\n")

if len(acertos) == len(nomes):
  print("---Parabéns você acertou todos os nomes!---")







