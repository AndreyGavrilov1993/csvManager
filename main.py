import os
import file
import list_function
import ui
def main():
    os.system('cls')
    ui.show_menu()
    try:
        choice=ui.choice_menu()
        print(choice)
        if choice==7:
            ui.show_data(file.read_file('data.csv'))
        elif choice==2:
            category=ui.show_category('data.csv')
            element=input("введите значение для поиска: ")
            list = list_function.search_in_file('data.csv', category, element)
            ui.show_list(list)
            input()
            main()

        # elif choice==4:
        #     id=input("Введите Id города: ")
        #     city=input("Введите название города: ")
        #     region=input("Введите регион города: ")
        #     district=("Введите округ города: ")
        #     population=("Введите население города: ")
        #     foundation=("Введите дату основания города: ")
        #     file.write_down('data.csv',list_function.create_new_line(id,city,region,district,population,foundation))
        #     print("Файл изменён")
        #     input()

        elif choice==4:
            list = ui.add_element('data.csv')
            file.write_line('data.csv', list)
            print("запись завершена")
        input()
        main()

    except Exception as ex:
        print(str(ex))
        input()
        main()


main()

