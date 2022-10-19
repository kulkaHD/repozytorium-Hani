"""
    Kalkulator wykonuje następujące operacje:
    - pobiera informacje, które działanie chcemy wykonać (dodawanie, odejmowanie,mnożenie,dzielenie)
    - pobiera wartości dla dwóch argumentów a i b zwracając uwagę użytkownika,gdy nie wpisze on wartości liczbowych. Uzytkownik może wpisać je ponownie.
    - dla dodawania i mnożenia mozliwe jest dodanie dowolnej liczby argumentów - tutaj również uzytkownik może popełniać błędy w wprowadzaniu danych. Może się poprawiać.

"""

import logging
logging.basicConfig(level=logging.DEBUG)

def add(a, b, *args):
    return a + b + sum(args)

def sub(a, b):
    return a - b

def mult(a, b, *args):
    result = a * b
    for i in args:
        result *= i
    return result

def div(a, b):
    return a / b

def check_user_input_float(input):
    try:
        float(input)
        return True
    except ValueError:
        return False 

def check_user_input_int(input):
    try:
        int(input)
        return True
    except ValueError:
        return False

operations = {
    "1": add,
    "2": sub,
    "3": mult,
    "4": div
    }

operations_instruction = '''Podaj numer operacji:
    1 (dodawanie)
    2 (odejmowanie)
    3 (mnożenie)
    4 (dzielenie) '''

op_log_info = {
        "1": "Wybrałeś dodawanie.",
        "2": "Wybrałeś odejmowanie.",
        "3": "Wybrałeś mnożenie.",
        "4": "Wybrałeś dzielenie."
        }

def get_data():
    op = input(operations_instruction)
    while op not in operations:
        print ("Poproszę o liczbę z zakresu 1-4.")
        op = input(operations_instruction)  
    logging.info(op_log_info[op])
    args=[]
    if op in ("1", "3"):
        how_many_num = (input("Ile liczb potrzebujesz w swojej operacji? "))
        while check_user_input_int(how_many_num) == False:
            logging.info("Nie wpisałeś liczby całkowitej. Wpisz liczbę całkowitą.")
            how_many_num = input("Ile liczb potrzebujesz w swojej operacji? ")
        how_many_num = int(how_many_num) 
        for i in range (how_many_num-2):
            x = input("Wpisz liczbę: ")
            while check_user_input_float(x) == False:
                logging.info("Nie wpisałeś liczby. Wpisz liczbę.")
                x = input("Wpisz liczbę: ")
            x = float(x)
            args.append(x)
      
    a = input("Wpisz liczbę: ")
    while check_user_input_float(a) == False:
        logging.info("Nie wpisałeś liczby. Wpisz liczbę.")
        a = input("Wpisz liczbę: ")
    a = float(a)
       
    b = input("Wpisz liczbę: ")
    while check_user_input_float(b) == False:
        logging.info("Nie wpisałeś liczby. Wpisz liczbę.")
        b = input("Wpisz liczbę: ")
    b = float(b)
    while op == "4" and b == 0:
        logging.warning("Nie można dzielić przez 0. Proszę wybrać inną liczbę.")
        b = input("Wpisz liczbę: ")
        while check_user_input_float(b) == False:
            logging.info("Nie wpisałeś liczby. Wpisz liczbę.")
            b = input("Wpisz liczbę: ")
        b = float(b)
   
    return op, a, b, args
    
def main():
    operation, a, b, args = get_data()
    result = operations[operation](a, b, *args)
    print ("wynik to: ", "%.2f" % result)
    return result

main()
