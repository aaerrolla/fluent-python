from bird import Bird
from duck import Duck

def greet(bird):
    bird.quack()

def greet_bird(bird: Bird) -> None:
    bird.quack()  # this will produce type error with mypy : error: "Bird" has no attribute "quack"  [attr-defined]

def greet_duck(bird: Duck) -> None:
    bird.quack()

def main():
    b1 = Bird()
    d1 = Duck()

    # greet(b1) #  this is runtime AttributeError 'Bird' object has no attribute 'quack'
    greet(d1) 

    # greet_bird(b1)  # runtime AttributeError: 'Bird' object has no attribute 'quack'
    greet_bird(d1)

    # greet_duck(b1) # runtime AttributeError: 'Bird' object has no attribute 'quack'
    greet_duck(d1)

if __name__ == "__main__":
    main()    