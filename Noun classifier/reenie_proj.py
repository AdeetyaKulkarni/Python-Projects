import subprocess as sp
#Undo these if says requirement unfulfilled
#sp.call('pip install textblob')
#sp.call('pip install PyPDF2')
import PyPDF2
from textblob import TextBlob
import nltk
#nltk.download('brown')
#nltk.download('punkt')
#nltk.download('averaged_perceptron_tagger')

#Create a function to display window to enter file name

#File open
pdfFile = open('pdffile.pdf','rb')

#Pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFile)

#No of pages
print(pdfReader.numPages)

pageObj = pdfReader.getPage(0)

allText = pageObj.extractText().splitlines()


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


tfile = open('textfile.txt','r')
outf = open('outp.txt','w')
allText = tfile.read().splitlines()
allTextnew = []
lno = 1
#Adding line no to each line:
for ind in range(0,len(allText)):
    allTextnew.append(str(lno) + "-- " +  allText[ind])
    lno+=1


nounlist = innermachine(allTextnew)


outlist = {}

for noun in nounlist:
    pglst = []
    for line in allTextnew:
       if(noun in line):
           pglst.append(line[0]+line[1])

    outf.write('Noun-' + str(noun) + '::Times appeared-' + str(nounlist[noun]) + '::Line Numbers-' + str(pglst) + "\n\n")


tfile.close()

pdfFile.close()



















