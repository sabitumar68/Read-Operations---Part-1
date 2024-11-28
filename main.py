file = open('Coding.txt','r')
print(file.read())
file.close()

file = open('coding.txt','r')
print("\n Read in parts \n")
print(file.read(8))
file.close()

file = open('Coding.txt','a')
file.write("Hi! I am Sabit Umar and I am 12 years old.")
file.close()