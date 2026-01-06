class Autor:
    def __init__(self):
        while True:
            try:
                self.nome = input("Digite o nome do autor: ")
                self.email = input("Digite o email do autor: ")
                self.descricao = input("Faça uma breve descrição sobre o Autor: ")
                break
            except ValueError as erro:
                print(f"Erro: {erro}")
                print("Tente novamente.\n")

    # Getter e Setter do nome
    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        if not nome.strip():
            raise ValueError("O nome não pode ser vazio.")
        if not nome.replace(" ", "").isalpha():  # permite apenas letras e espaços
            raise ValueError("O nome não pode conter números ou caracteres especiais.")
        self.__nome = nome

    # Getter e Setter do email
    @property
    def email(self):
        return self.__email
    
    @email.setter
    def email(self, email):
        if not (email.endswith("@gmail.com") or email.endswith("@hotmail.com")):
            raise ValueError("O email está no formato errado (apenas @gmail.com ou @hotmail.com).")
        self.__email = email

    # Getter e Setter da descrição
    @property
    def descricao(self):
        return self.__descricao
    
    @descricao.setter
    def descricao(self, descricao):
        if len(descricao) == 0 or len(descricao) > 150:
            raise ValueError("Sua descrição deve conter de 1 a 150 caracteres.")
        self.__descricao = descricao

    # Método para apresentar o autor
    def apresentar(self):
        print(f"""
Nome do Autor: {self.__nome}
Email: {self.__email}
Descrição do Autor: {self.__descricao}
""")

autor1 = Autor()
autor1.apresentar()
