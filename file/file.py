f = open("demo.txt", "rt") # open file
# print(f.read()) # read file
# print(f.read(11)) # read file part
print(f.readline()) # read line1
print(f.readline()) # read line2
print(f.readline()) # read line3

for x in f:
  print(x)

f.close()
