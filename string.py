# url = 'https://akashmallik.com'

# #list[start:end:step]

# print(url)
# # Reverse the url
# print(url[::-1])
# # Get the top level domain
# print(url[-4:])
# # Print the url without the https://
# print(url[8:])
# # Pritn the url without the https:// or the top level domain
# print(url[8:-4])


message = 'Hello World'
print(message)
# lowercase
print(message.lower())
# uppercase
print(message.upper())
# count 
print(message.count('l'))
# find
print(message.find('World'))
print(message.find('world'))
# replace
print(message.replace('l', 'L', 2))

#concatenation
gretting = "Hello"
name = "Akash"
message = gretting + ', ' + name
print(message)

# Formated string
message = '{}, {}, Welcome!'.format(gretting, name)
print(message)
message = f'{gretting}, {name}, Welcome!'
print(message)
