import file
def search_in_file(path,category,element):
    text=file.read_file(path).split('\n')
    for i in text:
        list = i.split(";")
        if (list[category]==element):
            return list
    return []

def search_in_text(text,arg,category):
    for i in text:
        i=str(i).split(";")
        if i[category]==arg:
            print(*i)
            break
    else:
        print("Элемент отсутствует")

def create_new_line(id,city,region,district,population,foundation):
    line = [id + ";",city + ";",region + ";",district + ";",population + ";",foundation + "\n"]
    return line