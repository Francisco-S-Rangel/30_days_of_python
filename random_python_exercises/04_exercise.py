class Person:
    def __init__(self, name, age):
        # Public attribute (can be accessed from anywhere)
        self.name = name
        # "Protected" attribute (convention: internal use only)/ its not protected really... the underline means that should be!!! - convention: using 1 underline -> _
        self._age = age
        # "Private" attribute (name mangling) using 2 underlines -> __
        self.__secret = "Likes anchovy pizza!"
    
    def get_secret(self):
        return self.__secret

# Create object
person_one = Person("Francisco", 25)
# Public -> OK
print("Public:", person_one.name)
# Protected -> Still accessible (not enforced)
print("Protected:", person_one._age)
# Private -> Direct access will fail
# print(person_one.__secret) # Uncomment to see the error

# Private with getter method - RIGHT WAY TO DO IT!
print("Private using getter method:", person_one.get_secret())
# Private -> Accessible via name mangling (not recommended) - WRONG WAY TO DO IT! but it works...
print("Private (mangled) WRONG WAY!:", person_one._Person__secret)

# PYTHON DOES NOT ENFORCE TRUE PRIVATE FIELDS!!!!

print("----------------")

class Client(Person):
    def __init__(self, name, age, balance = 0):
        self.__balance = balance
        super().__init__(name, age)

    def get_client_info(self):
        return f"Name: {self.name} - Age: {self._age} - Balance: {self.__balance}$ - Secret: {self.get_secret()}"
    
client_one = Client("Denzel", 55, 120000)
print(client_one.get_client_info())
    