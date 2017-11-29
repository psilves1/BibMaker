from tkinter import *

master = Tk()

master.geometry("800x500")#Sets shape of GUI
master.title("Bibliography Maker Pre-Development") #Title
master.iconbitmap("Apple.ico")#Icon Picture

#Gap between the entry widgets is 25 pixels


#Functions_________________________________________________________________________________________________________________

def clearFunction():
    #Article
    articleTitleLabel.place_forget()
    articleEntry.place_forget()
    articleEntry.delete(0, END)
    articleEntry.insert(0, "Article Title")
    articleEntry.configure(fg = "grey")
    #Author
    authorLabel.place_forget()
    authorFirstEntry.place_forget()
    authorFirstEntry.delete(0, END)
    authorFirstEntry.insert(0, "First name")
    authorFirstEntry.configure(fg = "grey")
    authorMiddleEntry.place_forget()
    authorMiddleEntry.delete(0, END)
    authorMiddleEntry.insert(0, "M.I.")
    authorMiddleEntry.configure(fg = "grey")
    authorLastEntry.place_forget()
    authorLastEntry.delete(0, END)
    authorLastEntry.insert(0, "Last name")
    authorLastEntry.configure(fg = "grey")
    #Website
    websiteTitleLabel.place_forget()
    websiteTitleEntry.place_forget()
    websiteTitleEntry.delete(0, END)
    websiteTitleEntry.insert(0, 'Website Title')
    websiteTitleEntry.configure(fg = "grey")
    #Publisher
    publisherLabel.place_forget()
    publisherEntry.place_forget()
    publisherEntry.delete(0, END)
    publisherEntry.insert(0, "Publisher")
    publisherEntry
    #URL
    URLLabel.place_forget()
    URLEntry.place_forget()
    URLEntry.delete(0, END)
    URLEntry.insert(0, "URL")
    URLEntry
    #Publisher Date
    pDateLabel.place_forget()
    pmonthEntry.place_forget()
    pmonthEntry.delete(0, END)
    pmonthEntry.insert(0, "Month")
    pmonthEntry
    pdayEntry.place_forget()
    pdayEntry.delete(0, END)
    pdayEntry.insert(0, "Day")
    pdayEntry
    pyearEntry.place_forget()
    pyearEntry.delete(0, END)
    pyearEntry.insert(0, "Year")
    pyearEntry
    #Accessed Date
    aDateLabel.place_forget()
    amonthEntry.place_forget()
    amonthEntry.delete(0, END)
    amonthEntry.insert(0, "Month")
    amonthEntry
    adayEntry.place_forget()
    adayEntry.delete(0, END)
    adayEntry.insert(0, "Day")
    adayEntry
    ayearEntry.place_forget()
    ayearEntry.delete(0, END)
    ayearEntry.insert(0, "Year")
    ayearEntry
    #Book Title
    bookTitleLabel.place_forget()
    bookEntry.place_forget()
    bookEntry.delete(0, END)
    bookEntry.insert(0, "Book Title")
    bookEntry
    #Book Location City
    blocationLabel.place_forget()
    blocationEntry.place_forget()
    blocationEntry.delete(0, END)
    blocationEntry.insert(0, "City the book was published in")
    blocationEntry
    #MLA Book Year
    mlabookpyearLabel.place_forget()
    mlabookpyearEntry.place_forget()
    mlabookpyearEntry.delete(0, END)
    mlabookpyearEntry.insert(0, "Year")
    mlabookpyearEntry
    #Book Location State
    statelocationEntry.place_forget()
    statelocationLabel.place_forget()
    statelocationEntry.delete(0, END)
    statelocationEntry.insert(0, "State the book was published in")
    statelocationEntry

    clearLastWidget()


def clearLastWidget(): #Clears the widget the cursor is in. In Python it is called the Focus
    try:
        e = master.focus_get()
        e.delete(0, END)
        e.configure(fg = "black")
    except AttributeError:#This error will occur if the user hits "Cite it" wihtout having a widget selected
        pass

#Place Functions___________________________________________________________________________________________________________

#Website Place Functions
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

