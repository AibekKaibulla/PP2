# Examples

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 


for x in "banana":
  print(x) 


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x) 
  if x == "banana":
    break


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) 


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x) 


for x in range(6):
  print(x) 


for x in range(2, 6):
  print(x) 


for x in range(2, 30, 3):
  print(x) 


for x in range(6):
  print(x)
else:
  print("Finally finished!")


for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")

#If the loop breaks, the else block is not executed.

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)


for x in [0, 1, 2]:
  pass

# having an empty for loop like this, would raise an error without the pass statement

# Exercises

fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
     continue
  print(x)

for x in range(6):
   print(x)

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana": 
     break
  print(x)