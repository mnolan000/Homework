a = 3
b = 5.8
c = "hi"

if a > b:
  print("something")

print(type(a))
print(type(b))
print(type(c))

c = 5
print(type(c))

my_list =  ["hi",3,"hello",5.3]
print(type(my_list))

print(my_list[0])
print(my_list[3])

my_list.append("milk")
print(my_list)

#access first character in the string
print(my_list[0][0])

#remove things from string
my_list.remove(3)
print(my_list)
my_list.pop(2)
print(my_list)

print(len(my_list))

print()

#exercise
to_do = ["call mom", "walk the dog", "go to the store"]
to_do.append("read a book")
to_do[1] = "finish homework"
to_do.remove("call mom")
print(len(to_do))
print(to_do)

coordinates = [
  [100,200],
  [200,300]
]