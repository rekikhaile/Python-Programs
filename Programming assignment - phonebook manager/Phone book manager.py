'''
def get_user_input():
    line_count = input()

    user_input_lines = []

    for i in range(int(line_count)):
        user_input_lines.append(input())

    return user_input_lines
'''

def process_add_command(phone_book, arguments):
    number = int(arguments[0])
    name = arguments[1]

    if name in phone_book:
        phone_book[name].append(number)
    else:
        phone_book[name] = [number]

def process_delete_command(phone_book, argument):
    try:
        del phone_book[argument[0]]
    except:
        pass

def process_find_command(phone_book, argument):
    person_number = None

    try:
        person_number = phone_book[argument[0]]
    except:
        pass

    if person_number != None:
        number = None

        for n in person_number:
            if number == None or n < number:
                number = n

        return number
    else:
        return "not found"


def run_phone_book_manager():
    #lines = get_user_input()

    phone_book = {}

    '''
    for l in lines:
        parts = l.split()

        if parts[0] == "add":
            process_add_command(phone_book, parts[1:])
        elif parts[0] == "del":
            process_delete_command(phone_book, parts[1:])
        elif parts[0] == "find":
            print(process_find_command(phone_book, parts[1:]))
    '''

    input_line_count = int(input())

    for i in range(input_line_count):
        line = input()

        parts = line.split()

        if parts[0] == "add":
            process_add_command(phone_book, parts[1:])
        elif parts[0] == "del":
            process_delete_command(phone_book, parts[1:])
        elif parts[0] == "find":
            print(process_find_command(phone_book, parts[1:]))

run_phone_book_manager()