# def chicagoWebsitePlaceFunction():
#     articleTitleLabel.place(x=15, y=125)
#     articleEntry.place(x=105, y=125)
#     authorLabel.place(x=15, y=150)
#     authorFirstEntry.place(x=105, y=150)
#     authorMiddleEntry.place(x=255, y=150)
#     authorLastEntry.place(x=290, y=150)
#     websiteTitleLabel.place(x=15, y=175)
#     websiteTitleEntry.place(x=105, y=175)
#     pDateLabel.place(x=15, y=200)
#     pmonthEntry.place(x=105, y=200)
#     pdayEntry.place(x=255, y=200)
#     pyearEntry.place(x=290, y=200)
#     aDateLabel.place(x=15, y=250)
#     amonthEntry.place(x=105, y=225)
#     adayEntry.place(x=255, y=225)
#     ayearEntry.place(x=290, y=225)
#     URLLabel.place(x=15, y=250)
#     URLEntry.place(x=105, y=250)

#Book Place Functions
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

# def chicagoBookPlaceFunction():
#     bookTitleLabel.place(x=15, y=125)
#     bookEntry.place(x=105, y=125)
#     authorLabel.place(x=15, y=150)
#     authorFirstEntry.place(x=105, y=150)
#     authorMiddleEntry.place(x=255, y=150)
#     authorLastEntry.place(x=290, y=150)
#     blocationLabel.place(x=15, y=175)
#     blocationEntry.place(x=105, y=175)
#     publisherLabel.place(x=15, y=200)
#     publisherEntry.place(x=105, y=200)
#     mlabookpyearLabel.place(x=15, y=225)
#     mlabookpyearEntry.place(x=105, y=225)


#Button Functions__________________________________________________________________________________________________________
def mlaButtonFunction(event):
    bibType.configure(text = "MLA8")
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
    bibType.configure(text = "APA")
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

# def chicagoButtonFunction(event):
#     bibType.configure(text = "Chicago")
#     clearFunction()
#     if(typeFormat.cget('text') == "Website"):
#         chicagoWebsitePlaceFunction()
#     elif(typeFormat.cget("text") == "Book"):
#         chicagoBookPlaceFunction()
#     elif(typeFormat.cget("text") == "Video"):
#         pass
#     elif(typeFormat.cget('text') == "Journal"):
#         pass
#     else:
#         print("An Error Occurred")



#Type Functions
#Will need to add more funcionality to these functions

def websiteButtonFunction(event):
    typeFormat.configure(text = "Website")
    clearFunction()
    if(bibType.cget('text') == "MLA8"):
        mlaWebsitePlaceFunction()
    elif(bibType.cget('text') == "APA"):
        apaWebsitePlaceFunction()
    # elif(bibType.cget('text') == "Chicago"):
    #     chicagoWebsitePlaceFunction()
    else:
        print("An Error Occurred")

def bookButtonFunction(event):
    typeFormat.configure(text = "Book")
    clearFunction()
    if(bibType.cget("text") == "MLA8"):
        mlaBookPlaceFunction()
    elif(bibType.cget('text') == "APA"):
        apaBookPlaceFunction()
    # elif(bibType.cget('text') == "Chicago"):
    #     chicagoBookPlaceFunction()
    else:
        print("An Error Occurred")

# def videoButtonFunction(event):
#     typeFormat.configure(text = "Video")
#     clearFunction()
#     if (bibType.cget('text') == "MLA8"):
#         pass
#     elif (bibType.cget('text') == "APA"):
#         pass
#     elif (bibType.cget('text') == "Chicago"):
#         pass
#     else:
#         print("An Error Occurred")
#
# def journalButtonFunction(event):
#     typeFormat.configure(text = "Journal")
#     clearFunction()
#     if (bibType.cget('text') == "MLA8"):
#         pass
#     elif (bibType.cget('text') == "APA"):
#         pass
#     elif (bibType.cget('text') == "Chicago"):
#         pass
#     else:
#         print("An Error Occurred")



#Format Binds

#Bind Functions____________________________________________________________________________________________________________

def articleOnEntryClick(event):
    if articleEntry.get() == 'Article Title':
       articleEntry.delete(0, "end") # delete all the text in the entry
       articleEntry.insert(0, '') #Insert blank for user input
       articleEntry.config(fg = 'black')
def articleOnFocusOut(event):
    if articleEntry.get() == '':
        articleEntry.insert(0, 'Article Title')
        articleEntry.config(fg = 'grey')

