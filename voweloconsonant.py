ch=input()
char=ch.isalpha()
if(char==True):
  if(ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u'):
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")
