# Written by Daniel Demidovski to separate all homework from single file to files

def slicer(file_path, start, end):
    file = open(file_path, 'r')
    all_lines = file.readlines()
    file.close()
    return all_lines[start-1:end]

def create_file(name, context):
    formated_context = ''
    for i in context:
        formated_context += i
    file = open(name, 'x')
    file.write(str(formated_context))
    file.close()

def repeater():
    print("    _____ __________  ___    ____  ___    ____  ____ \n \
  / ___// ____/ __ \/   |  / __ \/   |  / __ \/ __ \ \n \
  \__ \/ __/ / /_/ / /| | / /_/ / /| | / / / / / / / \n \
 ___/ / /___/ ____/ ___ |/ _, _/ ___ |/ /_/ / /_/ / \n \
/____/_____/_/   /_/  |_/_/ |_/_/  |_/_____/\____/ \n \
                                                    \n \
if u lazy like me, welcome to the club XD          \n \
-----------------------------------------          ")
    path_to_file = input(" Please paste file location with extansion: ")
    while True:
        start_line = int(input(" Please type first line: "))
        end_line = int(input(" Please type closing line: "))
        result = slicer(path_to_file, start_line, end_line)
        print(type(result))
        f_name = input(" Please type desired file name: ")
        create_file(f_name + ".py", result)
        print(f"File saved! {f_name}.py")

repeater()
