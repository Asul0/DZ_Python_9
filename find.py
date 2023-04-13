def find_contact():
   find_string = input("Введите поисковой запрос: ")
   file = open('sample.txt', 'r', encoding= 'UTF-8')
   data = file.readlines()
   for index, data_str in enumerate(data):
      if find_string in data_str:
         print("Найдена запись: ", data_str)