def authorFirstOnEntryClick(event):
    if authorFirstEntry.get() == 'First Name':
       authorFirstEntry.delete(0, "end") # delete all the text in the entry
       authorFirstEntry.insert(0, '') #Insert blank for user input
       authorFirstEntry.config(fg = 'black')
def authorFirstOnFocusOut(event):
    if authorFirstEntry.get() == '':
        authorFirstEntry.insert(0, 'First Name')
        authorFirstEntry.config(fg = 'grey')

def authorMiddleOnEntryClick(event):
    if authorMiddleEntry.get() == 'M.I.':
       authorMiddleEntry.delete(0, "end") # delete all the text in the entry
       authorMiddleEntry.insert(0, '') #Insert blank for user input
       authorMiddleEntry.config(fg = 'black')
def authorMiddleOnFocusOut(event):
    if authorMiddleEntry.get() == '':
        authorMiddleEntry.insert(0, 'M.I.')
        authorMiddleEntry.config(fg = 'grey')

def authorLastOnEntryClick(event):
    if authorLastEntry.get() == 'Last Name':
       authorLastEntry.delete(0, "end") # delete all the text in the entry
       authorLastEntry.insert(0, '') #Insert blank for user input
       authorLastEntry.config(fg = 'black')
def authorLastOnFocusOut(event):
    if authorLastEntry.get() == '':
        authorLastEntry.insert(0, 'Last Name')
        authorLastEntry.config(fg = 'grey')

def websiteTitleOnEntryClick(event):
    if websiteTitleEntry.get() == 'Website Title':
        websiteTitleEntry.delete(0, "end") # delete all the text in the entry
        websiteTitleEntry.insert(0, '') #Insert blank for user input
        websiteTitleEntry.config(fg = 'black')
def websiteTitleOnFocusOut(event):
    if websiteTitleEntry.get() == '':
        websiteTitleEntry.insert(0, 'Website Title')
        websiteTitleEntry.config(fg = 'grey')

def authorLastOnEntryClick(event):
    if authorLastEntry.get() == 'Last Name':
       authorLastEntry.delete(0, "end") # delete all the text in the entry
       authorLastEntry.insert(0, '') #Insert blank for user input
       authorLastEntry.config(fg = 'black')
def authorLastOnFocusOut(event):
    if authorLastEntry.get() == '':
        authorLastEntry.insert(0, 'Last Name')
        authorLastEntry.config(fg = 'grey')

def publisherOnEntryClick(event):
    if publisherEntry.get() == 'Publisher':
        publisherEntry.delete(0, "end") # delete all the text in the entry
        publisherEntry.insert(0, '') #Insert blank for user input
        publisherEntry.config(fg = 'black')
def publisherOnFocusOut(event):
    if publisherEntry.get() == '':
        publisherEntry.insert(0, 'Publisher')
        publisherEntry.config(fg = 'grey')

def pmonthOnEntryClick(event):
    if pmonthEntry.get() == 'Month':
       pmonthEntry.delete(0, "end") # delete all the text in the entry
       pmonthEntry.insert(0, '') #Insert blank for user input
       pmonthEntry.config(fg = 'black')
def pmonthOnFocusOut(event):
    if pmonthEntry.get() == '':
        pmonthEntry.insert(0, 'Month')
        pmonthEntry.config(fg = 'grey')

def pdayOnEntryClick(event):
    if pdayEntry.get() == 'Day':
       pdayEntry.delete(0, "end") # delete all the text in the entry
       pdayEntry.insert(0, '') #Insert blank for user input
       pdayEntry.config(fg = 'black')
def pdayOnFocusOut(event):
    if pdayEntry.get() == '':
        pdayEntry.insert(0, 'Day')
        pdayEntry.config(fg = 'grey')

def pyearOnEntryClick(event):
    if pyearEntry.get() == 'Year':
       pyearEntry.delete(0, "end") # delete all the text in the entry
       pyearEntry.insert(0, '') #Insert blank for user input
       pyearEntry.config(fg = 'black')
def pyearOnFocusOut(event):
    if pyearEntry.get() == '':
        pyearEntry.insert(0, 'Year')
        pyearEntry.config(fg = 'grey')

