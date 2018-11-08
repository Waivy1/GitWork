class Tail:
    size = 'medium'
    color = 'shcwarz'
    material = 'wool'

    def __init__(self, size, color):
        self.size = size
        self.color = color

wolf = Tail('big', 'grey')
print(wolf.color)