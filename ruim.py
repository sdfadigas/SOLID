class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass


class Dog:
    animal=Animal()
    def speak(self):
        return "auau!"


class Cat:
    animal=Animal()
    def speak(self):
        return "miau!"



dog = Dog("Belinha")
cat = Cat("Jujuba")



# A classe Animal é uma abstração que representa um animal genérico e possui um método speak() que é implementado pelas classes Dog e Cat. A classe AnimalSound depende da classe Animal, que é uma abstração, e não das classes Dog e Cat. Isso significa que, se você quiser adicionar uma nova classe que represente um animal diferente, você só precisa implementar o método speak() na nova classe e a classe AnimalSound poderá usá-la sem alterações.

# Assim o DIP permite que os módulos sejam desenvolvidos e testados independentemente uns dos outros, e facilita a adição de novas funcionalidades sem afetar o código existente.