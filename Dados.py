from Banco import Banco

class Dados(object):
	def __init__(self, idusuario = 0, nome = "", cpf = "", telefone = ""):
		print(idusuario, nome, telefone)

		self.info = {}
		self.idusuario = idusuario
		self.nome = nome
		self.cpf = cpf
		self.telefone = telefone

		print(idusuario, nome, telefone)

	def insertUser(self):
		banco = Banco()
		try:
			c = banco.conexao.cursor()
			print("OI")
			
			c.execute("insert into dados (nome, cpf, telefone) values ('" + self.nome + "', '" + self.cpf + "', '" + self.telefone + "')")

			banco.conexao.commit()
			c.close()

			return "Usuário cadastrado com sucesso"
		except:
			return "Ocorreu um erro na inserção do usuário"

	