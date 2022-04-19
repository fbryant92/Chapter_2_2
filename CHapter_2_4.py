# num1 = 1
# num2 = 10
# num3 = 1000
# sum_of_all_numbers = num1 + num2 + num3

# print("Sum is {0:n}".format(sum_of_all_numbers))

# words = ["Test", "this", "backwards"]
# list_of_numbers = [1, 10, 1000]
# print("Words reversed is {0:s}".format(words))

# print(sum(list_of_numbers))

# print(reverse())

# grades = []
# # grades.append(1)
# # grades.append(2)
# # grades.append(4)
# # grades.append(9)

# # print("grades", grades)

# # length = len(grades) #
# # print("length", length)
# # print("sliced:", grades[0:2])
# # str1 = "a,b,c"
# # parts = str1.split(",")

# # print("parts:", parts)

# # lines = ["To", "be", "or", "not", "to", "be"]

# # print("lines before join:", lines)

# joined = " ".join(lines)

# print("joined:", joined)
# # Open up the fhe Data.txt file in read mode
# infile = open("Data.txt", "r")

# names = []
# # using the for the loop to populate the names array with names
# for line in infile:
#     names.append(line.rstrip())

# print("names:", names)
# # CLose the Data.txt file to preserve memory
# infile.close()

# names_using_list_comprehension = [line.rstrip() for line in infile]
# print("names_using_list_compresnsion: ", names_using_list_comprehension)
# infile.close()

# infile = open("Grades.txt", "r")
# for line in infile:
#     print("line:", line.rstrip())

# infile.close()

# infile = open("Grades.txt", "r")
# list_of_numbers = [eval(line) for line in infile]
# infile.close()

# list_of_names = ("Lucas", "John", "Adam")

# print("list_of_names", list_of_names)

list1 = ["A", "B", "C"]
list2 = list(list1)
list2.append("D")
print(list1)