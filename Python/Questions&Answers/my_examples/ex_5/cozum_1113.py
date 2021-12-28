number = int(input("give me a number : "))
base = int(input("which base arithmetic do you want to convert to?:  "))


def unitconverters(number, base):
    result = ''
    while base <= number:
        result += str(number % base)
        number = number // base
    result += str(number)
    result = result[::-1]
    return result


unitconverters(number, base)
if base < 10:
    print(f'{number} decimal = {unitconverters(number,base)} in base-{base}.')
else:
    print("base can not be bigger and equal than 10.")
