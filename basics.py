# j = 50
# k = 5
# print (j + k)
# if j > 25:
#     print "j is the winner"
#
# listA = ["mother", "father", "1970", "1965"]
# print (listA[3])
#
# tupA = ("brother", "sister", "1990", "1992", "1993", "1995")
# print (tupA[1:4])

# mylist =[1,2,2,3,3,3,4,4,4,4,5,5,5,5,5,6,6,6,6,6,6]
# print set(mylist)

string = raw_input("Enter your string.\n")
newstr = ""
for l in range (0, len(string)):
    if l == 0:
        newstr += string[l].upper()
    elif string[l - 1] == " ":
        newstr += string[l].upper()
    else:
        newstr += string[l]
print newstr
