mytuple=("apple","banana","cherry")
print(mytuple[2])
print(mytuple[-1])
print(len(mytuple))

print(type(mytuple))

fruits = ("apple","banana","cherry")
mytuple = fruits * 2
print(mytuple)

mytuple1 = ("apple","banana","cherry")
mytuple2 = ("mango","orange","avocado")
mytuple3 = mytuple1 + mytuple2
print(mytuple3)

fruits=list(fruits)
print(fruits)

fruits.insert(-2,"kiwi")
print(fruits)

mytupletolist=list(fruits)
print(mytupletolist)
mytupletolist.append("lemon")
print(mytupletolist)

mytupletolist.remove("kiwi")
print(mytupletolist)

mytupletolist.extend(["watermelon","pineapple"])
print(mytupletolist)

fruits.sort()
print(fruits)









