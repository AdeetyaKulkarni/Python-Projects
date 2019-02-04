import subprocess as sp
#Undo these if says requirement unfulfilled
#For pycharm
#sp.call('pip install textblob')
#sp.call('pip install PyPDF2')

#For Windows pakage install
#sp.call('py -3 -m pip install textblob')
#sp.call('py -3 -m pip install PyPDF2')

#For MacOs pakage install
#sp.call('sudo python3 -m pip install textblob')
#sp.call('sudo python3 -m pip install PyPDF2')

#nltk.download('brown')
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

from textblob import TextBlob
#import PyPDF2
#import nltk
from tkinter import *
#-----------------------------------------------------------------------------------------------------------------------



def getfile():
    filename = e1.get()
    head(filename)

def innermachine(allTextnew):
    #get list of all nouns
    nounlist = {}
    for l in allTextnew:
        lineno = l[0] + l[1]
        #nl = TextBlob(l)
        #print(nl.noun_phrases)
        words = l.split(' ')
        for word in words:
            for (w,pos) in (TextBlob(word).pos_tags):
                if pos[0] == 'N':
                    if w in nounlist:
                        nounlist[w] += 1
                    else:
                        nounlist[w] = 1



    return nounlist


def head(filename):
    filename = filename + '.txt'
    tfile = open(filename,'r')


    allText = tfile.read().splitlines()

    tfile.close()

    allTextnew = []
    lno = 1

    #Adding line no to each line:
    for ind in range(0,len(allText)):
        allTextnew.append(str(lno) + "-- " +  allText[ind])
        lno+=1

    nounlist = innermachine(allTextnew)
    tail(nounlist,allTextnew)


def tail(nounlist,allTextnew):
    outlist = {}
    outf = open('result.txt', 'w')

    for noun in nounlist:
        pglst = []
        for line in allTextnew:
           if(noun in line):
               pglst.append(line[0]+line[1])

        outf.write('Noun-' + str(noun) + '::Times appeared-' + str(nounlist[noun]) + '::Line Numbers-' + str(pglst) + "\n\n")

    outf.close()


#MAIN::
#File read
#Create a function to display window to enter file name


master = Tk()
master.title("Reenie's software")

Label(master,text='File-name').grid(row='0',column='0')
e1 = Entry(master)
e1.grid(row='0', column='1')
button = Button(master, text='Submit', width=25, command=getfile).grid(row='3',column='0')
mainloop()
















