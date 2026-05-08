#!/usr/bin/env python
# coding: utf-8

# # Activity: Debug Python Code

# ## Introduction
# 
# One of the biggest challenges faced by analysts is ensuring that automated processes run smoothly. Debugging is an important practice that security analysts incorporate in their work to identify errors in code and resolve them so that the code achieves the desired outcome. 
# 
# Through a series of tasks in this lab, you'll develop and apply your debugging skills in Python.

# <details><summary><h2>Tips for completing this lab</h2></summary>
# 
# As you navigate this lab, keep the following tips in mind:
# 
# - `### YOUR CODE HERE ###` indicates where you should write code. Be sure to replace this with your own code before running the code cell.
# - Feel free to open the hints for additional guidance as you work on each task. 
# - To enter your answer to a question, double-click the markdown cell to edit. Be sure to replace the "[Double-click to enter your responses here.]" with your own answer.
# - You can save your work manually by clicking File and then Save in the menu bar at the top of the notebook. 
# - You can download your work locally by clicking File and then Download and then specifying your preferred file format in the menu bar at the top of the notebook. 
# </details>

# ## Scenario
# 
# In your work as a security analyst, you need to apply debugging strategies to ensure your code works properly.
# 
# Throughout this lab, you'll work with code that is similar to what you've written before, but now it has some errors that need to be fixed. You'll need to read code cells, run them, identify the errors, and adjust the code to resolve the errors.

# ## Task 1
# 
# The following code cell contains a syntax error. In this task, you'll run the code, identify why the error is occuring, and modify the code to resolve it. (To ensure that it has been resolved, run the code again to check if it now functions properly.)

# In[2]:


# For loop that iterates over a range of numbers
# and displays a message each iteration

for i in range(10):
    print("Connection cannot be established")


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# The header of a `for` loop in Python requires specific punctuation at the end. 
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# The header of a `for` loop in Python requires a colon (`:`) at the end.  
# 
# </details>

# #### **Question 1**
# **What happens when you run the code before modifying it? How can you fix this?**

# Before modifying the code, running the cell results in a SyntaxError. Python indicates that there is invalid syntax at the end of the for loop header. This prevents the code from executing at all because the structure of the loop is incomplete.
# 
# How can you fix this?
# To fix the error, you need to add a colon (:) to the end of the for loop header.
# 
# The corrected code should look like this:
# 
# 
# for i in range(10):
#     print("Connection cannot be established")

# ## Task 2
# In the following code cell, you're provided a list of usernames. There is an issue with the syntax. In this task, you'll run the cell, observe what happens, and modify the code to fix the issue.

# In[4]:


# Assign `usernames_list` to a list of usernames

usernames_list = ["djames", "jpark", "tbailey", "zdutchma ","esmith", "srobinso", "dcoleman", "fbautist"]

# Display `usernames_list`

print(usernames_list)


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Each element in `usernames_list` is a username and should be a string. In Python, a string should have quotation marks around it.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# When creating a list in Python, the elements of the list should be separated with commas. There should be a comma between every two consecutive elements. 
# 
# </details>

# #### **Question 2**
# **What happens when you run the code before modifying it? How can you fix it?**

# For Question 2 in your Coursera activity, here is the breakdown of the error and the solution:
# 
# What happens when you run the code?
# Before modifying the code, running the cell results in a SyntaxError. This happens because the list elements are not properly separated. Specifically, the username "zdutchma" is missing a closing quotation mark, and there are missing commas between several strings in the list. Python cannot parse where one string ends and the next begins.
# 
# How can you fix it?
# To fix the error, you need to ensure two things for every item in the usernames_list:
# 
# Each username must be enclosed in opening and closing quotation marks (e.g., "username").
# 
# Each item in the list must be separated by a comma.
# 
# The corrected code should look like this:
# 
# usernames_list = ["djames", "jpark", "tbailey", "zdutchma", "esmith", "srobinso", "dcoleman", "fbautist"]
# 
# print(usernames_list)

# ## Task 3
# In the following code cell, there is a syntax error. Your task is to run the cell, identify what is causing the error, and fix it.

# In[6]:


# Display a message in upper case 

print("update needed".upper())


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Calling a function in Python requires both opening and closing parantheses. 
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# In the code above, check that each function call has both opening and closing parantheses. 
# 
# </details>

