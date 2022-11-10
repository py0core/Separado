# Written by Daniel Demidovski to separate all homework from single file to files
import sys

import keyboard
from colored import bg
import os

def welcome_text():
    print("    _____ __________  ___    ____  ___    ____  ____ \n \
      / ___// ____/ __ \/   |  / __ \/   |  / __ \/ __ \ \n \
      \__ \/ __/ / /_/ / /| | / /_/ / /| | / / / / / / / \n \
     ___/ / /___/ ____/ ___ |/ _, _/ ___ |/ /_/ / /_/ / \n \
    /____/_____/_/   /_/  |_/_/ |_/_/  |_/_____/\____/ \n \
                                                        \n \
    if u lazy like me, welcome to the club XD          \n \
    -----------------------------------------          ")

def cmdLineCleaner():
    keyboard.press('ESC')
    keyboard.release('ESC')
def slicer(file_path, start, end):
    file = open(file_path, 'r')
    all_lines = file.readlines()
    file.close()
    return all_lines[start-1:end]

def slicer_full(file_path):
    file = open(file_path, 'r')
    all_lines = file.readlines()
    file.close()
    return all_lines

def create_file(name, context):
    formated_context = ''
    for i in context:
        formated_context += i
    file = open(name, 'x')
    file.write(str(formated_context))
    file.close()

def chose_file():
    path_to_file = str(sys.argv[1])
    return path_to_file

def repeater():
    cmdLineCleaner()
    path_to_file = None
    while True:
        if path_to_file is None:
            path_to_file = chose_file()
        start_line = int(input(" Please type first line: "))
        end_line = int(input(" Please type closing line: "))
        result = slicer(path_to_file, start_line, end_line)
        print(type(result))
        f_name = input(" Please type desired file name: ")
        create_file(f_name + ".py", result)
        print(f"File saved! {f_name}.py")
        quit()

def indexes(iterable, obj):
    return (index for index, elem in enumerate(iterable) if elem == obj)

def se_repeater():
    cmdLineCleaner()
    path_to_file = None
    start_line = None
    end_line = None
    counter = 0
    code_list = []
    indx = 0
    while True:
        if path_to_file is None:
            path_to_file = chose_file()
        result = slicer_full(path_to_file)
        #print(result)
        #print(''.join(result))
        for i in result:
            if i.startswith("#$"):
                if ( i[2:5] != "end"):
                    #print(i)
                    f_name = i[2:]
                    start_line = result.index(i)

                if ( i[2:5] == "end" ):
                    #print(i)
                    end_line = list(indexes(result, i))
                    print(f"Code start at {start_line} and end at {end_line[indx]}")

                    y = 0

                    for x in end_line:
                        #print(indx)
                        while start_line <= end_line[indx]:
                            #print(end_line[indx])
                            # print(result[start_line].strip())
                            code_list.append(result[start_line])
                            start_line += 1
                            # print(code_list)
                    indx += 1
                    create_file(f_name[:-1] + ".py", code_list)
                    code_list.clear()
                    print(f"File saved! {f_name[:-1]}.py")

        #


        quit()

def main():

    welcome_text()
    options_list = ['Please press the corresponding number',
                    '1 | Select start and end line method',
                    '2 | Whole file separated with special char']
    option_selected = ["1", "2"]
    print('\n'.join(options_list))
    while True:
            if keyboard.is_pressed("1"):
                option_selected = 1
                repeater()
                cmdLineCleaner()
                break
            elif keyboard.is_pressed("2"):
                option_selected = 2
                se_repeater()
                cmdLineCleaner()
                break
            elif keyboard.read_key() not in option_selected:
                cmdLineCleaner()
                os.system('cls')
                print((bg('red')) + f"\nSELECT ONLY NUMBERS FROM THE LIST. {keyboard.read_key()} is not in the list.\n" + (bg('black')))
                return main()



# programStartHere

main()