from tkinter import *

master = Tk()

master.geometry("800x500")#Sets shape of GUI
master.title("Bibliography Maker Pre-Development") #Title
master.iconbitmap("Apple.ico")

#Gap between the entry widgets is 25 pixels

#FIRST LEVEL STUFF

questionForFormat = Label(master, text = "How do you want to format the bibliography? ")
questionForFormat.place(x=10,y=10)

mlaButton = Button(master, text = "MLA8")
mlaButton.place(x = 15, y = 35)

apaButton = Button(master, text = "APA")
apaButton.place(x = 65, y = 35)

#chicagoButton = Button(master, text = "Chicago")
#chicagoButton.place(x=105, y = 35)

bibSaying = Label(master, text = "Type of Bibliography: ")
bibSaying.place(x=15, y=70)

bibFormat = Label(master, text="MLA8")
bibFormat.place(x= 135, y=70)

questionForBibType = Label(master, text = "What type of bibliography do you want to make? ")
questionForBibType.place(x = 300, y = 10)

websiteButton = Button(master, text = "Website")
websiteButton.place(x = 300, y = 35)

bookButton = Button(master, text = "Book")
bookButton.place(x = 360, y = 35)

#videoButton = Button(master, text = "Video")
#videoButton.place(x = 404, y = 35)

#journalButton = Button(master, text = "Journal")
#journalButton.place(x = 450, y = 35)

typeSaying = Label(master, text = "Type of Format: ")
typeSaying.place(x = 300, y = 70)

typeFormat = Label(master, text = "Website")
typeFormat.place(x = 390, y = 70)#Check if this is a good value for x

#Format Functions
#Will need to add more funcionality to these functions
""""ADD EVERY SINGLE WIDGET TO THE CLEAR FUNCTION!!!!!"""
def clearFunction():
    #Article
    articleTitleLabel.place_forget()
    articleEntry.place_forget()
    #Author
    authorLabel.place_forget()
    authorFirstEntry.place_forget()
    authorMiddleEntry.place_forget()
    authorLastEntry.place_forget()
    websiteTitleLabel.place_forget()
    websiteTitleEntry.place_forget()
    #Publisher
    publisherLabel.place_forget()
    publisherEntry.place_forget()
    #URL
    URLLabel.place_forget()
    URLEntry.place_forget()
    #Publisher Date
    pDateLabel.place_forget()
    pmonthEntry.place_forget()
    pdayEntry.place_forget()
    pyearEntry.place_forget()
    #Accessed Date
    aDateLabel.place_forget()
    amonthEntry.place_forget()
    adayEntry.place_forget()
    ayearEntry.place_forget()
    #Book Title
    bookTitleLabel.place_forget()
    bookEntry.place_forget()
    #Book Location City
    blocationLabel.place_forget()
    blocationEntry.place_forget()
    #MLA Book Year
    mlabookpyearLabel.place_forget()
    mlabookpyearEntry.place_forget()
    #Book Location State
    statelocationEntry.place_forget()
    statelocationLabel.place_forget()



def mlaWebsitePlaceFunction():
    articleTitleLabel.place(x=15, y=125)
    articleEntry.place(x=105, y=125)
    authorLabel.place(x=15, y=150)
    authorFirstEntry.place(x=105, y=150)
    authorMiddleEntry.place(x=255, y=150)
    authorLastEntry.place(x=290, y=150)
    websiteTitleLabel.place(x=15, y=175)
    websiteTitleEntry.place(x=105, y=175)
    publisherLabel.place(x=15, y=200)
    publisherEntry.place(x=105, y=200)
    pDateLabel.place(x=15, y=225)
    pmonthEntry.place(x=105, y=225)
    pdayEntry.place(x=255, y=225)
    pyearEntry.place(x=290, y=225)
    aDateLabel.place(x=15, y=250)
    amonthEntry.place(x=105, y=250)
    adayEntry.place(x=255, y=250)
    ayearEntry.place(x=290, y=250)
    URLLabel.place(x=15, y=275)
    URLEntry.place(x=105, y=275)


