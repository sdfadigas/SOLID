class Animal:
    def speak(self):
        print("au au")


class Dog:
    def __init__(self, animal: Animal):
        self.animal = animal

    def latir(self):
        return self.animal.speak()
    

    
b=Animal()    
a=Dog(b)
a.latir()


 