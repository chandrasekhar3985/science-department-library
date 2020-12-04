import json
import os
import sys
import pygame


class Library:
    def __init__(self, books_dict, lend_dict, students_list):
        self.books = books_dict
        self.lend = lend_dict
        self.list = students_list

    @staticmethod
    def displayBooks():
        print(f"Books available in Prasad library are {prasad.books}")

    def addBooks(self, name_b, name_n):
        getoutput()
        books = list(prasad.books.keys())
        try:
            l = list(prasad.lend[name_b])
        except Exception as e:
            l = []

        if name_b in books:
            c1 = int(len(l))
            c2 = prasad.books[name_b]
            c1 = c1 + c2
            print(c1)

            if (c1 + name_n) < 11:

                h = prasad.books.get[name_b]
                h = h + name_n
                prasad.books.get[name_b] = h
                with open('books_lib.json', 'w') as f:
                    json.dump(prasad.books, f, indent=4, separators=(",", ":"))
            elif c1 == 10:
                print(f"For this {name_b} book Library has full capacity, Submit this to Administration ")
            elif (c1 + name_n) >= 11:
                c4 = 10 - c1
                print(f"Following {name_b} added in {c4} numbers to achieve its full capacity")
                print(f"Rest {name_b} books {name_n - c4} submitted to Administration")
                h = prasad.books[name_b]
                h = h + c4
                prasad.books[name_b] = h
                with open('books_lib.json', 'w') as f:
                    json.dump(prasad.books, f, indent=4, separators=(",", ":"))
        else:
            if name_n < 11:
                print(f"The book {name_b} in {name_n} added to the library")
                new_dict_1 = {name_b: name_n}
                prasad.books.update(new_dict_1)
                with open('books_lib.json', 'w') as f:
                    json.dump(prasad.books, f, indent=4, separators=(",", ":"))
            else:
                c5 = name_n - 10
                new_dict_1 = {name_b: 10}
                prasad.books.update(new_dict_1)
                with open('books_lib.json', 'w') as f:
                    json.dump(prasad.books, f, indent=4, separators=(",", ":"))
                print(f"The Book {name_b} in 10 numbers added to library and {c5} returned to admin")

    def lendBooks(self, name_s, name_b):
        getoutput()
        books = list(prasad.books.keys())
        if name_b in books:
            try:  # check name of the book present in book library
                l = list(prasad.lend[name_b])
            except Exception as e:
                l = []
            if name_s not in l:  # check name of the student in present in lending book list
                if prasad.books[name_b] >= 1:
                    print(f"{name_b} has been given to {name_s}.")
                    z = prasad.books[name_b]
                    z = z - 1
                    prasad.books[name_b] = z
                    with open('books_lib.json', 'w') as f:
                        json.dump(prasad.books, f, indent=4, separators=(",", ":"))
                    try:
                        l = list(prasad.lend[name_b])
                        l.append(name_s)
                        new_dic = {name_b: l}
                        prasad.lend.update(new_dic)
                        with open('lend_lib.json', 'w') as f:
                            json.dump(prasad.lend, f, indent=4, separators=(",", ":"))

                    except Exception as e:
                        l3 = []
                        l3.append(name_s)
                        new_dic_1 = {name_b: l3}
                        prasad.lend.update(new_dic_1)
                    with open('lend_lib.json', 'w') as f:
                        json.dump(prasad.lend, f, indent=4, separators=(",", ":"))

                else:
                    print(f"Sorry, {name_b} is not in stuck")
                    print("Books are with {}".format(l))
                    print("Request Them To Return So that it will be available to you")
            else:
                print(f"You already Posses {name_b}, Please Return it.")
        else:
            print(f"The Requested book is not in Library \n Contact Administration")

    def returnBooks(self, name_s, name_b):
        getoutput()
        n = list(prasad.lend.keys())
        if name_b in n:
            try:  # check name of the book present in book library
                p = list(prasad.lend[name_b])
            except Exception as e:
                p = []
            if name_s in p:
                print(f"Thank You, Book {name_b} well received, visit Again")
                z = prasad.books[name_b]
                z = z + 1
                prasad.books[name_b] = z
                with open('books_lib.json', 'w') as f:
                    json.dump(prasad.books, f, indent=4, separators=(",", ":"))
                l = list(prasad.lend[name_b])
                l1 = name_s
                l.remove(l1)
                new_dic = {name_b: l}
                prasad.lend.update(new_dic)
                with open('lend_lib.json', 'w') as f:
                    json.dump(prasad.lend, f, indent=4, separators=(",", ":"))
            else:
                print(f"This {name_b} book is not belong to this Library")
        else:
            print(f"Such {name_b} has not been lend to any one. Check again")

    def delBooks(self, name_b):
        getoutput()
        books = list(prasad.books.keys())
        if name_b in books:
            del prasad.books[name_b]
            try:
                del prasad.lend[name_b]
            except Exception as e:
                pass
            with open('books_lib.json', 'w') as f:
                json.dump(prasad.books, f, indent=4, separators=(",", ":"))
            with open('lend_lib.json', 'w') as f:
                json.dump(prasad.lend, f, indent=4, separators=(",", ":"))
        else:
            print(f" Such book {name_b} is not in Library Database")

    def addStudents(self, name_s):
        getoutput()
        l = prasad.list
        if name_s not in l:
            l.append(name_s)
            with open('students_lib.json', 'w') as f:
                json.dump(prasad.list, f, indent=4, separators=(",", ":"))
            print(f"Student {name_s} added to Database")
        else:
            print(f"Student {name_s} already exists in database.")


