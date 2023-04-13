from menu import main_menu
from show import show_all
from add import add_contact
from edit import edit_contact
from find import find_contact
from delete import delete_contact


if __name__ == "__main__":
   main_menu()

   while True:
      choose =  int(input("Введите пункт меню: "))
      if choose == 1:
            show_all()
      if choose == 2:
            add_contact()
      if choose == 3:
            edit_contact()
      if choose == 4:
            find_contact()
      if choose == 5:
            delete_contact()
      if choose == 6:
            break
