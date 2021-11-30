class Ebob:
    def __init__(self,x):
        self.x = x

    def max_divide(self):
        for i in range(self.x - 1, 1, -1):
            if self.x % i == 0: return i

    def min_divide(self):
        for i in range(1, self.x):
            if self.x % i == 0: return i

    def list_of_divides(self):
        divides = []
        for i in range(1, self.x+1):
            if self.x % i == 0:
                divides.append(i)
        return divides

    def sum_of_divides(self):
        sum =0
        for i in self.list_of_divides():
            sum += i
        return sum

    def length_of_divides(self):
        return len(self.list_of_divides())


print(Ebob(86).max_divide())
print(Ebob(100).min_divide())
print(Ebob(86).list_of_divides())
print(Ebob(100).length_of_divides())
print(Ebob(100).sum_of_divides())


# bir sayinin butun tam bolenlerinin toplamini girdi olarak yazarak, O sayinin bize ne oldugunu gosteren program
def find_num(x):
    sum = 0
    max = x // 2
    min = x // 3

    for i in range(min,max):
        random_num = Ebob(i).sum_of_divides()
        if random_num == x: return i


print(find_num(217))