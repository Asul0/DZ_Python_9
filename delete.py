def delete_contact():
   find_string = input("Введите поисковой запрос: ")
   file = open('sample.txt', 'r', encoding='UTF-8')
   data = file.readlines()
   data_new = []
   for data_str in data:
      if find_string not in data_str:
            data_new.append(data_str)
   file.close()
   file = open('sample.txt', 'w', encoding='UTF-8')
   file.writelines(data_new)
   file.close()
