from random import randrange
n = randrange(1000)
while True:
  v = int(input())
  if n == v:
    print ("You've won!")
    break
  print("Smaller!" if (n < v) else "Bigger!")
