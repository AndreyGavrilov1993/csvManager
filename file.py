def read_file(path):
    with open(path, 'r', encoding='utf-8') as file:
       return file.read()

def read_line(path):
    with open(path, encoding='utf-8') as file:
        return file.readline()

def text_create(path):
    with open(path, encoding='utf-8') as file:
        file.readline()
        text = file.readline()
        return text

def read_line(path):
    with open(path, encoding='utf-8') as file:
        return file.readline()
def write_down(path,line):
    with open(path, 'a') as file:
        file.write('\n\n')
    file.write('Добавим данных в файл\n')
    for line in path:
        file.write(line + '\n')
    return file.read()

def write_line(path, list):
    line=""
    for i in list:
        line+=i+";"
    line=line[:-1:]
    with open(path, encoding='utf-8') as file:
        file.write("\n"+line)