def apaWebsitePlaceFunction():
    articleTitleLabel.place(x=15, y=125)
    articleEntry.place(x=105, y=125)
    authorLabel.place(x=15, y=150)
    authorFirstEntry.place(x=105, y=150)
    authorMiddleEntry.place(x=255, y=150)
    authorLastEntry.place(x=290, y=150)
    pDateLabel.place(x=15, y=175)
    pmonthEntry.place(x=105, y=175)
    pdayEntry.place(x=255, y=175)
    pyearEntry.place(x=290, y=175)
    URLLabel.place(x=15, y=200)
    URLEntry.place(x=105, y=200)

def chicagoWebsitePlaceFunction():
    articleTitleLabel.place(x=15, y=125)
    articleEntry.place(x=105, y=125)
    authorLabel.place(x=15, y=150)
    authorFirstEntry.place(x=105, y=150)
    authorMiddleEntry.place(x=255, y=150)
    authorLastEntry.place(x=290, y=150)
    websiteTitleLabel.place(x=15, y=175)
    websiteTitleEntry.place(x=105, y=175)
    pDateLabel.place(x=15, y=200)
    pmonthEntry.place(x=105, y=200)
    pdayEntry.place(x=255, y=200)
    pyearEntry.place(x=290, y=200)
    aDateLabel.place(x=15, y=250)
    amonthEntry.place(x=105, y=225)
    adayEntry.place(x=255, y=225)
    ayearEntry.place(x=290, y=225)
    URLLabel.place(x=15, y=250)
    URLEntry.place(x=105, y=250)



def mlaBookPlaceFunction():
    bookTitleLabel.place(x=15, y=125)
    bookEntry.place(x=105, y=125)
    authorLabel.place(x=15, y=150)
    authorFirstEntry.place(x=105, y=150)
    authorMiddleEntry.place(x=255, y=150)
    authorLastEntry.place(x=290, y=150)
    blocationLabel.place(x=15, y=175)
    blocationEntry.place(x=105, y=175)
    publisherLabel.place(x=15, y=200)
    publisherEntry.place(x=105, y=200)
    mlabookpyearLabel.place(x=15, y=225)
    mlabookpyearEntry.place(x=105, y=225)

def apaBookPlaceFunction():
    bookTitleLabel.place(x=15, y=125)
    bookEntry.place(x=105, y=125)
    authorLabel.place(x=15, y=150)
    authorFirstEntry.place(x=105, y=150)
    authorMiddleEntry.place(x=255, y=150)
    authorLastEntry.place(x=290, y=150)
    blocationLabel.place(x=15, y=175)
    blocationEntry.place(x=105, y=175)
    publisherLabel.place(x=15, y=200)
    publisherEntry.place(x=105, y=200)
    mlabookpyearLabel.place(x=15, y=225)
    mlabookpyearEntry.place(x=105, y=225)
    statelocationLabel.place(x=15, y=250)
    statelocationEntry.place(x=105, y = 250)

def chicagoBookPlaceFunction():
    bookTitleLabel.place(x=15, y=125)
    bookEntry.place(x=105, y=125)
    authorLabel.place(x=15, y=150)
    authorFirstEntry.place(x=105, y=150)
    authorMiddleEntry.place(x=255, y=150)
    authorLastEntry.place(x=290, y=150)
    blocationLabel.place(x=15, y=175)
    blocationEntry.place(x=105, y=175)
    publisherLabel.place(x=15, y=200)
    publisherEntry.place(x=105, y=200)
    mlabookpyearLabel.place(x=15, y=225)
    mlabookpyearEntry.place(x=105, y=225)



def mlaButtonFunction(event):
    bibFormat.configure(text = "MLA8")
    clearFunction()
    if(typeFormat.cget('text') == "Website"):
        mlaWebsitePlaceFunction()
    elif(typeFormat.cget('text') == "Book"):
        mlaBookPlaceFunction()
    elif(typeFormat.cget("text") == "Video"):
        pass
    elif(typeFormat.cget("text") == "Journal"):
        pass
    else:
        print("An Error Occurred")

def apaButtonFunction(event):
    bibFormat.configure(text = "APA")
    clearFunction()
    if(typeFormat.cget('text') == "Website"):
        apaWebsitePlaceFunction()
    elif(typeFormat.cget('text') == 'Book'):
        apaBookPlaceFunction()
    elif(typeFormat.cget("text") == "Video"):
        pass
    elif(typeFormat.cget('text') == "Journal"):
        pass
    else:
        print("An Error Occurred")