# #### **Question 3**
# **What happens when you run the code before modifying it? What is causing the syntax error? How can you fix it?**

# The Error
# Running the code results in a SyntaxError due to unbalanced parentheses. The print() function is missing its closing parenthesis.
# 
# The Fix
# Add a closing parenthesis ) at the end of the line.
# 
# Corrected Code:
# 
# print("update needed".upper())

# ## Task 4
# In the following code cell, you're provided a `usernames_list`, a `username`, and code that determines whether the username is approved. There are two syntax errors and one exception. Your task is to find them and fix the code. A helpful debugging strategy is to focus on one error at a time and run the code after fixing each one.

# In[11]:


# Assign `usernames_list` to a list of usernames that represent approved users

usernames_list = ["djames", "jpark", "tbailey", "zdutchma", "esmith", "srobinso", "dcoleman", "fbautist"]

# Assign `username` to a specific username 

username = "esmith"

# For loop that iterates over the elements of `usernames_list` and determines whether each element corresponds to an approved user

for name in usernames_list:

    # Check if `name` matches `username` 
    # If it does match, then display a message accordingly 

    if name == username:
        print("The user is an approved user")


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# In Python, the `=` assignment operator allows you to assign or reassign a variable to a value, and the `==` comparison operator allows you to compare one value to another (or the value of one variable to the value of another). 
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Indentation is important in Python syntax. Check that the indentation inside the `for` loop and the indentation inside the `if` statement are correct.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Check that each time a variable is used, it's spelled in the same way it was spelled when it was assigned.
# 
# </details>

# #### **Question 4**
# **What happens when you run the code before modifying it? What is causing the errors? How can you fix it?**

# The Errors
# Variable Typo: username_list was used instead of the correct usernames_list.
# 
# Comparison Error: A single = (assignment) was used instead of == (comparison).
# 
# Indentation: The print statement was not properly nested inside the if block.
# 
# The Fixed Code
# usernames_list = ["djames", "jpark", "tbailey", "zdutchma", "esmith", "srobinso", "dcoleman", "fbautist"]
# username = "esmith"
# 
# for name in usernames_list:
#     if name == username:
#         print("The user is an approved user")

# ## Task 5
# 
# In this task, you'll examine the following code and identify the type of error that occurs. Then, you'll adjust the code to fix the error.

# In[13]:


# Assign `usernames_list` to a list of usernames

usernames_list = ["elarson", "bmoreno", "tshah", "sgilmore", "eraab"]

# Assign `username` to a specific username

username = "eraab"

# Determine whether `username` is the final username in `usernames_list` 
# If it is, then display a message accordingly 

if username == usernames_list[4]:
    print("This username is the final one in the list.")


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Recall that indexing in Python starts at `0`.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Identify how many elements there are in the `usernames_list`.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Since indexing in Python starts at `0` and the `usernames_list` contains `5` elements, identify which index value corresponds to the final element in `usernames_list`.
# 
# </details>

# #### **Question 5**
# **What happens when you run the code before modifying it? What type of error is this? How can you fix it?**

# The Error
# The code technically runs without a crash but contains a Logic Error. If the list were different (e.g., only 3 items), it would cause an IndexError. The code hardcodes index 4 to find the last item, which is risky.
# 
# The Fix
# Use index -1 to always reference the final element in a list, regardless of its length.
# 
# Corrected Code:
# 
# Python
# if username == usernames_list[-1]:
#     print("This username is the final one in

# ## Task 6
# In this task, you'll examine the following code. The code imports a text file into Python, reads its contents, and stores the contents as a list in a variable named `ip_addresses`. It then removes elements from `ip_addresses` if they are in `remove_list`. There are two errors in the code: first a syntax error and then an exception related to a string method. Your goal is to find these errors and fix them.

# In[16]:


# Assign `import_file` to the name of the text file

import_file = "allow_list.txt"

# Assign `remove_list` to a list of IP addressess that are no longer allowed to access the network 

remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# With statement that reads in the text file and stores its contents as a list in `ip_addresses` 

with open(import_file, "r") as file:
    ip_addresses = file.read()

# Convert `ip_addresses` from a string to a list

ip_addresses = ip_addresses.split()

# For loop that iterates over the elements in `remove_list`,
# checks if each element is in `ip_addresses`,
# and removes each element that corresponds to an IP address that is no longer allowed

for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# Display `ip_addresses` after the removal process

