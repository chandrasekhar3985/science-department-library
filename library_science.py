import json
import os
import pygame
from pygame import mixer
import random
import threading
import sys



os.chdir("/Users/chandrasekhar/chandrasekhar_git/Science_dept_lib")
os.system("clear")

songs = ("ddnews.ogg", "malgudi.ogg", "milesur.ogg", "radio.ogg", "sare.ogg", "surabhi.ogg", "terimitti.ogg", "vande.ogg")
pygame.mixer.init()
pygame.display.init()

def music_back():
    global songs
    list = random.choice(songs)
    mixer.music.load(list)
    mixer.music.set_volume(0.5)
    mixer.music.play()
    list = random.choice(songs)
    mixer.music.queue(list)
    pygame.mixer.music.set_endevent(pygame.USEREVENT)
    mixer.music.play()

    while True:
        x = input()
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                if len(songs) > 0:
                    list = random.choice(songs)
                    pygame.mixer.music.queue(list)




class Library:
    def __init__(self, books_dict, lend_dict, students_list):
        self.books = books_dict
        self.lend = lend_dict
        self.list = students_list

    @staticmethod
    def displayBooks():
        with open('books_lib.json', 'r') as read1:
            b1 = json.load(read1)
        b2 = json.dumps(b1, indent=4, separators=(",",":"))
        print(f"\u001b[34mBooks available in Prasad library are :\u001b[32m{b2}\u001b[0m")


    @staticmethod
    def displaystudents():
        with open('students_lib.json', 'r') as read2:
            s1 = json.load(read2)
        s2 = json.dumps(s1, indent=4, separators=(",", ":"))
        print(f"\u001b[34mStudents Enrolled For Library are : \u001b[32m{s2}\u001b[0m")

    @staticmethod
    def displayborrow():
        with open('lend_lib.json', 'r') as read3:
            p1 = json.load(read3)
        p2 = json.dumps(p1, indent=4, separators=(",", ":"))
        print(f"\u001b[34mBooks are Borrowed By Following Students : \u001b[31m{p2}\u001b[0m")
        pass

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
                print(f"\u001b[31mFor this {name_b} book Library has full capacity, Submit this to Administration ")
            elif (c1 + name_n) >= 11:
                c4 = 10 - c1
                print(f"\u001b[32;1mFollowing {name_b} added in {c4} numbers to achieve its full capacity")
                print(f"\u001b[32;1mRest {name_b} books {name_n - c4} submitted to Administration")
                h = prasad.books[name_b]
                h = h + c4
                prasad.books[name_b] = h
                with open('books_lib.json', 'w') as f:
                    json.dump(prasad.books, f, indent=4, separators=(",", ":"))
        else:
            if name_n < 11:
                print(f"\u001b[32;1mThe book {name_b} in {name_n} added to the library")
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
                print(f"\u001b[32;1mThe Book {name_b} in 10 numbers added to library and {c5} returned to admin")

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
                    print("\u001b[31mRequest Them To Return So that it will be available to you")
            else:
                print(f"\u001b[31mYou already Posses {name_b}, Please Return it.")
        else:
            print(f"\u001b[31mThe Requested book is not in Library \n Contact Administration")

    def returnBooks(self, name_s, name_b):
        getoutput()
        n = list(prasad.lend.keys())
        if name_b in n:
            try:  # check name of the book present in book library
                p = list(prasad.lend[name_b])
            except Exception as e:
                p = []
            if name_s in p:
                print(f"\u001b[32;1mThank You, Book {name_b} well received, visit Again")
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
                print(f"\u001b[31mThis {name_b} book is not belong to this Library")
        else:
            print(f"\u001b[31mSuch {name_b} has not been lend to any one. Check again")

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
            print(f" \u001b[31mSuch book {name_b} is not in Library Database")

    def addStudents(self, name_s):
        getoutput()
        l = prasad.list
        if name_s not in l:
            l.append(name_s)
            with open('students_lib.json', 'w') as f:
                json.dump(prasad.list, f, indent=4, separators=(",", ":"))
            print(f"Student {name_s} added to Database")
        else:
            print(f"\u001b[31mStudent {name_s} already exists in database.")


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

        print(" \n\u001b[31m*******WELCOME TO PRASAD LIBRARY FOR SCIENCE DEPARTMENT******\n ")
        print("\u001b[34;1mYOU ARE WILLING TO VISIT STUDENTS DEPARTMENT OR ADMINISTRATIVE DEPARTMENT\n")
        print("\n\u001b[35;1mSTUDENTS DEPARTMENT DEALS WITH BORROWING AND RETURNING BOOKS FROM LIBRARY\n")
        print("\n\u001b[36;1mADMINISTRATIVE DEPARTMENT DEALS WITH ADDING AND REMOVING BOOKS FROM LIBRARY")
        print("\u001b[36;1mTO RESET LIBRARY  AND TO ADD STUDENTS\n")
        print("\n\u001b[34mEnter 1. For Students department\n\u001b[35m      2. For Administrative Department ")
        print("\u001b[36m      3. Exit the Program\n\u001b[34;1m    Note: keep ready your passkey for Admin work\n")
        print("     \u001b[43m\u001b[37m4. Pause the music\u001b[0m \n     \u001b[43m\u001b[37m5. Resume The music\u001b[0m")
        x = input("\u001b[35;1m    Please Enter a Valid option : \u001b[0m")
        if x == "1":
            studentsDepart()
        elif x == "2":
            adminDepart()

        elif x == "3":
            exit()

        elif x == "4":
            mixer.music.pause()
        elif x == "5":
            mixer.music.unpause()
        else:
            print("\u001b[31mInvalid Choice Try Again")