def chicagoButtonFunction(event):
    bibFormat.configure(text = "Chicago")
    clearFunction()
    if(typeFormat.cget('text') == "Website"):
        chicagoWebsitePlaceFunction()
    elif(typeFormat.cget("text") == "Book"):
        chicagoBookPlaceFunction()
    elif(typeFormat.cget("text") == "Video"):
        pass
    elif(typeFormat.cget('text') == "Journal"):
        pass
    else:
        print("An Error Occurred")



#Type Functions
#Will need to add more funcionality to these functions
def websiteButtonFunction(event):
    typeFormat.configure(text = "Website")
    clearFunction()
    if(bibFormat.cget('text') == "MLA8"):
        mlaWebsitePlaceFunction()
    elif(bibFormat.cget('text') == "APA"):
        apaWebsitePlaceFunction()
    elif(bibFormat.cget('text') == "Chicago"):
        chicagoWebsitePlaceFunction()
    else:
        print("An Error Occurred")

def bookButtonFunction(event):
    typeFormat.configure(text = "Book")
    clearFunction()
    if(bibFormat.cget("text") == "MLA8"):
        mlaBookPlaceFunction()
    elif(bibFormat.cget('text') == "APA"):
        apaBookPlaceFunction()
    elif(bibFormat.cget('text') == "Chicago"):
        chicagoBookPlaceFunction()
    else:
        print("An Error Occurred")

def videoButtonFunction(event):
    typeFormat.configure(text = "Video")
    clearFunction()
    if (bibFormat.cget('text') == "MLA8"):
        pass
    elif (bibFormat.cget('text') == "APA"):
        pass
    elif (bibFormat.cget('text') == "Chicago"):
        pass
    else:
        print("An Error Occurred")

def journalButtonFunction(event):
    typeFormat.configure(text = "Journal")
    clearFunction()
    if (bibFormat.cget('text') == "MLA8"):
        pass
    elif (bibFormat.cget('text') == "APA"):
        pass
    elif (bibFormat.cget('text') == "Chicago"):
        pass
    else:
        print("An Error Occurred")



#Format Binds
mlaButton.bind('<Button-1>', mlaButtonFunction)
apaButton.bind('<Button-1>', apaButtonFunction)
#chicagoButton.bind('<Button-1>', chicagoButtonFunction)

#Type Binds
websiteButton.bind('<Button-1>', websiteButtonFunction)
bookButton.bind('<Button-1>', bookButtonFunction)
#videoButton.bind('<Button-1>', videoButtonFunction)
#journalButton.bind('<Button-1>', journalButtonFunction)

#ENTRY CODE FOR MLA WEBSITE

#Article Entry Code
articleTitleLabel = Label(master, text = "Article Title: ")
articleTextVar = StringVar()
articleTextVar.set("Article Title")
articleEntry = Entry(master, textvariable=articleTextVar, fg = "grey", width = 70)

def articleOnEntryClick(event):
    if articleEntry.get() == 'Article Title':
       articleEntry.delete(0, "end") # delete all the text in the entry
       articleEntry.insert(0, '') #Insert blank for user input
       articleEntry.config(fg = 'black')
def articleOnFocusOut(event):
    if articleEntry.get() == '':
        articleEntry.insert(0, 'Article Title')
        articleEntry.config(fg = 'grey')

articleEntry.bind('<FocusIn>', articleOnEntryClick)
articleEntry.bind('<FocusOut>', articleOnFocusOut)

#Author Entry Code
#First Name
authorLabel = Label(master, text = "Author:")
authorFirstTextVar = StringVar()
authorFirstTextVar.set("First Name")
authorFirstEntry = Entry(master, textvariable=authorFirstTextVar, fg = 'grey', width = 24)

def authorFirstOnEntryClick(event):
    if authorFirstEntry.get() == 'First Name':
       authorFirstEntry.delete(0, "end") # delete all the text in the entry
       authorFirstEntry.insert(0, '') #Insert blank for user input
       authorFirstEntry.config(fg = 'black')
def authorFirstOnFocusOut(event):
    if authorFirstEntry.get() == '':
        authorFirstEntry.insert(0, 'First Name')
        authorFirstEntry.config(fg = 'grey')

authorFirstEntry.bind('<FocusIn>', authorFirstOnEntryClick)
authorFirstEntry.bind('<FocusOut>', authorFirstOnFocusOut)

