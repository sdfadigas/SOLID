class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "auau!"


class Cat(Animal):
    def speak(self):
        return "miau!"


class AnimalSound:
    def __init__(self, animal):
        self.animal = animal

    def make_sound(self):
        return self.animal.speak()

# Pode-se criar novas instâncias sem alterar a classe Animal
# Cria instâncias das classes Dog e Cat
dog = Dog("Belinha")
cat = Cat("Jujuba")

# Cria instâncias da classe AnimalSound passando as instâncias das classes Dog e Cat
dog_sound = AnimalSound(dog)
cat_sound = AnimalSound(cat)

# Imprime o som que cada animal faz
print(dog_sound.make_sound())  
print(cat_sound.make_sound())  


# A classe Animal é uma abstração que representa um animal genérico e possui um método speak() que é implementado pelas classes Dog e Cat. A classe AnimalSound depende da classe Animal, que é uma abstração, e não das classes Dog e Cat. Isso significa que, se você quiser adicionar uma nova classe que represente um animal diferente, você só precisa implementar o método speak() na nova classe e a classe AnimalSound poderá usá-la sem alterações.

# Assim o DIP permite que os módulos sejam desenvolvidos e testados independentemente uns dos outros, e facilita a adição de novas funcionalidades sem afetar o código existente.