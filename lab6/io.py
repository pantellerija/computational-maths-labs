
def get_method_type():
    while True:
        try:
            method_choice = int(input('Enter\n'
                                           '0 -- modified euler method\n'
                                           '1 -- adams method\n'))
            if method_choice < 0 or method_choice >= 2:
                print('Error. Enter 0 or 1')
            else:
                break
        except ValueError:
            print("Error. Enter the number")
    return method_choice


def get_float(req):
    while True:
        try:
            num = float(input(req))
            return num
        except ValueError:
            print("Error. Enter the number")
