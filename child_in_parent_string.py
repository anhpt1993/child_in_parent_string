def input_string(text):
    return input(text)

def check_index(child, parent):
    return parent.find(child)
    
if __name__ == '__main__':
    my_str1 = input_string("Input parent string here: ")
    my_str2 = input_string("Input child string here: ")

    result = check_index(child = my_str2, parent = my_str1)

    if result == -1:
        print(f"Sub string '{my_str2}' is not in '{my_str1}'")
    else:
        print(f"Sub string '{my_str2}' found at index: {result + 1}")