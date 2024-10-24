element = "a"
argument = tuple()
while element != "":
    element = input("Enter an element: ")
    if element == "":
        break
    argument = argument + (element, )



def list_items(argument: tuple):
    if argument:
        if len(argument) > 1:
            output_string = ""
            for i in range(len(argument) - 1):
                if i == 0 and str(argument[0]).isalpha():
                    output_string += f"{argument[0].capitalize()}, "
                else:
                    output_string += f"{argument[i]}, "
            output_string += f"{argument[-1]}."
            return output_string
        elif len(argument) == 1 and str(argument[0]).isalpha():
            return f"{argument[0].capitalize()}."
        elif len(argument) == 1:
            return f"{argument[0]}."
    else:
        return ""


def write_data_to_file():
    with open("exam.txt", "w") as file:
        file.write(list_items(argument))
