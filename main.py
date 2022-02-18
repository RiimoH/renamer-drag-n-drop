import sys
from time import sleep
from pathlib import Path
import rename

def printr(path_dict):
    for k, v in path_dict.items():
        print(k.name, '-->', v.name)

def get_instructions():
    print("""options:
1 = append a string -> 1 test = appends test to filename
2 = insert a string -> 2 test = inserts test before the filename
3 = replace a string -> 3 test data = replaces test with data in filename
4 = switch places in string -> 4 2 1 = switches the first and second thingy, can also be used to cut stuff out.
e = execute renaming""")
    inp = input("Enter input here >>> ")
    if not inp:
        quit()
    elif inp.lower() == 'e':
        return 0, None
    else:
        inp = inp.split(' ')
        return (int(inp[0]), *inp[1:])

functions = {
    1: rename.append,
    2: rename.insert,
    3: rename.replace,
    4: rename.switch,
    }

if __name__ == '__main__':
    dropped_files = map(lambda x: Path(x), sys.argv[1:])
        
    path_dict = {old: old for old in dropped_files}

    while True:
        printr(path_dict)
        instr, *args = get_instructions()

        if instr == 0:
            for k, v in path_dict.items():
                rename.execute(k, v)
            print("Renaming done.")
            break
        
        for k, v in path_dict.items():
            path_dict[k] = functions[instr](v, *args)



    