print(ip_addresses)


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# A `with` statement in Python requires a colon (`:`) at the end of the header.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# The `.split()` method in Python is used on strings to convert them to lists. To call the `.split()` method, place the string you want to split in front of the method call.
# 
# </details>

# #### **Question 6**
# **What happens when you run the code before modifying it? What is causing the errors? How can you fix them?**

# The Errors
# SyntaxError: The with statement was missing a colon (:) at the end of the line.
# 
# AttributeError: The .split() method was used incorrectly as a standalone function instead of being called on the string variable.
# 
# The Fix
# Add the colon to the with header and call .split() directly on the ip_addresses variable.
# 
# Corrected Code:
# 
# 
# with open(import_file, "r") as file:
#     ip_addresses = file.read()
# 
# ip_addresses = ip_addresses.split()

# ## Task 7
# In this final task, there are three operating systems: OS 1, OS 2, and OS 3. Each operating system needs a security patch by a specific date. The patch date for OS 1 is `"March 1st"`, the patch date for OS 2 is `"April 1st"`, and the patch date for OS 3 is `"May 1st"`. 
# 
# The following code stores one of these operating systems in a variable named `system`. Then, it uses conditionals to output the patch date for this operating system. 
# 
# However, this code has logic errors. Your goal is to assign the `system` variable to different values, run the code to examine the output, identify the error, and fix it.

# In[19]:


# Assign `system` to a specific operating system as a string

system = "OS 2"

# Assign `patch_schedule` to a list of patch dates in order of operating system

patch_schedule = ["March 1st", "April 1st", "May 1st"]

# Conditional statement that checks which operating system is stored in `system` and displays a message showing the corresponding patch date 

if system == "OS 1":
    print("Patch date:", patch_schedule[0])

elif system == "OS 2":
    print("Patch date:", patch_schedule[1])

elif system == "OS 3":
    print("Patch date:", patch_schedule[2])


# <details>
#   <summary><h4><strong>Hint 1</strong></h4></summary>
# 
# Recall that indexing in Python starts at `0`.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 2</strong></h4></summary>
# 
# Note that the patch dates in `patch_schedule` are in order of operating system. The first patch date in `patch_schedule` corresponds to OS 1, the second patch date in `patch_schedule` corresponds to OS 2, and so on.
# 
# </details>

# <details>
#   <summary><h4><strong>Hint 3</strong></h4></summary>
# 
# Since indexing in Python starts at `0` and `patch_schedule` is in order of operating system from OS 1 to OS 3, the index value `0` corresponds to the patch date for OS 1, the index value `1` corresponds to the patch date for OS 2, and so on.
# 
# </details>

# #### **Question 7**
# **What happens when you run the code before modifying it? What is causing the logic errors? How can you fix them?**

# The Error
# The code contains logic errors because the list indices in the print statements do not match the correct operating systems. Since Python uses 0-based indexing:
# 
# OS 1 should be index [0] (March 1st)
# 
# OS 2 should be index [1] (April 1st)
# 
# OS 3 should be index [2] (May 1st)
# 
# The Fixed Code
# Python
# system = "OS 2"
# patch_schedule = ["March 1st", "April 1st", "May 1st"]
# 
# if system == "OS 1":
#     print("Patch date:", patch_schedule[0]) # Fixed index to 0
# elif system == "OS 2":
#     print("Patch date:", patch_schedule[1]) # Fixed index to 1
# elif system == "OS 3":
#     print("Patch date:", patch_schedule[2]) # F

# ## Conclusion
# 
# **What are your key takeaways from this lab?**

# Syntax Precision: Python requires specific structural elements to run, such as colons (:) at the end of for, if, and with statements, as well as balanced parentheses for nested functions like print(string.upper()).
# 
# Variable Consistency: Even a small typo (like username_list vs usernames_list) will trigger a NameError. Consistent naming is critical for automation scripts.
# 
# Logical vs. Syntax Errors: Code that runs without crashing can still have logic errors. Using 0-based indexing correctly and utilizing dynamic indices like [-1] ensures the script interacts with data as intended.
# 
# Attribute Awareness: Methods like .split() must be called directly on the object they are modifying (e.g., variable.split()) rather than being treated as standalone functions.
# 
# Operator Distinction: It is essential to distinguish between the assignment operator (=) and the comparison operator (==) to ensure conditional logic works correctly.
