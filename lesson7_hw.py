# 1.


class Matrix:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def __add__(self):
        matrix = [
            [1, 2, 3],
            [1, 2, 3],
            [1, 2, 3]
        ]

        for i in range(len(self.list1)):

            for j in range(len(self.list2)):
                matrix[i][j] = self.list1[i][j] + self.list2[i][j]
        return str("\n".join(["\t".join([str(j) for j in i]) for i in matrix]))

    def __str__(self, matrix):
        return str("\n".join(["\t".join([str(j) for j in i]) for i in matrix]))


final_res = Matrix([
    [3, 2, 1],
    [6, 5, 4],
    [9, 8, 7]],
    [[11, 12, 13],
     [14, 15, 16],
     [17, 18, 19]
     ])

print(final_res.__add__())

# 2.

from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, cost):
        self.cost = cost

    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, cost):
        super().__init__(cost)

    @property
    def consumption(self):
        return round(self.cost / 6.5 + .5 , 2)


class Suit(Clothes):
    def __init__(self, cost):
        super().__init__(cost)

    @property
    def consumption(self):
        return round(self.cost * 2 + .3 , 3)

coat = Coat(int(input("Пальто: ")))
suit = Suit(int(input("Костюм: ")))

print(coat.consumption,suit.consumption)
