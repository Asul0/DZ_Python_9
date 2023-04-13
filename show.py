def show_all():
   file = open('sample.txt', 'r', encoding= 'UTF-8')
   data = file.readlines()
   file.close()
   for i in data:
      print(i)
