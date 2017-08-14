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

# string = raw_input("Enter your string.\n")
# newstr = ""
# for l in range (0, len(string)):
#     if l == 0:
#         newstr += string[l].upper()
#     elif string[l - 1] == " ":
#         newstr += string[l].upper()
#     else:
#         newstr += string[l]
# print newstr

# candy = raw_input("Does it like candies, precious?\n").lower()
# if candy == "yes" or candy == "y":
#     print "It likes candies, precious."
# elif candy == "no" or candy == "n":
#     print "It dasn't like candies, precious. What's wrong with its?"
# else:
#     print "It doesn't answer the question, precious. Why dasn't it answer the question?"

# import time
# for counter in range (1, 11):
#     print counter
#     time.sleep(.5)
#
# import time
# for counter in range (10, 0, -1):
#     print counter
#     time.sleep(.5)


# import time
# for count in range(4):
#     print count
#     time.sleep(.5)

# import time
# for count in range(3, -1, -1):
#     print count
#     time.sleep(.5)

# import time
# for count in range(8, 0, -2):
#     print count
#     time.sleep(.5)

# mylist = ["one", "two", "three", "four", "five"]
# mylist_len = len(mylist)
# for i in range (0, mylist_len):
#     print mylist[i]

# import time
# counter = 1
# while counter < 11:
#     print (counter)
#     time.sleep(.5)
#     counter += 1
#     time.sleep(.5)

# import time
# nums = [1, 2, 3, 4, 5, 6]
# counter = 0
# while counter < len(nums):
#     print (nums[counter])
#     counter += 1
#     time.sleep(.5)

# bands = ["The Beatles", "Rolling Stones", "Led Zeppelin", "Jimmy Hendrix"]
# str = ""
# for b in range (0, len(bands)):
#     if b != (len(bands) - 2):
#         str = str + bands[b] +", "
#     elif b == (len(bands) - 2):
#         str = str + bands[b] + "and"
# print (str)

birthdays = {"Emily": "June 1950", "Maxine": "March 1962", "Kelly": "May 1955", "Violet": "January 1948"}
print (birthdays)
print (birthdays["Maxine"])
birthdays["Emily"] = "December 1975"
print (birthdays)
birthdays["Sara"] = "November 1980"
print(birthdays)
del birthdays["Kelly"]
print (birthdays)

# def subtraction (a, b):
#     subtract = a-b
#     return subtract
#
# print(subtraction(20,10) + subtraction(20,10))

# x = 15
# print (x)
# del (x)
# print (x)