def amonthOnEntryClick(event):
    if amonthEntry.get() == 'Month':
       amonthEntry.delete(0, "end") # delete all the text in the entry
       amonthEntry.insert(0, '') #Insert blank for user input
       amonthEntry.config(fg = 'black')
def amonthOnFocusOut(event):
    if amonthEntry.get() == '':
        amonthEntry.insert(0, 'Month')
        amonthEntry.config(fg = 'grey')

def adayOnEntryClick(event):
    if adayEntry.get() == 'Day':
       adayEntry.delete(0, "end") # delete all the text in the entry
       adayEntry.insert(0, '') #Insert blank for user input
       adayEntry.config(fg = 'black')
def adayOnFocusOut(event):
    if adayEntry.get() == '':
        adayEntry.insert(0, 'Day')
        adayEntry.config(fg = 'grey')

def ayearOnEntryClick(event):
    if ayearEntry.get() == 'Year':
       ayearEntry.delete(0, "end") # delete all the text in the entry
       ayearEntry.insert(0, '') #Insert blank for user input
       ayearEntry.config(fg = 'black')
def ayearOnFocusOut(event):
    if ayearEntry.get() == '':
        ayearEntry.insert(0, 'Year')
        ayearEntry.config(fg = 'grey')

def URLOnEntryClick(event):
    if URLEntry.get() == 'URL':
        URLEntry.delete(0, "end") # delete all the text in the entry
        URLEntry.insert(0, '') #Insert blank for user input
        URLEntry.config(fg = 'black')
def URLOnFocusOut(event):
    if URLEntry.get() == '':
        URLEntry.insert(0, 'URL')
        URLEntry.config(fg = 'grey')

def bookOnEntryClick(event):
    if bookEntry.get() == 'Book Title':
       bookEntry.delete(0, "end") # delete all the text in the entry
       bookEntry.insert(0, '') #Insert blank for user input
       bookEntry.config(fg = 'black')
def bookOnFocusOut(event):
    if bookEntry.get() == '':
        bookEntry.insert(0, 'Book Title')
        bookEntry.config(fg = 'grey')

def blocationOnEntryClick(event):
    if blocationEntry.get() == 'City the book was published in':
       blocationEntry.delete(0, "end") # delete all the text in the entry
       blocationEntry.insert(0, '') #Insert blank for user input
       blocationEntry.config(fg = 'black')
def blocationOnFocusOut(event):
    if blocationEntry.get() == '':
        blocationEntry.insert(0, 'City the book was published in')
        blocationEntry.config(fg = 'grey')

def mlabookpyearOnEntryClick(event):
    if mlabookpyearEntry.get() == 'Year':
       mlabookpyearEntry.delete(0, "end") # delete all the text in the entry
       mlabookpyearEntry.insert(0, '') #Insert blank for user input
       mlabookpyearEntry.config(fg = 'black')
def mlabookpyearOnFocusOut(event):
    if mlabookpyearEntry.get() == '':
        mlabookpyearEntry.insert(0, 'Year')
        mlabookpyearEntry.config(fg = 'grey')

def statelocationOnEntryClick(event):
    if statelocationEntry.get() == 'State the book was published in':
       statelocationEntry.delete(0, "end") # delete all the text in the entry
       statelocationEntry.insert(0, '') #Insert blank for user input
       statelocationEntry.config(fg = 'black')
def statelocationOnFocusOut(event):
    if statelocationEntry.get() == '':
        statelocationEntry.insert(0, 'State the book was published in')
        statelocationEntry.config(fg = 'grey')

def citeButtonFunction(event):
    print ("Cite it")

    clearFunction()

    if(bibType.cget('text') == "MLA8"):
        if(typeFormat.cget('text') == "Website"):
            mlaWebsitePlaceFunction()
        else:
            mlaBookPlaceFunction()
    elif(bibType.cget('text') == "APA"):
        if(typeFormat.cget('text') == "Website"):
            apaWebsitePlaceFunction()
        else:
            apaBookPlaceFunction()




#Places the Buttons and Labels that never move_____________________________________________________________________________

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

bibType = Label(master, text="MLA8")
bibType.place(x= 135, y=70)

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
typeFormat.place(x = 390, y = 70)





#Core Button Binds_________________________________________________________________________________________________________

