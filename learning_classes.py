class Tail:
    size = 'medium'
    color = 'shcwarz'
    material = 'wool'

    def __init__(self, size, color):
        self.size = size
        self.color = color

    def burn(self):
        pass

    def wear(self):
        pass


wolf = Tail('big', 'grey')
print(wolf.color)

class Cat (Tail):

    def lie(self, size):
        self.size = size


hlib = Cat('12', 'grey')
hlib.lie('10')
print(hlib.size)





