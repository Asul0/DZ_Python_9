def add_contact():
   file = open('sample.txt', 'a', encoding= 'UTF-8')
   data = input("Введите фамилию, телефон, коменнтарий, (разделляя ;)")
   data += '\n'
   file.write(data)
   file.close()
