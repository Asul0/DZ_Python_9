def edit_contact():
   find_string = input("Введите поисковой запрос: ")
   replace_string = input("Введите новые данные: ")
   file = open('sample.txt', 'r', encoding='UTF-8')
   data = file.readlines()
   data_new = []
   for data_str in data:
      if find_string in data_str:
            print("Найдена запись: ", data_str)
            data_new.append(replace_string + '\n')
      else:
            data_new.append(data_str)
   file.close()
   file = open('sample.txt', 'w', encoding='UTF-8')
   file.writelines(data_new)
   file.close()
