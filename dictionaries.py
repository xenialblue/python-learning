phonebook = {
    "John" : 927808723,
    "Jack" : 872130987,
    "Jill" : 891723057,
    "Jake" : 938273443
}
for name, number in phonebook.items():
    print("Phone number of %s is %d" % (name, number))
    
#removing values
phonebook.pop("Jill")

if "Jake" in phonebook:
    print("Jake is listed")
    
if "Jill" in phonebook:
    print("Jill is not in list")