mlaButton.bind('<Button-1>', mlaButtonFunction)
apaButton.bind('<Button-1>', apaButtonFunction)
#chicagoButton.bind('<Button-1>', chicagoButtonFunction)

#Type Binds
websiteButton.bind('<Button-1>', websiteButtonFunction)
bookButton.bind('<Button-1>', bookButtonFunction)
#videoButton.bind('<Button-1>', videoButtonFunction)
#journalButton.bind('<Button-1>', journalButtonFunction





#Article Entry Code________________________________________________________________________________________________________
articleTitleLabel = Label(master, text = "Article Title: ")
articleTextVar = StringVar()
articleTextVar.set("Article Title")
articleEntry = Entry(master, textvariable=articleTextVar, fg = "grey", width = 70)
#Binds
articleEntry.bind('<FocusIn>', articleOnEntryClick)
articleEntry.bind('<FocusOut>', articleOnFocusOut)



#Author Entry Code_________________________________________________________________________________________________________

#First Name________________________________________________________________________________________________________________
authorLabel = Label(master, text = "Author:")
authorFirstTextVar = StringVar()
authorFirstTextVar.set("First Name")
authorFirstEntry = Entry(master, textvariable=authorFirstTextVar, fg = 'grey', width = 24)
#Binds
authorFirstEntry.bind('<FocusIn>', authorFirstOnEntryClick)
authorFirstEntry.bind('<FocusOut>', authorFirstOnFocusOut)

#Middle Initial____________________________________________________________________________________________________________
authorMiddleTextVar = StringVar()
authorMiddleTextVar.set("M.I.")
authorMiddleEntry = Entry(master, textvariable=authorMiddleTextVar, fg = 'grey', width = 5)
#Binds
authorMiddleEntry.bind('<FocusIn>', authorMiddleOnEntryClick)
authorMiddleEntry.bind('<FocusOut>', authorMiddleOnFocusOut)

#Last Name_________________________________________________________________________________________________________________
authorLastTextVar = StringVar()
authorLastTextVar.set("Last Name")
authorLastEntry = Entry(master, textvariable=authorLastTextVar, fg = 'grey', width = 39)#Weird Value so that the entry widgets line up together
#Binds
authorLastEntry.bind('<FocusIn>', authorLastOnEntryClick)
authorLastEntry.bind('<FocusOut>', authorLastOnFocusOut)




#Website Title_____________________________________________________________________________________________________________
websiteTitleLabel = Label(master, text = "Website Title:")
websiteTitleTextVar = StringVar()
websiteTitleTextVar.set("Website Title")
websiteTitleEntry = Entry(master, textvariable=websiteTitleTextVar, fg = 'grey', width = 70)
#Binds
websiteTitleEntry.bind('<FocusIn>', websiteTitleOnEntryClick)
websiteTitleEntry.bind('<FocusOut>', websiteTitleOnFocusOut)


#Publisher/Sponser Information_____________________________________________________________________________________________
publisherLabel = Label(master, text = "Publisher: ")
publisherTextVar = StringVar()
publisherTextVar.set("Publisher")
publisherEntry = Entry(master, textvariable=publisherTextVar, fg = 'grey', width = 70)
#Binds
publisherEntry.bind('<FocusIn>', publisherOnEntryClick)
publisherEntry.bind('<FocusOut>', publisherOnFocusOut)




#Date Published Code_______________________________________________________________________________________________________

#Month_____________________________________________________________________________________________________________________
pDateLabel = Label(master, text = "Date Published:")
pmonthTextVar = StringVar()
pmonthTextVar.set("Month")
pmonthEntry = Entry(master, textvariable=pmonthTextVar, fg = 'grey', width = 24)
#Binds
pmonthEntry.bind('<FocusIn>', pmonthOnEntryClick)
pmonthEntry.bind('<FocusOut>', pmonthOnFocusOut)

#Day_______________________________________________________________________________________________________________________
pdayTextVar = StringVar()
pdayTextVar.set("Day")
pdayEntry = Entry(master, textvariable=pdayTextVar, fg = 'grey', width = 5)
#Binds
pdayEntry.bind('<FocusIn>', pdayOnEntryClick)
pdayEntry.bind('<FocusOut>', pdayOnFocusOut)