def studentsDepart():

    while True:
        print("\n\u001b[31m=======Books Only Available To lend If your Name is  Enrolled========\n")
        print("\n\u001b[36;1mRequested To Return Book As Soon As  Possible So that others can benefit\n")
        print("\n\u001b[34;1mENTER 1. DISPLAY AVAILABLE BOOKS \n\u001b[35;1m      2. TO LEND A BOOK \n\u001b[36;1m      3. TO RETURN A  BOOK ")
        print("\u001b[34m      4. TO DISPLAY NAME OF STUDENTS ENROLLED TO LIBRARY")
        print("\u001b[35m      5. TO DISPLAY BOOKS BORROWED BY STUDENTS \n\u001b[36m      6.TO EXIT STUDENTS DEPARTMENT \n")
        print("     \u001b[43m\u001b[37m7. Pause the music\u001b[0m \n     \u001b[43m\u001b[37m8. Resume The music\u001b[0m")

        x = input("\u001b[34;1mPlease Enter a Valid Option :  ")
        if x == "1":
            prasad.displayBooks()
        elif x == "2":
            name_s = input("\u001b[34mEnter The Name Of the Student :   ")
            name_s = name_s.upper()

            if name_s in prasad.list:
                name_b = input("\u001b[35mPlease Enter The name of the Book :  ")
                name_b = name_b.upper()
                prasad.lendBooks(name_s, name_b)
            else:
                print(f"\u001b[31mYou {name_s} is not belong to Library Contact Admin")
        elif x == "3":
            name_s = input("\u001b[36mEnter The Name Of the Student :   ")
            name_s = name_s.upper()
            if name_s in prasad.list:
                name_b = input("\u001b[34mPlease Enter The name of the Book :  ")
                name_b = name_b.upper()
                prasad.returnBooks(name_s, name_b)
            else:
                print(f"\u001b[31mYou {name_s} is not belong to Library Contact Admin")
        elif x == "4":
            prasad.displaystudents()
        elif x == "5":
            prasad.displayborrow()
        elif x == "6":
            break
        elif x == "7":
            mixer.music.pause()
        elif x == "8":
            mixer.music.unpause()
        else:
            print("\u001b[31m Its a invalid Choice")


def adminDepart():

    x = input("\u001b[35m Please Submit Valid Passkey To Enter the Department  :  ")
    if x == "abcd1234":
        while True:
            print("\n\u001b[31m#####WELCOME TO ADMINISTRATIVE DEPARTMENT####\n")
            print("\n\u001b[36mENTER 1. TO DISPLAY AVAILABLE BOOKS \n\u001b[34m      2. TO ADD BOOKS")
            print("\u001b[35m      3. TO DEL BOOKS \n\u001b[36m      4. TO ADD NEW STUDENT \n\u001b[34m      0. RESET THE LIBRARY TO DEFAULT")
            print("\u001b[35m      5. TO DISPLAY NAME OF STUDENTS ENROLLED TO LIBRARY")
            print("\u001b[36m      6. TO DISPLAY BOOKS BORROWED BY STUDENTS")
            print("\u001b[34m      7. TO EXIT \n\u001b[31m        NOTE: DELETE STUDENTS ARE RESTRICTED BY ORDER PRINCIPAL")
            print("      \u001b[43m\u001b[37m8. Pause the music\u001b[0m \n      \u001b[43m\u001b[37m9. Resume The music\u001b[0m")
            y = input("\u001b[34mPLEASE ENTER A VALID OPTION :  ")
            if y == "1":
                prasad.displayBooks()
            elif y == "2":
                name_b = input("\u001b[36mPlease Enter The Name of the book")
                name_b = name_b.upper()
                name_n = int(input(
                    "\u001b[32;1mEnter The number of books you want to add. \n Note Maximum capacity of Each book is 10, Extra book will Return to Admin \n  : "))
                prasad.addBooks(name_b, name_n)
            elif y == "3":
                print(
                    "\n\u001b[31mCaution If you delete record of the book,\n Same is removed from Library book Record  and Students Lend Record")
                name_b = input("\u001b[36mPlease Enter The name of Book You want To Remove : ")
                name_b = name_b.upper()
                prasad.delBooks(name_b)
            elif y == "4":
                name_s = input("\u001b[36mPlease Enter The Name Of Student : ")
                name_s = name_s.upper()
                prasad.addStudents(name_s)
            elif y == "5":
                prasad.displaystudents()
            elif y == "6":
                prasad.displayborrow()
            elif y == "7":
                break
            elif y == "8":
                pygame.mixer.music.pause()
            elif y == "9":
                pygame.mixer.music.unpause()
            elif y == "0":
                initial()
            else:
                print("\u001b[31mIts a invalid Input")


def main():
    thread1 = threading.Thread(target=main_lib)
    thread1.start()

    thread2 = threading.Thread(target=music_back)
    thread2.start()
    thread1.join()
    thread2.join()


if __name__ == "__main__":
    main()




