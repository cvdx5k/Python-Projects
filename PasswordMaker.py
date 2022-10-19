import random
# had some problems with max characters so divided into multiple lists
list1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
list2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
list3 = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
# combines list
list1.extend(list2)
list1.extend(list3)
list4 = []
# function to convert a list like above into a singular string
def listToString(list4):
    # initialize an empty string
    str1 = ""
    # traverse in the string
    for anyy in list4:
        str1 += anyy
    # return string
    return str1
# password generator
print("How long do you want your password to be?")
j = input()
c = int(j)

for i in range(c):
    list4.append(random.choice(list1))
    j = int(j) - 1
# prints the generated password
print(listToString(list4))