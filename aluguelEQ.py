import datetime

class Equipamentos:
  def __init__(self, listaEQ, nomeEquipamento):
    self.listaEQ = listaEQ
    self.nomeEquipamento = nomeEquipamento
    self.equipamentoD = {}
    id = 1001

    with open(self.listaEQ) as eq: 
      conteudo = eq.readlines()
    
    for i in conteudo:
      self.equipamentoD.update({str(id):{"nome do equipamento":i.replace("\n",'' ), "nome do alugando ": "", "data do aluguel": "", "status": ""}})
      id = id + 1
 
  def imprimirEQ(self):
    print(" ------------------------------------------------")
    print("id:", "\t","\t","\t" "Nome:","\t","\t" "Situação:")
    print(" ------------------------------------------------")
    for chave, valor in self.equipamentoD.items():
      print(chave, "\t\t", valor.get("nome do equipamento"), '- [',valor.get("status"),']')
   
  def alugarEQ(self):
    idEQ = input("Digite o ID do equipamento que você deseja: ")
    dataAtual = datetime.datetime.now().strftime ("%d-%m-%Y %H:%M:%s")
    if idEQ in self.equipamentoD.keys():
      if not self.equipamentoD[idEQ]["status"] == "Disponivel":
        print (f"O equipamento foi alugado")
      elif self.equipamentoD[idEQ]["status"] == "Disponivel":
        nome = input ("digite seu nome: ")
        self.equipamentoD[idEQ]["nome do alugando"] = nome
        self.equipamentoD[idEQ]["data do aluguel"] = dataAtual
        self.equipamentoD[idEQ]["status"] = "Não disponivel"
        print("Emprestimo realizado com sucesso! \n")
      else:
        print("Equipamento não encontrado")
        return self.alugarEQ()

  def adicionarEQ(self):
    novoEQ = input("Digite o nome do novo equipamento: ")
    if novoEQ == " ":
      return self.adicionarEQ()
    else:
      with open(self.listaEQ,'a') as eq:
        eq.writelines(f"{novoEQ}\n")
        self.equipamentoD.update({str(int(max(self.equipamentoD))+1):{"nome do equipamento":novoEQ,
        "nome do alugando": '', "data do aluguel": '', "status": ''}})
        print(f"O equipamento {novoEQ} foi adicionado com sucesso!")  

  def retornaEQ(self):
    idEQ = input("Digite o ID do Equipamento: ")
    if idEQ in self.equipamentoD.keys():
      if self.equipamentoD[idEQ] ["status"] == "Disponivel": 
        print("Este equipamento não foi emprestado") 
        return self.retornaEQ()
      elif not self.equipamentoD[idEQ]["status"] == "Disponivel":
        self.equipamentoD[idEQ]["nome do alugando"] = '' 
        self.equipamentoD[idEQ]["data do aluguel"] = ''
        self.equipamentoD[idEQ]["status"] = "Disponivel"
        print("Devolução realizada com sucesso! \n")
      else:
        print("ID do equipamento não encotrado!")   