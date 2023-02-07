testing = 'nama saya nanda'
print(testing.upper())
print(testing.lower())
print(testing)
print(testing.find('nanda'))
print(testing.replace('n', 'p'))
print('nama' in testing)

astring = "hello world!"
print(astring[3:7:2])

s = "Strings are awesome!"
print("Length of s = %d" % len(s))
print("The first occurence of the letter a = %d" % s.index("a"))
print("a occurs %d times" % s.count("a"))

print("The first five characters are '%s'" % s[:5])
print("The next five characters are '%s'" % s[:5:10])
print("The thirteen character are '%s'" % s[:12])
print("The characters with odd index are '%s'" % s[1::2])
print("The last five characters are '%s'" % s[-5:])

print("In Uppercase : %s " % s.upper())
print("In Uppercase : %s " % s.lower())

print("Split the words : %s " % s.split())