#Middle Initial
authorMiddleTextVar = StringVar()
authorMiddleTextVar.set("M.I.")
authorMiddleEntry = Entry(master, textvariable=authorMiddleTextVar, fg = 'grey', width = 5)

def authorMiddleOnEntryClick(event):
    if authorMiddleEntry.get() == 'M.I.':
       authorMiddleEntry.delete(0, "end") # delete all the text in the entry
       authorMiddleEntry.insert(0, '') #Insert blank for user input
       authorMiddleEntry.config(fg = 'black')
def authorMiddleOnFocusOut(event):
    if authorMiddleEntry.get() == '':
        authorMiddleEntry.insert(0, 'M.I.')
        authorMiddleEntry.config(fg = 'grey')

authorMiddleEntry.bind('<FocusIn>', authorMiddleOnEntryClick)
authorMiddleEntry.bind('<FocusOut>', authorMiddleOnFocusOut)

#Last Name
authorLastTextVar = StringVar()
authorLastTextVar.set("Last Name")
authorLastEntry = Entry(master, textvariable=authorLastTextVar, fg = 'grey', width = 39)#Weird Value so that the entry widgets line up together
def authorLastOnEntryClick(event):
    if authorLastEntry.get() == 'Last Name':
       authorLastEntry.delete(0, "end") # delete all the text in the entry
       authorLastEntry.insert(0, '') #Insert blank for user input
       authorLastEntry.config(fg = 'black')
def authorLastOnFocusOut(event):
    if authorLastEntry.get() == '':
        authorLastEntry.insert(0, 'Last Name')
        authorLastEntry.config(fg = 'grey')

authorLastEntry.bind('<FocusIn>', authorLastOnEntryClick)
authorLastEntry.bind('<FocusOut>', authorLastOnFocusOut)


#Website Title
websiteTitleLabel = Label(master, text = "Website Title:")
websiteTitleTextVar = StringVar()
websiteTitleTextVar.set("Website Title")
websiteTitleEntry = Entry(master, textvariable=websiteTitleTextVar, fg = 'grey', width = 70)

def websiteTitleOnEntryClick(event):
    if websiteTitleEntry.get() == 'Website Title':
        websiteTitleEntry.delete(0, "end") # delete all the text in the entry
        websiteTitleEntry.insert(0, '') #Insert blank for user input
        websiteTitleEntry.config(fg = 'black')
def websiteTitleOnFocusOut(event):
    if websiteTitleEntry.get() == '':
        websiteTitleEntry.insert(0, 'Website Title')
        websiteTitleEntry.config(fg = 'grey')

websiteTitleEntry.bind('<FocusIn>', websiteTitleOnEntryClick)
websiteTitleEntry.bind('<FocusOut>', websiteTitleOnFocusOut)

#Publisher/Sponser Information
publisherLabel = Label(master, text = "Publisher: ")
publisherTextVar = StringVar()
publisherTextVar.set("Publisher")
publisherEntry = Entry(master, textvariable=publisherTextVar, fg = 'grey', width = 70)

def publisherOnEntryClick(event):
    if publisherEntry.get() == 'Publisher':
        publisherEntry.delete(0, "end") # delete all the text in the entry
        publisherEntry.insert(0, '') #Insert blank for user input
        publisherEntry.config(fg = 'black')
def publisherOnFocusOut(event):
    if publisherEntry.get() == '':
        publisherEntry.insert(0, 'Publisher')
        publisherEntry.config(fg = 'grey')

publisherEntry.bind('<FocusIn>', publisherOnEntryClick)
publisherEntry.bind('<FocusOut>', publisherOnFocusOut)

#Date Published Code
#Month
pDateLabel = Label(master, text = "Date Published:")
pmonthTextVar = StringVar()
pmonthTextVar.set("Month")
pmonthEntry = Entry(master, textvariable=pmonthTextVar, fg = 'grey', width = 24)

def pmonthOnEntryClick(event):
    if pmonthEntry.get() == 'Month':
       pmonthEntry.delete(0, "end") # delete all the text in the entry
       pmonthEntry.insert(0, '') #Insert blank for user input
       pmonthEntry.config(fg = 'black')
def pmonthOnFocusOut(event):
    if pmonthEntry.get() == '':
        pmonthEntry.insert(0, 'Month')
        pmonthEntry.config(fg = 'grey')

pmonthEntry.bind('<FocusIn>', pmonthOnEntryClick)
pmonthEntry.bind('<FocusOut>', pmonthOnFocusOut)

