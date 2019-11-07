import music_reports
import display
import os

    

def print_program_menu(menu):
    for option in menu:
        print(str(menu.index(option)+1) + '-' + option)

def display1():
    maxi=0
    maxq=0
    maxt=0
    maxv=0
    maxz=0
    for i,q,t,v,z in music_reports.openfile('text_albums_data.txt'):
        if len(i)>maxi:
            maxi=len(i)
        if len(q)>maxq:
            maxq=len(q)
        if len(t)>maxt:
            maxt=len(t)
        if len(v)>maxv:
            maxv=len(v)
        if len(z)>maxz:
            maxz=len(z)
    
    print((maxi+maxq+maxt+maxv+maxz+14)*'-')
    print ('|''{:^{mi}}'' |''{:^{mq}}'' | ''{:^{mt}}'' | ''{:^{mv}}'' | ''{:^{mz}}'' |' .format("Singer","Album","Year","Genre","Lenght",mi=maxi,mq=maxq,mt=maxt,mv=maxv,mz=maxz))
    print((maxi+maxq+maxt+maxv+maxz+14)*'-')
    for  i,q,t,v,z in music_reports.openfile('text_albums_data.txt'):
        print('|''{:>{mi}}'' |''{:>{mq}}'' | ''{:>{mt}}'' | ''{:>{mv}}'' | ''{:>{mz}}'' |' .format(i,q,t,v,z,mi=maxi,mq=maxq,mt=maxt,mv=maxv,mz=maxz))
    print((maxi+maxq+maxt+maxv+maxz+14)*'-')

    
    
    
def main():
    menu=['Albumlist','Choose by genre','Find all album by given timerange','Find th shortest\\longest album','All albums by given artist','Albums name']
    music_reports.openfile('text_albums_data.txt')
    print_program_menu(menu)
    
    music_reports.progressmenü()
    display1()

if __name__ == "__main__":
    main()