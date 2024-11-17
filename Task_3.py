d = 1.44
c = d * 1024 * 1024

p = 100
l = 50
s = 25
b = 4

book_size = p * l * s * b
n = int(c // book_size)

print("Количество книг, помещающихся на дискету:", n)
