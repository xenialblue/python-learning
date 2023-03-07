phonebook = {
    "Roger" : 92819,
    "Bob" : 98219,
    "Jill" : 91203
}

phonebook["James"] = 92014

del phonebook ["Bob"]
print(phonebook.get("Jill"))
print("Bob" in phonebook)
print(list(phonebook.items()))
print(len(phonebook))