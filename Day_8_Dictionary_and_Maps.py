# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
phone_book={}

for i in range(0, n):
    entry = str(input()).split(" ")
    name = entry[0]
    number = int(entry[1])
    phone_book[name] = number

for i in range(0, n):
    name = input()
    if name in phone_book:
        print(name + "=" + str(phone_book[name]))
    else:
        print("Not found")
