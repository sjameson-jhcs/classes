# *******************************
# ****** SECTION 1 - LISTS ******
# *******************************

# Lists are like variables except they can store more than one value
# They defined by using square brackets like this:
# name = [contents]

days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
prime_numbers = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
mixed_bag_of_stuff = ["blah", 4.2, False, 18]

# *******************************
# ****** SECTION 2 - Index ******
# *******************************

# Every spot in an list has a number associated with it
# The first spot in the list is given the number 0
print(days_of_the_week)
# print(days_of_the_week[0])
# print(days_of_the_week[6])

# You can use negative numbers to index from the end of a list
# print(days_of_the_week[-1])
# print(days_of_the_week[-2])

# *************************************************
# ****** SECTION 3 - Multi-Dimensional Lists ******
# *************************************************

# You can put lists inside of lists when appropriate
# Note: it is often convenient to write them on multiple lines but it is not required.
classes_grouped_by_department = [["Algebra", "Geometry"],
                                 ["Creative Writing", "British Lit."],
                                 ["Physics", "Chemistry", "Biology"]]

# To access an index in a multi-dimensional array you need to specify both indices
# print(classes_grouped_by_department[0][1])
# print(classes_grouped_by_department[2][2])

# **************************************
# ****** SECTION 4 - Dictionaries ******
# **************************************

# A dictionary is similar to a list except each index has a key with a name
# We call these key/value pairs
# They are defined with curly braces and colons between the keys/values.
# name = {"key 1": "value 1", "key 2": "value 2", etc.}

pro_football_teams = {"Chicago": "Bears", "Cincinnati": "Bengals", "Miami": "Dolphins"}
# print(pro_football_teams)
# print(pro_football_teams["Chicago"])

# ***********************************
# ****** SECTION 5 - FOR LOOPS ******
# ***********************************

# Any code inside of a loop will repeat a designated number of times
# A "For Loop" is most commonly used to loop through a list or dictionary

# Example with a list
# for day in days_of_the_week:
#     print(day)
#     if day == "Saturday":
#         print("WooHoo!")

# Example with a dictionary
# for city, mascot in pro_football_teams.items():
#     print(city)
#     print(mascot)

# Sometimes you may want a loop to repeat a known number of times
# You can use range(x) to specify a number of loops
# for i in range(10):
#     print(i)

# *************************************
# ****** SECTION 6 - WHILE LOOPS ******
# *************************************

# A "While Loop" will continue to run while a condition is true
# day_counter = 0
# while days_of_the_week[day_counter] != "Saturday":
#     print(days_of_the_week[day_counter])
#     day_counter += 1
#     if day_counter > 6:
#         break

# Notice: it is usually a good idea to add a break condition to avoid infinite loops.

# A continue will stop the current iteration of the loop and start the next one
# day_counter = 0
# while days_of_the_week[day_counter] != "Saturday":
#     if day_counter == 2:
#         day_counter += 1
#         continue
#     print(days_of_the_week[day_counter])
#     day_counter += 1

# user_command = ""
# iteration_count = 0
# while user_command != "quit":
#     user_command = input("User Command? ")
#     iteration_count += 1
#     print(f"Iteration Count = {iteration_count}")
#     if iteration_count >= 10:
#         break


# **************************************
# ****** SECTION 6 - NESTED LOOPS ******
# **************************************

# Loops can be put inside of loops. This is often useful for multi-dimesional lists
# There is a multiplicative factor for the number of times the loops will run

# courses_dictionary = {
#     "Math": ["Algebra", "Geometry", "Calculus", "Trigonometry"],
#     "English": ["Creative Writing", "British Lit."],
#     "Science": ["Physics", "Chemistry", "Biology"]
# }
#
# for department, courses in courses_dictionary.items():
#     print(f"The {department} Department has the foloowing {len(courses)} classes:")
#     for course in courses:
#         print(course)
