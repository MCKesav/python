a = input("Enter the word ")
b = len(a)
if (a[-3:] == "ing"):
  print(a.replace("ing","ly"))
elif (b >= 3):  print(a + "ing")
else:
  print("")
