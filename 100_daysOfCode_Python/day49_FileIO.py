# READING A FILE
""" 
f = open('file1.txt','r')

text = f.read()
print(text)
f.close() 

"""

# WRITING A FILE
""" 
f = open('file1.txt','a')
f.write('Hello, world  ')
f.close()

"""

with open('file1.txt','a') as f:
    f.write("\n")
    f.write("Hello everyone I am a very good person")
    









