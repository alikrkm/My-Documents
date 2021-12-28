name = str(input("String : "))

print(name.capitalize().swapcase())
# print(name[0].lower() + name[1:].upper())

name_titled = name.title()

mid = len(name_titled) // 2

solution = chr(ord(name_titled[0]) + 32) + (len(name_titled) > 2 and (name_titled[1:(mid)] + chr(
    ord(name_titled[mid]) - 32) + name_titled[(mid+1):]) or name_titled[1:])

print((len(solution) > 2 and len(solution) % 2 == 0 and (solution[0:(mid-1)] + chr(
    ord(solution[mid-1]) - 32) + solution[(mid):]) or solution))