import random

class MyList(list):                            # inherits from the list
    
    def shuffle(self):
        random.shuffle(self)

    def get_random(self):
        return random.choice(self)


# object

a = MyList([12,121,3,1,2,4,5,1,2,5])
a.sort()
print(a)
a.shuffle()
print(a)
print("random item from the list = ", a.get_random())
