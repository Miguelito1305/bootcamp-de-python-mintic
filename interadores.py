my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

my_iter = iter(my_list)

print(next(my_iter))

text = "Hola mundo"

iter_text = iter(text)
for char in iter_text:
    print(char)
    
odd_iter = iter(range(1, 10, 2))

for num in odd_iter:
    print(num)
    
def my_generator():
    yield 1
    yield 2
    yield 3

for num in my_generator():
    print(num)
    
def fibonacci(limit):
    a, b = 0, 1
    
    while a < limit:
        yield a
        a, b = b, a + b 

for num in fibonacci(10):
    print(num)