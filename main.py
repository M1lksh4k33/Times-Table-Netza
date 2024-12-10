# ask the user for a number
num= int(input("Enter a number: "))

# initialize counter
count= 10

#multiply through the numbers from 10 to 20 with the user's number
while(count<= 20):
  print(str(count) + "*" + str(num) + "=" + str(count * num))
  count= count + 1