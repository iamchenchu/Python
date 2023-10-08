from operator import add


def format_address(address_string):
    house_number =" "
    stret_name = " "

    address_string=address_string.split()

    for number in address_string:
        if number.isdigit():
            house_number = number
        else:
            stret_name += number
            stret_name += ""
    return ("house number {} on the street name of {} ").format(house_number,stret_name)

print(format_address("123 main street"))       

