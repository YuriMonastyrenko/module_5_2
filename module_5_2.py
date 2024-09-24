class House:
    def __init__(self, name, floors):
        self.name = name
        self.number_of_floors = floors

    def __len__(self):
       return self.number_of_floors

    def __str__(self):
        return (f'Название: {self.name}, кол-во этажей: {self.number_of_floors}')

    def __del__(self):
        print(f'{self.name} снесли :(')

    # def go_to(self, new_floor):
    #     floor = 0
    #     for i in range(1, new_floor):
    #         if new_floor > self.number_of_floors:
    #             print('Такого этажа не существует')
    #             break
    #         else:
    #             floor += 1
    #             print(floor)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)
print(h1)
print(h2)
print(len(h1))
print(len(h2))

