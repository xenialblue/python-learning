class Dog:
    """A Class for Representating a dog"""
    def __init__(self, name, age):
        """Initialize a new dog"""
        self.name = name
        self.age = age
        
    def bark(self):
        """Generating the sound of the dog barking
        """
        print("he said WOOF!")
        
print(help(Dog))