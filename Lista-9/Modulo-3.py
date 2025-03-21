# 7. Criando uma Classe Carro
# Implemente uma classe Carro com os atributos marca, modelo e ano. A classe deve ter
# um método exibir_detalhes() que imprime essas informações. No programa
# principal, crie dois objetos da classe e exiba seus detalhes.

class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def exibir_detalhes(self):
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nAno: {self.ano}")
        
carro1 = Carro("Chevrolet", "Onix", 2021)
carro2 = Carro("Fiat", "Uno", 2019)

carro1.exibir_detalhes()

carro2.exibir_detalhes()

# 8. Classe com Métodos Especiais (__str__ e __len__)
# Crie uma classe Livro com atributos titulo, autor e paginas. Implemente os
# métodos:
# • __str__(): Retorna uma string formatada com as informações do livro.
# • __len__(): Retorna o número de páginas.
# No programa principal, instancie um objeto da classe e exiba seus detalhes.

class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        
    def __str__(self):
        return f"Título: {self.titulo}\nAutor: {self.autor}\nPáginas: {self.paginas}"
        
    def __len__(self):
        return self.paginas
    
livro = Livro("Dom Casmurro", "Machado de Assis", 256)

print(livro)

# 9. Herança e Polimorfismo
# Crie uma classe Animal com um método fazer_som(). Depois, crie duas subclasses
# Cachorro e Gato que sobrescrevem esse método para imprimir sons específicos de cada
# animal. No programa principal, crie objetos das classes e chame fazer_som().

class Animal:
    def fazer_som(self):
        pass
    
class Cachorro(Animal):
    def fazer_som(self):
        print("Au au!")
        
class Gato(Animal):
    def fazer_som(self):
        print("Miau!")
        
cachorro = Cachorro()

gato = Gato()

cachorro.fazer_som()

gato.fazer_som()