#Year______________________________________________________________________________________________________________________
pyearTextVar = StringVar()
pyearTextVar.set("Year")
pyearEntry = Entry(master, textvariable=pyearTextVar, fg = 'grey', width = 39)#Weird Value so that the entry widgets line up together
#Binds
pyearEntry.bind('<FocusIn>', pyearOnEntryClick)
pyearEntry.bind('<FocusOut>', pyearOnFocusOut)




#Date Accessed Code________________________________________________________________________________________________________

#Month_____________________________________________________________________________________________________________________
aDateLabel = Label(master, text = "Date Accessed:")
amonthTextVar = StringVar()
amonthTextVar.set("Month")
amonthEntry = Entry(master, textvariable=amonthTextVar, fg = 'grey', width = 24)
#Binds
amonthEntry.bind('<FocusIn>', amonthOnEntryClick)
amonthEntry.bind('<FocusOut>', amonthOnFocusOut)

#Day_______________________________________________________________________________________________________________________
adayTextVar = StringVar()
adayTextVar.set("Day")
adayEntry = Entry(master, textvariable=adayTextVar, fg = 'grey', width = 5)
#Binds
adayEntry.bind('<FocusIn>', adayOnEntryClick)
adayEntry.bind('<FocusOut>', adayOnFocusOut)

#Year______________________________________________________________________________________________________________________
ayearTextVar = StringVar()
ayearTextVar.set("Year")
ayearEntry = Entry(master, textvariable=ayearTextVar, fg = 'grey', width = 39)#Weird Value so that the entry widgets line up together
#Binds
ayearEntry.bind('<FocusIn>', ayearOnEntryClick)
ayearEntry.bind('<FocusOut>', ayearOnFocusOut)

#URL Information____________________________________________________________________________________________________________
URLLabel = Label(master, text = "URL: ")
URLTextVar = StringVar()
URLTextVar.set("URL")
URLEntry = Entry(master, textvariable=URLTextVar, fg = 'grey', width = 70)
#Binds
URLEntry.bind('<FocusIn>', URLOnEntryClick)
URLEntry.bind('<FocusOut>', URLOnFocusOut)
#___________________________________________________________________________________________________________________________



#General Book Information___________________________________________________________________________________________________

#Book_______________________________________________________________________________________________________________________
bookTitleLabel = Label(master, text = "Book Title:")
bookTextVar = StringVar()
bookTextVar.set("Book Title")
bookEntry = Entry(master, textvariable = bookTextVar, fg = "grey", width = 70)
#Binds
bookEntry.bind('<FocusIn>', bookOnEntryClick)
bookEntry.bind('<FocusOut>', bookOnFocusOut)

#Location of Publication (City)_____________________________________________________________________________________________
blocationLabel = Label(master, text = "City:")
blocationTextVar = StringVar()
blocationTextVar.set("City the book was published in")
blocationEntry = Entry(master, textvariable = blocationTextVar, fg = "grey", width = 70)
#Binds
blocationEntry.bind('<FocusIn>', blocationOnEntryClick)
blocationEntry.bind('<FocusOut>', blocationOnFocusOut)

#MLA Year of Publication___________________________________________________________________________________________________
mlabookpyearLabel = Label(master, text = "Year:")
mlabookpyearTextVar = StringVar()
mlabookpyearTextVar.set("Year")
mlabookpyearEntry = Entry(master, textvariable=mlabookpyearTextVar, fg = 'grey', width = 70)
#Binds
mlabookpyearEntry.bind('<FocusIn>', mlabookpyearOnEntryClick)
mlabookpyearEntry.bind('<FocusOut>', mlabookpyearOnFocusOut)

#Location of Publication (State)___________________________________________________________________________________________
statelocationLabel = Label(master, text = "State:")
statelocationTextVar = StringVar()
statelocationTextVar.set("State the book was published in")
statelocationEntry = Entry(master, textvariable = statelocationTextVar, fg = "grey", width = 70)
#Binds
statelocationEntry.bind('<FocusIn>', statelocationOnEntryClick)
statelocationEntry.bind('<FocusOut>', statelocationOnFocusOut)



#Cite Button_______________________________________________________________________________________________________________
citeButton = Button(master, text = "Cite It!")
citeButton.place(x = 15, y =350)
#Bind
citeButton.bind('<Button-1>', citeButtonFunction)






mlaWebsitePlaceFunction()
master.mainloop()














