# ------------------------------------------------- #
# Title: Lab7-1
# Description: Create a new script that demonstrates how Pickling and Structured error handling work
# ChangeLog: (Who, When, What)
# MSumnicht,2022.02.27,Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []
lstAllCustomers = []


# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_lists):
    objFile = open(file_name, "wb")
    pickle.dump(list_of_lists, objFile)
    objFile.close()


def read_data_from_file(file_name):
    objFileData = []

    try:
        objFile = open(file_name, "rb")
        objFileData = pickle.load(objFile)  # load() only loads one row of data.
    except FileNotFoundError:
        objFile = open(file_name, "wb")

    objFile.close()

    print(objFileData)


# Presentation ------------------------------------ #
# Get ID and NAME From user, then store it in a list object

read_data_from_file(strFileName)

while True:
    print("* Menu of Options *\n"
          "     1) Add a customer\n"
          "     2) Save the file\n"
          "     3) Display current file\n"
          "     4) Exit\n")

    choice = input("Please select an option: ")
    if choice == "1":
        try:
            intId = int(input("Enter an Id: "))
        except TypeError:
            print("Please enter a number.")
        strName = str(input("Enter a Name: "))
        lstCustomer = [intId, strName]
        lstAllCustomers.append(lstCustomer)

        for row in lstAllCustomers:
            print(str(row[0]) + "," + row[1])
    elif choice == "2":
        save_data_to_file(strFileName, lstAllCustomers)
        print(lstAllCustomers)
    elif choice == "3":
        print(read_data_from_file(strFileName))
    elif choice =="4":
        break
    else:
        print("Please select a valid option")
