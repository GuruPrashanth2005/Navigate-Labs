import random
print(random.randint(1, 10))
print(random.random())
print(random.choice(['apple', 'banana', 'cherry']))
list = [1, 2, 3, 4, 5]
random.shuffle(list)
print(list)
print(random.choice(list))
