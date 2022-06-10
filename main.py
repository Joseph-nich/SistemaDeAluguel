
from aluguelEQ import Equipamentos as EQ

b1= EQ("eq.txt","aluguelEQ")
while True :
  print ('====================')
  print (' Menu Equipamentos ')
  print ('====================')
  print ('opções:')
  print ('1- Alugar')
  print ('2- Devolver')
  print ('3- Adicionar')
  print ('4- Imprimir')
  print ('5- Sair')
  operacao=input('que operação deseja fazer?:')
  if (operacao=='1'):
    b1.alugarEQ()
  elif (operacao=='2'):
    b1.retornaEQ()
  elif (operacao=='3'):
    b1.adicionarEQ()
  elif (operacao=='4'):
    b1.imprimirEQ()
  elif (operacao=='5'):
    break

