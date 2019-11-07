import display
import os
import sys

def openfile(filename):
    listoflist=[]
    with open (filename) as lista:
        for line in lista:
            line =line.strip()
            line= line.split(',')
            listoflist.append(line)
    return listoflist

def writetotxt():
    os.system('clear')
    with open('text_albums_data.txt', 'a+') as f , open('newalbum.txt', 'w') as d:     
        singer = input("Add the singers name: ")
        album = input("Add the album name: ") 
        year = input("Add the release year: ")
        genre = input("Add the genre: ") 
        lenght = input("Add the lenght: ")
        f.write(singer + ",")
        f.write(album + ",")
        f.write(year + ",")
        f.write(genre + ",")
        f.write(lenght)
        f.write("\n")
        f.close()
        d.write(singer + ",")
        d.write(album + ",")
        d.write(year + ",")
        d.write(genre + ",")
        d.write(lenght)
        d.write("\n")
        d.close()


def addsong():
    addsong = input("To add a song to the list press 'a'!\nTo go back to menu press 'q'!\n ")
    if addsong == "a":
        writetotxt()
        os.system('clear')
        option_1()
    elif addsong == "q":
        os.system('clear')
        display.print_program_menu(menu)
        progressmenü()
    else:
        os.system('clear')
        option_1()


def option_1():
    display.display1()
    addsong()

def option_2():
    lg=[]
    for  i,q,t,g,z in openfile('text_albums_data.txt'):
        lg.append(g)
        sg=set(lg)
        lg=list(sg)
    display.print_program_menu(lg)
    spaceline()
    try:
        albumbydata(3,lg[int(input('Choose one option: '))-1])
        spaceline()
    except:
        os.system('clear')
        option_2()   
    print('press any key to go back to genres! ')
    a=input("Press 'q' to back to main menu : ")
    if a =='q':
        os.system('clear')
        display.print_program_menu(menu)
        progressmenü()
    else:
        os.system('clear')
        option_2()
    
def option_3():
    try:
        timerange(int(input('Shortest Time: ')),int(input('Longest Time: ')))
        spaceline()
    except:
        os.system('clear')
        print('You have to write integers! ')
        option_3()
    print('press any key if you want to give another range! ')
    a=input("Press 'q' to back to main menu : ")
    if a=='q':
        os.system('clear')
        display.print_program_menu(menu)
        progressmenü()
    else:
        os.system('clear')
        option_3()

def option_4():
    shortlonglist=['shortest album','longest album']
    display.print_program_menu(shortlonglist)
    spaceline()
    option=int(input('Choose from the options: '))
    spaceline()
    if option == 1:
        shortest()
        spaceline()
        print('press any key if you want to go back: ')
        a=input("Press 'q' to back to main menu : ")
        if a=='q':
            os.system('clear')
            display.print_program_menu(menu)
            progressmenü()
        else:
            os.system('clear')
            option_4()
    elif option == 2:
        longest()
        spaceline()
        print('press any key if you want to go back: ')
        a=input("Press 'q' to back to main menu : ")
        if a=='q':
            os.system('clear')
            display.print_program_menu(menu)
            progressmenü()
        else:
            os.system('clear')
            option_4()
    else:
        os.system('clear')
        option_4()

def option_5():
    li=[]
    for i,q,y,g,t in openfile('text_albums_data.txt'):
        li.append(i)
        si=set(li)
        li=list(si)
    display.print_program_menu(li)
    spaceline()
    try:
        albumbydata(0,li[int(input('Choose one option: '))-1])
        spaceline()
    except:
        os.system('clear')
        option_2() 
    print('Press any key if you want to go back! ')
    a=input("Press 'q' to back to main menu : ")
    if a =='q':
        os.system('clear')
        display.print_program_menu(menu)
        progressmenü()
    else:
        os.system('clear')
        option_5()

def option_6():       
    lq=[]
    for i,q,y,g,t in openfile('text_albums_data.txt'):
        lq.append(q)
        sq=set(lq)
        lq=list(sq)
    display.print_program_menu(lq)
    spaceline()
    try:
        albumbydata( 1 ,lq[int(input('Choose one option: '))-1])
        spaceline()
    except:
        os.system('clear')
        option_2() 
    print('Press any key if you want to go back! ')
    a=input("Press 'q' to back to main menu : ")
    if a =='q':
        os.system('clear')
        display.print_program_menu(menu)
        progressmenü()
    else:
        os.system('clear')
        option_6()

