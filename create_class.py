#%%
## CRIA CLASSES

class Exemplo():
    pass

# %%
x = Exemplo()
print(type(x))

# %%
class Dog():
    def __init__(self, raca):
        self.raca = raca
        self.idade = 10
    
    def envelhecer(self):
        self.idade += 1

# %%
dog = Dog('Lab')

# %%
print(dog.idade, dog.raca)

#%%
dog.envelhecer()

#%%
print(dog.idade, dog.raca)
# %%
class Circle:
    def __init__(self, raio=1):
        self.raio = raio
    
    def calcula_area(self):
        return self.raio ** 2 * 3.14
    
    def retorna_raio(self):
        return self.raio
    
# %%
c1 = Circle()
c2 = Circle(10)

#%%
c1.calcula_area()
#%%
c2.calcula_area()
# %%
## HERANCA
class Animal:
    def __init__(self):
        print('Animal criado')
    
    def quem_sou_eu(self):
        print('Eu sou um animal')
    
    def comer(self):
        print('Comendo')

class Cachorro(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Eu sou um cachorro')
    
    def quem_sou_eu(self):
        print('Eu sou um cachorro')
# %%
animal = Animal()
# %%
cachorro = Cachorro()
# %%
