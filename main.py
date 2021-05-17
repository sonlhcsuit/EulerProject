a = "some_string"
print(id(a))
print(id("some" + "_" + "string")) # Notice that both the ids are same.
array = [1, 8, 15]
# A typical generator expression
gen = (x for x in array if array.count(x) > 0)
array = [2, 8, 22]
print(list(gen))
