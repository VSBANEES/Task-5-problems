string = "Guvi Geeks Network Private Limited"
count = 0

for i in string:
    if i == 'a' or i == 'A' or i == 'e' or i == 'E' or i == 'i' or i == 'I' or i == 'o' or i == 'O'or i == 'u' or i == 'U':
         count+=1
         
print("The total number vowels in the string is: "+str(count))
