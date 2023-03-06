done = True

print(type(done) == bool)
if done :
    print("yes")
else :
    print("no")


book1 = True
book2 = False

read = any([book1, book2])
read = all([book1, book2])