#Day
pdayTextVar = StringVar()
pdayTextVar.set("Day")
pdayEntry = Entry(master, textvariable=pdayTextVar, fg = 'grey', width = 5)

def pdayOnEntryClick(event):
    if pdayEntry.get() == 'Day':
       pdayEntry.delete(0, "end") # delete all the text in the entry
       pdayEntry.insert(0, '') #Insert blank for user input
       pdayEntry.config(fg = 'black')
def pdayOnFocusOut(event):
    if pdayEntry.get() == '':
        pdayEntry.insert(0, 'Day')
        pdayEntry.config(fg = 'grey')

pdayEntry.bind('<FocusIn>', pdayOnEntryClick)
pdayEntry.bind('<FocusOut>', pdayOnFocusOut)

#Year
pyearTextVar = StringVar()
pyearTextVar.set("Year")
pyearEntry = Entry(master, textvariable=pyearTextVar, fg = 'grey', width = 39)#Weird Value so that the entry widgets line up together

def pyearOnEntryClick(event):
    if pyearEntry.get() == 'Year':
       pyearEntry.delete(0, "end") # delete all the text in the entry
       pyearEntry.insert(0, '') #Insert blank for user input
       pyearEntry.config(fg = 'black')
def pyearOnFocusOut(event):
    if pyearEntry.get() == '':
        pyearEntry.insert(0, 'Year')
        pyearEntry.config(fg = 'grey')

pyearEntry.bind('<FocusIn>', pyearOnEntryClick)
pyearEntry.bind('<FocusOut>', pyearOnFocusOut)


#Date Accessed Code
#Month
aDateLabel = Label(master, text = "Date Accessed:")
amonthTextVar = StringVar()
amonthTextVar.set("Month")
amonthEntry = Entry(master, textvariable=amonthTextVar, fg = 'grey', width = 24)

def amonthOnEntryClick(event):
    if amonthEntry.get() == 'Month':
       amonthEntry.delete(0, "end") # delete all the text in the entry
       amonthEntry.insert(0, '') #Insert blank for user input
       amonthEntry.config(fg = 'black')
def amonthOnFocusOut(event):
    if amonthEntry.get() == '':
        amonthEntry.insert(0, 'Month')
        amonthEntry.config(fg = 'grey')

amonthEntry.bind('<FocusIn>', amonthOnEntryClick)
amonthEntry.bind('<FocusOut>', amonthOnFocusOut)

#Day
adayTextVar = StringVar()
adayTextVar.set("Day")
adayEntry = Entry(master, textvariable=adayTextVar, fg = 'grey', width = 5)

def adayOnEntryClick(event):
    if adayEntry.get() == 'Day':
       adayEntry.delete(0, "end") # delete all the text in the entry
       adayEntry.insert(0, '') #Insert blank for user input
       adayEntry.config(fg = 'black')
def adayOnFocusOut(event):
    if adayEntry.get() == '':
        adayEntry.insert(0, 'Day')
        adayEntry.config(fg = 'grey')

adayEntry.bind('<FocusIn>', adayOnEntryClick)
adayEntry.bind('<FocusOut>', adayOnFocusOut)

#Year
ayearTextVar = StringVar()
ayearTextVar.set("Year")
ayearEntry = Entry(master, textvariable=ayearTextVar, fg = 'grey', width = 39)#Weird Value so that the entry widgets line up together

def ayearOnEntryClick(event):
    if ayearEntry.get() == 'Year':
       ayearEntry.delete(0, "end") # delete all the text in the entry
       ayearEntry.insert(0, '') #Insert blank for user input
       ayearEntry.config(fg = 'black')
def ayearOnFocusOut(event):
    if ayearEntry.get() == '':
        ayearEntry.insert(0, 'Year')
        ayearEntry.config(fg = 'grey')

ayearEntry.bind('<FocusIn>', ayearOnEntryClick)
ayearEntry.bind('<FocusOut>', ayearOnFocusOut)

#URL Information
URLLabel = Label(master, text = "URL: ")
URLTextVar = StringVar()
URLTextVar.set("URL")
URLEntry = Entry(master, textvariable=URLTextVar, fg = 'grey', width = 70)

def URLOnEntryClick(event):
    if URLEntry.get() == 'URL':
        URLEntry.delete(0, "end") # delete all the text in the entry
        URLEntry.insert(0, '') #Insert blank for user input
        URLEntry.config(fg = 'black')
