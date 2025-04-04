'''Task 1: Create a Dictionary of Student Marks

Problem Statement: Write a Python program that:
1.   Creates a dictionary where student names are keys and their marks are values.
2.   Asks the user to input a student's name.
3.   Retrieves and displays the corresponding marks.
4.   If the student’s name is not found, display an appropriate message.'''

dict = {'Alice':85}

print(dict)

find = input("Enter the student's name:")

if find in dict:
    a = dict[find]
    print(f"{find}'s marks: ",a)

else:
    print('Student not found.')

'''Task 2: Demonstrate List Slicing 
Problem Statement: Write a Python program that:
1.   Creates a list of numbers from 1 to 10.
2.   Extracts the first five elements from the list.
3.   Reverses these extracted elements.
4.   Prints both the extracted list and the reversed list
'''

list = [1,2,3,4,5,6,7,8,9,10]
print('Original List: ', list)
print('Extracted First five elements: ', list[:5])
print('Reversed extracted elements: ',list[-6::-1])
