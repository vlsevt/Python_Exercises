"""Car inventory."""
from collections import defaultdict, Counter, OrderedDict


def list_of_cars(all_cars: str) -> list:
    """
    Return list of cars.

    The input string contains of car makes and models, separated by comma.
    Both the make and the model do not contain spaces (both are one word).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi A4", "Skoda Superb", "Audi A4"]
    """
    car_list = []
    cars = ""
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    x = 0
    if all_cars != "":
        for char in all_cars:
            if char in alphabet and x != 2:
                cars += char
            elif char in alphabet and x == 2:
                cars += char
                x = 0
            elif char == " " and x == 0:
                cars += char
            elif char == " " and x == 2:
                cars = ""
                x = 0
            else:
                car_list.append(cars)
                x = 2
                cars = ""
        car_list.append(cars)
    return car_list


def car_makes(all_cars: str) -> list:
    """
    Return list of unique car makes.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4" => ["Audi", "Skoda"]
    """
    car_list = []
    new_car_list = []
    cars = ""
    x = 0
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    for char in all_cars:
        if char in alphabet and x != 2:
            cars += char
        elif char in alphabet and x == 2:
            cars += char
            x = 0
        elif char == " " and x == 0:
            car_list.append(cars)
            x = 1
        elif char == " " and x == 1:
            cars = ""
        elif char == " " and x == 2:
            cars = ""
            x = 0
        else:
            x = 2
            cars = ""
    for i in car_list:
        if i not in new_car_list:
            new_car_list.append(i)
    return new_car_list


def car_models(all_cars: str) -> list:
    """
    Return list of unique car models.

    The order of the elements should be the same as in the input string (first appearance).

    "Audi A4,Skoda Superb,Audi A4,Audi A6" => ["A4", "Superb", "A6"]
    """
    model_list = []
    new_model_list = []
    models = ""
    x = 0
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
    for char in all_cars:
        if char in alphabet and x != 2:
            models += char
        elif char in alphabet and x == 2:
            models += char
            x = 0
        elif char == " " and x == 0:
            models = ""
            x = 1
        elif char == " " and x == 1:
            models += char
        elif char == " " and x == 2:
            models = ""
            x = 0
        else:
            model_list.append(models)
            x = 2
            models = ""
    if all_cars != "":
        model_list.append(models)
    for i in model_list:
        if i not in new_model_list:
            new_model_list.append(i)
    return new_model_list


def search_by_make(all_cars: str, needed_make: str) -> list:
    """Find needed car make from a list."""
    car_list = []
    for car in list_of_cars(all_cars):
        for make in car_makes(car):
            if needed_make.lower() == make.lower() and " " not in needed_make:
                car_list.append(car)
    return car_list


def search_by_model(all_cars: str, needed_model: str) -> list:
    """Find needed car model from a list."""
    car_list = []
    for car in list_of_cars(all_cars):
        for model in car_models(car):
            for i in model.split():
                if needed_model.lower() == i.lower() and " " not in needed_model:
                    car_list.append(car)
    return car_list


def car_make_and_models(all_cars: str) -> list:
    """
    Create a list of structured information about makes and models.

    For each different car make in the input string an element is created in the output list.
    The element itself is a list, where the first position is the name of the make (string),
    the second element is a list of models for the given make (list of strings).

    No duplicate makes or models should be in the output.

    The order of the makes and models should be the same os in the input list (first appearance).

    "Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon Lux,Skoda Superb,Skoda Superb,BMW x5" =>
    [['Audi', ['A4']], ['Skoda', ['Super', 'Octavia', 'Superb']], ['BMW', ['530', 'x5']], ['Seat', ['Leon Lux']]]
    """
    if not all_cars:
        return list()

    make_model_list = [make_model.split(' ', 1) for make_model in all_cars.split(',')]
    make_model_dict = defaultdict(list)
    for make, model in make_model_list:
        if model not in make_model_dict[make]:
            make_model_dict[make].append(model)
    return [[key, values] for key, values in make_model_dict.items()]


def add_cars(car_list: list[[str, list[str]]], all_cars: str) -> list:
    """
    Add cars from the list into the existing car list.

    The first parameter is in the same format as the output of the previous function.
    The second parameter is a string of comma separated cars (as in all the previous functions).
    The task is to add cars from the string into the list.

    Hint: This and car_make_and_models are very similar functions. Try to use one inside another.

    [['Audi', ['A4']], ['Skoda', ['Superb']]]
    and
    "Audi A6,BMW A B C,Audi A4"

    =>

    [['Audi', ['A4', 'A6']], ['Skoda', ['Superb']], ['BMW', ['A B C']]]
    """
    if not all_cars:
        return car_list

    new_make_models = [car.split(' ', 1) for car in all_cars.split(',')]
    car_dict = defaultdict(OrderedDict, {make: OrderedDict.fromkeys(models) for (make, models) in car_list})
    for new_make, new_model in new_make_models:
        car_dict[new_make][new_model] = None
    return [[make, list(models)] for make, models in car_dict.items()]


def number_of_cars(all_cars: str) -> list:
    """
    Create a list of tuples with make quantities.

    The result is a list of tuples.
    Each tuple is in the form: (make_name: str, quantity: int).
    The order of the tuples (makes) is the same as the first appearance in the list.
    """
    if all_cars == '':
        return []
    all_cars_list = [car.split(' ', 1)[0] for car in all_cars.split(',')]
    counter = Counter(all_cars_list, )
    return [(make, count) for make, count in counter.items()]


def car_list_as_string(cars: list) -> str:
    """
    Create a list of cars.

    The input list is in the same format as the result of car_make_and_models function.
    The order of the elements in the string is the same as in the list.
    [['Audi', ['A4']], ['Skoda', ['Superb']]] =>
    "Audi A4,Skoda Superb"
    """
    return ','.join([f'{make} {model}' for make, models in cars for model in models])


if __name__ == '__main__':
    # print(search_by_model("Audi A4, Audi a40 2021, Tesla Model S, Audi A4 2020", "A4"))
    print(car_make_and_models(''))
    print(car_make_and_models("Audi A4,Skoda Super,Skoda Octavia,BMW 530,Seat Leon Lux,Skoda Superb,Skoda Superb,BMW x5"))
    print(add_cars([['Audi', ['A4']], ['Skoda', ['Superb']]], "Audi A6,BMW A B C,Audi A4"))
    print(add_cars([['Audi', ['A4']]], ""))
    print(number_of_cars("Audi A4,Skoda Superb,Seat Leon,Audi A6"))  # [('Audi', 2), ('Skoda', 1), ('Seat', 1)]
    print(number_of_cars("Mazda 6,Mazda 6,Mazda 6,Mazda 6"))  # [('Mazda', 4)]

    print(number_of_cars(""))  # []

    print(car_list_as_string([['Audi', ['A4']], ['Skoda', ['Superb']]]))  # "Audi A4,Skoda Superb"
