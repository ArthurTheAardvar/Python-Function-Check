import random

def monster():
    num = random.randrange(0, 100)
    if num < 20:
        print("skeleton")
    elif num >= 20 and num <= 50:
        print("zombie")
    elif num >= 50 and num <= 60:
        print("witch")
    else:
        print("nothing")


while True:
    print("Heres your monster")
    monster()
    