def option_7():
    print("This is the shortest Album:")
    shortest()
    spaceline()
    print("This is the longest Album:")
    longest()
    spaceline()
    print("These are the Last Releasead Albums from the Library:")
    youngest()
    spaceline()
    print("These are the First Releasead Albums from the Library:")
    oldest()
    spaceline()
    print(f"There are {howmanyalbums()} albums in the Library")
    howmanyalbums()
    spaceline()
    print("How many albums by genre:")
    howmanyalbumgivethegenres()
    spaceline()
    
    a=input("Press 'q' to back to main menu : ")
    if a =='q':
        os.system('clear')
        display.print_program_menu(menu)
        progressmenü()

def option_8():
    sys.exit()

def progressmenü():
    option=int(input('Choose from the options: '))
    os.system('clear')
    if option == 1:
        option_1() 
    elif option == 2:
        option_2()
    elif option == 3:
        option_3()
    elif option == 4:
        option_4()
    elif option == 5:
        option_5()  
    elif option == 6:
        option_6()
    elif option == 7:
        option_7()
    elif option == 8:
        option_8()
    else:
        display.print_program_menu(menu)
        progressmenü()

def albumbydata(number,data):
    albums=openfile('text_albums_data.txt')
    for album in albums:
        for dat in album:
            if dat==data and data in album[number]:
               print(*album,sep=',')
        
def timerange(mintimerange,maxtimerange):
    lt=[]
    for  i,q,y,g,t in openfile('text_albums_data.txt'):
        lt.append(t)
        for times in lt:
            wholetimes=times.split(':',1)[0]
        if mintimerange<int(wholetimes)<maxtimerange:
            print(i,q,y,g,t)
            
def longshort():
    lt=[]
    maxi=0
    mini=100
    for i,q,y,g,t in openfile('text_albums_data.txt'):
        t1=t.split(':')
        hossz='.'.join(t1)
        lt.append(float(hossz))
        for time in lt:
            if time<mini:
                mini=time
            if time>maxi:
                maxi=time
    maxi=str(maxi)
    maxi=maxi.split('.')
    maxnum=':'.join(maxi)
    mini=str(mini)
    mini=mini.split('.')
    minnum=':'.join(mini)
    return minnum,maxnum

def shortest():
    a=longshort()    
    for i,q,y,g,t in openfile('text_albums_data.txt'):
        if a[0] in t:
            print (i,q,y,g,t)

def longest():
    a=longshort()   
    for i,q,y,g,t in openfile('text_albums_data.txt'):
        if a[1] in t:
            print (i,q,y,g,t)

def oldestyoungest():
    oldestyoungest=[]
    oldest=3000
    youngest=0
    for i,q,y,g,t in openfile('text_albums_data.txt'):
        y=int(y)
        oldestyoungest.append(y)
        for years in oldestyoungest:
            if years>youngest:
                youngest=years
            if years<oldest:
                oldest=years
    return oldest,youngest

def oldest():
    oy=oldestyoungest()
    for i,q,y,g,t in openfile('text_albums_data.txt'):
        if str(oy[0]) == y:
            print(i,q,y,g,t)

def youngest():
    oy=oldestyoungest()
    for i,q,y,g,t in openfile('text_albums_data.txt'):
        if str(oy[1]) == y:
            print(i,q,y,g,t)

def howmanyalbums():
    a=len(openfile('text_albums_data.txt'))
    return a

def spaceline():
    print("-"*55)

def newline():
    print("\n")

def howmanyalbumgivethegenres():
    genres=[]
    howmany=[]
    together=0

    for i,q,y,g,t in openfile('text_albums_data.txt'):
        genres.append(g)
    for genre in genres:
        x=genres.count(genre)
        howmany.append(x)
    together=zip(genres,howmany)
    together=set(together)
    for datas in together:
        print(*datas,sep=': ')





menu=['Albumlist','Choose by genre','Find all album by given timerange','Find th shortest\\longest album','All albums by given artist','Albums name','Reports','Quit']