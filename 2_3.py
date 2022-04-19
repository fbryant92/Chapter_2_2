# print("one", "two", "three", sep=", ")
# print("Hello", end=" ")
# print("World!")
# print("a\tb\tc")
# print("a\tb\tc\nd\te\tf")
# print("\"Hello World!\"") # "Hello World!"
# str1 = "There are {0}% probability that the stock market will crash tomorrow and {1}% probability that it will rally!"
# print(str1.format(10, 50))

# print("{0:^5s}{1:<20s}{2:>3s}".format("Rank", "Player", "HR"))
# print("{0:^5n}{1:<20s}{2:>3n}".format(1, "Barry Bonds", 762))


# str2 = "Of the total U.S. population, {1:.2%} resides in {0:s}. "
# print(str2.format ("Texas", 26448000/309000000))
# grades = []
# grades.append(1)
# grades.append(2)
# grades.append(4)
# grades.append(9)

# print("grades", grades)

# length = len(grades) #
# print("length", length)
# print("sliced:", grades[0:2])
str1 = "a,b,c"
parts = str1.split(",")

print("parts:", parts)

lines = ["To", "be", "or", "not", "to", "be"]

print("lines before join:", lines)

joined = " ".join(lines)

print("joined:", joined)