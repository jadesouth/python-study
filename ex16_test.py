from sys import argv

(script, file_name) = argv

open_file = open(file_name)

print(open_file.readline(),)
print(open_file.read())
print(open_file.read())
print(open_file.read())
