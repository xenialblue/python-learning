def my_function():
    print("Function Here")
    
def argumen(username, greeting):
    print("Hello %s and here is function %s"%(username, greeting))
    
def sum_twonumber(a,b):
    return a+b

my_function()
argumen("John Doe", "a Great Day!")
x = sum_twonumber(1,2)
print(x)

def list_benefits():
    return "pintar", "jago problem solving", "paham komputer", "bisa jadi programmer"
def build_sentence(benefit):
    return "%s is a benefit of functions!" %benefit

def name_the_benefits_of_functions():
    list_of_benefits = list_benefits()
    for benefit in list_of_benefits:
        print(build_sentence(benefit))
        
name_the_benefits_of_functions()