def initial():
    prasad = Library({"PHYSICS": 8, "CHEMISTRY": 5, "BIOLOGY": 5, "MATH": 5},
                     {"PHYSICS": ["HARRY"], "CHEMISTRY": ["RADHA"]},
                     ["HARRY", "RADHA", "SMRITI", "PANKAJ", "ARABINDA", "PHALGUNI", "PRERANA"])
    with open('books_lib.json', 'w') as f:
        json.dump(prasad.books, f, indent=4, separators=(",", ":"))
    with open('lend_lib.json', 'w') as f:
        json.dump(prasad.lend, f, indent=4, separators=(",", ":"))
    with open('students_lib.json', 'w') as f:
        json.dump(prasad.list, f, indent=4, separators=(",", ":"))


def getoutput():
    with open('lend_lib.json', 'r') as f:
        l1 = json.load(f)
    with open('books_lib.json', 'r') as f:
        b1 = json.load(f)
    with open('students_lib.json', 'r') as f:
        k1 = json.load(f)
    prasad = Library(b1, l1, k1)


with open('lend_lib.json', 'r') as f:
    l1 = json.load(f)
with open('books_lib.json', 'r') as f:
    b1 = json.load(f)
with open('students_lib.json', 'r') as f:
    k1 = json.load(f)
prasad = Library(b1, l1, k1)


def main_lib():
    while True:

        print(" WELCOME TO PRASAD LIBRARY FOR SCIENCE DEPARTMENT ")
        print("YOU ARE WILLING TO VISIT STUDENTS DEPARTMENT OR ADMINISTRATIVE DEPARTMENT")
        print("STUDENTS DEPARTMENT DEALS WITH BORROWING AND RETURNING BOOKS FROM LIBRARY")
        print("ADMINISTATIVE DEPARTMENT DEALS WITH ADDING AND REMOVING BOOKS FROM LIBRARY AND TO RESET LIBRARY")
        x = input(
            "Enter 1. For Students department\n 2. For Administrative Department \n 3. Exit the Program\n Note: keep ready your passkey for Admin work\n : ")
        if x == "1":
            studentsDepart()
        elif x == "2":
            adminDepart()

        elif x == "3":
            exit()
        else:
            print("Invalid Choice Try Again")


def studentsDepart():
    while True:
        print("Books Only Available To lend If your Name is  Enrolled")
        print("Requested To Return Book As Soon As  Possible So that others can benefit")
        x = input(
            "Enter 1. Display available Books \n 2. To Lend A Book \n 3. To Return a Book \n 4 To Exit Students Department \n :  ")
        if x == "1":
            prasad.displayBooks()
        elif x == "2":
            name_s = input("Enter The Name Of the Student :   ")
            name_s = name_s.upper()

            if name_s in prasad.list:
                name_b = input("Please Enter The name of the Book :  ")
                name_b = name_b.upper()
                prasad.lendBooks(name_s, name_b)
            else:
                print(f"You {name_s} is not belong to Library Contact Admin")
        elif x == "3":
            name_s = input("Enter The Name Of the Student :   ")
            name_s = name_s.upper()
            if name_s in prasad.list:
                name_b = input("Please Enter The name of the Book :  ")
                name_b = name_b.upper()
                prasad.returnBooks(name_s, name_b)
            else:
                print(f"You {name_s} is not belong to Library Contact Admin")
        elif x == "4":
            break
        else:
            print(" Its a invalid Choice")


def adminDepart():
    x = input("Please Submit Valid Passkey To Enter the Department")
    if x == "abcd1234":
        while True:
            print("WELCOME TO ADMINISTRATIVE DEPARTMENT")
            print(
                "ENTER 1. TO DISPLAY AVAILABLE BOOKS \n 2. TO ADD BOOKS \n 3. TO DEL BOOKS \n 4. TO ADD NEW STUDENT \n 0. RESET THE LIBRARY \n 5. TO EXIT \n NOTE: DELETE STUDENTS ARE RESTRICTED BY ORDER PRINCEPAL")
            y = input("PLEASE ENTER A VALID OPTION :")
            if y == "1":
                prasad.displayBooks()
            elif y == "2":
                name_b = input("Please Enter The Name of the book")
                name_b = name_b.upper()
                name_n = int(input(
                    "Enter The number of books you want to add. \n Note Maximum capacity of Each book is 10, Extra book will Return to Admin \n  : "))
                prasad.addBooks(name_b, name_n)
            elif y == "3":
                print(
                    "\nCaution If you delete record of the book,\n Same is removed from Library book Record  and Students Lend Record")
                name_b = input("Please Enter The name of Book You want To Remove : ")
                name_b = name_b.upper()
                prasad.delBooks(name_b)
            elif y == "4":
                name_s = input("Please Enter The Name Of Student : ")
                name_s = name_s.upper()
                prasad.addStudents(name_s)
            elif y == "5":
                break
            elif y == "0":
                initial()
            else:
                print("Its a invalid Input")


if __name__ == "__main__":
    main_lib()