def URLOnFocusOut(event):
    if URLEntry.get() == '':
        URLEntry.insert(0, 'URL')
        URLEntry.config(fg = 'grey')

URLEntry.bind('<FocusIn>', URLOnEntryClick)
URLEntry.bind('<FocusOut>', URLOnFocusOut)



#bibFormat and typeFormat

#Stuff that needs declaration:
#Book
bookTitleLabel = Label(master, text = "Book Title:")
bookTextVar = StringVar()
bookTextVar.set("Book Title")
bookEntry = Entry(master, textvariable = bookTextVar, fg = "grey", width = 70)

def bookOnEntryClick(event):
    if bookEntry.get() == 'Book Title':
       bookEntry.delete(0, "end") # delete all the text in the entry
       bookEntry.insert(0, '') #Insert blank for user input
       bookEntry.config(fg = 'black')
def bookOnFocusOut(event):
    if bookEntry.get() == '':
        bookEntry.insert(0, 'Book Title')
        bookEntry.config(fg = 'grey')

bookEntry.bind('<FocusIn>', bookOnEntryClick)
bookEntry.bind('<FocusOut>', bookOnFocusOut)


#Location of Publication (City)
blocationLabel = Label(master, text = "City:")
blocationTextVar = StringVar()
blocationTextVar.set("City the book was published in")
blocationEntry = Entry(master, textvariable = blocationTextVar, fg = "grey", width = 70)

def blocationOnEntryClick(event):
    if blocationEntry.get() == 'City the book was published in':
       blocationEntry.delete(0, "end") # delete all the text in the entry
       blocationEntry.insert(0, '') #Insert blank for user input
       blocationEntry.config(fg = 'black')
def blocationOnFocusOut(event):
    if blocationEntry.get() == '':
        blocationEntry.insert(0, 'City the book was published in')
        blocationEntry.config(fg = 'grey')

blocationEntry.bind('<FocusIn>', blocationOnEntryClick)
blocationEntry.bind('<FocusOut>', blocationOnFocusOut)

#MLA Year of Publication
mlabookpyearLabel = Label(master, text = "Year:")
mlabookpyearTextVar = StringVar()
mlabookpyearTextVar.set("Year")
mlabookpyearEntry = Entry(master, textvariable=mlabookpyearTextVar, fg = 'grey', width = 70)

def mlabookpyearOnEntryClick(event):
    if mlabookpyearEntry.get() == 'Year':
       mlabookpyearEntry.delete(0, "end") # delete all the text in the entry
       mlabookpyearEntry.insert(0, '') #Insert blank for user input
       mlabookpyearEntry.config(fg = 'black')
def mlabookpyearOnFocusOut(event):
    if mlabookpyearEntry.get() == '':
        mlabookpyearEntry.insert(0, 'Year')
        mlabookpyearEntry.config(fg = 'grey')

mlabookpyearEntry.bind('<FocusIn>', mlabookpyearOnEntryClick)
mlabookpyearEntry.bind('<FocusOut>', mlabookpyearOnFocusOut)

#Location of Publication (State)
statelocationLabel = Label(master, text = "State:")
statelocationTextVar = StringVar()
statelocationTextVar.set("State the book was published in")
statelocationEntry = Entry(master, textvariable = statelocationTextVar, fg = "grey", width = 70)

def statelocationOnEntryClick(event):
    if statelocationEntry.get() == 'State the book was published in':
       statelocationEntry.delete(0, "end") # delete all the text in the entry
       statelocationEntry.insert(0, '') #Insert blank for user input
       statelocationEntry.config(fg = 'black')
def statelocationOnFocusOut(event):
    if statelocationEntry.get() == '':
        statelocationEntry.insert(0, 'State the book was published in')
        statelocationEntry.config(fg = 'grey')

statelocationEntry.bind('<FocusIn>', statelocationOnEntryClick)
statelocationEntry.bind('<FocusOut>', statelocationOnFocusOut)

#Cite Button
citeButton = Button(master, text = "Cite It!")
citeButton.place(x = 15, y =350)

def citeButtonFunction(event):
    print ("Cite it")

citeButton.bind('<Button-1>', citeButtonFunction)






mlaWebsitePlaceFunction()
master.mainloop()




















