import operator                                                     #Used for sorting list with multiple arguments

#Title, Author name, Publisher name, Version, Publish year, Price
bookList = [
                ["Mega Living", "Robin Sharma","Jaico",2,2018,399],
                ["The Alchemist","Paulo Coelho","Harper",5,1993,450],
                ["Animal Farm","George Orwell","Warburg",3,1945,299],
                ["The 5am club","Robin Sharma","Jaico",1,2018,350],
                ["Be Animated","Neil Ameer","Jaico",1,2010,375]
    ]

[print("~", end="") for _ in range(80)]

print("\n\n\t\t---- ---------- ------")
print("\t\tBOOK MANAGEMENT SYSTEM")
print("\t\t---- ---------- ------\n")

print("Display all details of books :\n\t1. Written by specific author\n\t2. Increasing order of price\n\t3. Published by publisher in a year\n\t4. Increasing order of author and publishing year\n")
option = int(input("What do you wish to do : "))


#Written by specific author
if(option == 1):
    authorName = input("\nEnter author name : ")
    print("\nTITLE\t\t\t\tPUBLISHER\t\tVERSION\t\t\tPUBLISHED YEAR\t\tPRICE")
    print("`````\t\t\t\t```````\t\t\t`````````\t\t````````` ````\t\t`````")
    flag = 0
    for i in range(len(bookList)):
        if(bookList[i][1].lower() == authorName.lower()):           #Convert to lowercase and compare
            flag = 1
            print(bookList[i][0]+"\t\t\t"+bookList[i][2]+"\t\t\t"+str(bookList[i][3])+"\t\t\t"+str(bookList[i][4])+"\t\t\t"+str(bookList[i][5]))
    if(flag == 0):
        print("--------------------------------------------")
        print("   Oops! No books for this author found :(  ")
        print("--------------------------------------------\n\n")
    print("\n\n\n")


#Increasing order of price
elif(option == 2):
    bookList.sort(key=lambda x: x[5])                   #Sort based on 6th column(price)
    print("\nTITLE\t\t\t\tAUTHOR\t\t\t\tPUBLISHER\t\tVERSION\t\t\tPUBLISHED YEAR\t\tPRICE")
    print("`````\t\t\t\t``````\t\t\t\t```````\t\t\t`````````\t\t````````` ````\t\t`````")
    for i in range(len(bookList)):
        print(bookList[i][0]+"\t\t\t"+bookList[i][1]+"\t\t\t"+bookList[i][2]+"\t\t\t"+str(bookList[i][3])+"\t\t\t"+str(bookList[i][4])+"\t\t\t"+str(bookList[i][5]))
    print("\n\n\n")



elif(option == 3):
    publisherName = input("\nEnter publisher name : ")
    publishedYear = int(input("\nEnter published year : "))
    print("\nTITLE\t\t\tAUTHOR\t\t\t\tVERSION\t\t\tPRICE")
    print("`````\t\t\t``````\t\t\t\t```````\t\t\t`````")
    flag = 0
    for i in range(len(bookList)):
        if((bookList[i][4] == publishedYear) and (bookList[i][2].lower() == publisherName.lower()) ):
            flag = 1
            print(bookList[i][0]+"\t\t"+bookList[i][1]+"\t\t\t"+str(bookList[i][3])+"\t\t\t"+str(bookList[i][5]))
    if(flag == 0):
        print("--------------------------------------------------------------")
        print("   Oops! No books by this publisher for given year found :(   ")
        print("--------------------------------------------------------------")
    print("\n\n\n")



elif(option == 4):
    bookList.sort(key=operator.itemgetter(1,4))                      #Sort based on 2nd and 5th column
    print("\nTITLE\t\t\t\tAUTHOR\t\t\t\tPUBLISHER\t\tVERSION\t\t\tPUBLISHED YEAR\t\tPRICE")
    print("`````\t\t\t\t``````\t\t\t\t```````\t\t\t`````````\t\t````````` ````\t\t`````")
    for i in range(len(bookList)):
        print(bookList[i][0]+"\t\t\t"+bookList[i][1]+"\t\t\t"+bookList[i][2]+"\t\t\t"+str(bookList[i][3])+"\t\t\t"+str(bookList[i][4])+"\t\t\t"+str(bookList[i][5]))
    print("\n\n\n")
else:
        print("--------------------------------------------")
        print("   Oops! INVALID INPUT :(  ")
        print("--------------------------------------------\n\n")
        print("\n\n\n")