print("Please insert the numbers ")

data_list = []
data2 = []
while True:
    data = input()
    if data == "/":
        break
    data_list += [data]
    data2 += [data]

data2.sort()

if(data2==data_list):
     print("The Arry Is Sorted")  
else:
      print("The Arry Is Not Sorted")  




