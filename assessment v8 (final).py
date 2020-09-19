#--- v1: basic program that had no validation and no dropdown ---#
#--- v2: basic program that had dropdown menus for colour ---#
#--- v3: program with validation for integers, and a dropdown menu for licence ---#
#--- v4: program with validation for special characters ---#
#--- v5: program that validates for negative integers ---#
#--- v6: added a label that changes colour when hovered over ---#
#--- v7: added a link to the label that changes colour (help feature) ---#
#--- v8 (final version): changed placing and size of labels and buttons ---#


from tkinter import *

import tkinter
import tkinter.messagebox
import string #imports punctuation set
import webbrowser #imports the browser, so when the link it clicked it goes straight to the browser

class Image:
    def __init__(self, id_i, filename_i, title_i, owner_i, licence_i, colour_i, form_i):
        self.id = id_i
        self.filename = filename_i
        self.title = title_i
        self.owner = owner_i
        self.licence = licence_i
        self.colour = colour_i
        self.form = form_i
        self.type= 'images'

    def get_id(self):
        return self.id

    def get_filename(self):
        return self.filename

    def get_title(self):
        return self.title

    def get_owner(self):
        return self.owner

    def get_licence(self):
        return self.licence

    def get_colour(self):
        return self.colour

    def get_form(self):
        return self.form



#create the GUI interface
class GUI:

    def __init__(self):

        window = Tk()
        window.title("Image Data Entry")
        window.minsize(width=340, height=250) #this window size is small and compact to fit all my fields, labels and buttons in.

        self.ready_to_write = False
        self.recordlist = []



#--------------set up of fields--------------#


        id_label = Label(window, text='Image ID').grid(row=0, pady = ("10","0"))
        filename_label = Label(window, text='Filename').grid(row=1)
        title_label = Label(window, text='Title').grid(row=2)
        owner_label = Label(window, text='Owner').grid(row=3, pady= ("5"))
        licence_label = Label(window, text='Licence (Attribution)').grid(row=4)
        colour_label = Label(window, text='Colour Depth').grid(row=5)

        #set up of the dropdown menus
        global form
        form = StringVar(window)
        form.set(".jpg")

        global licence
        licence = StringVar(window)
        licence.set("Attribution alone")

        global colour
        colour = StringVar(window)
        colour.set("Grayscale")

        self.id_field = Entry(window)
        self.filename_field = Entry(window)
        self.form_field = OptionMenu(window, form, ".jpg", ".png", ".gif", ".bmp")
        self.title_field = Entry(window)
        self.owner_field = Entry(window)
        self.licence_field = OptionMenu(window, licence,"Attribution alone", "+ Share-alike", "+ Non-Commercial", "+ No Derivatives",  "+ Share-alike, + Non-Commercial", "+ Non-Commericial, + No Derivatives")
        self.licence_field.config(width = "10") #when an option that has more than 10 characters is selected, the window size doesn't change to suit this.
        self.colour_field = OptionMenu(window, colour, "Grayscale", "Colour", "Monochrome")

        #validate button changes to a darker blue when clicked on it, csv button changes to grey when clicked        
        validate_button = Button(window,text='Validate', command=self.doSubmit, fg = 'white', bg = '#4d79ff', width = "15", activebackground = '#3e68e8', activeforeground = 'white')
        validate_button.config( fg = 'white')
        csv_button = Button(window, text= "Write to CSV", command = self.writetocsv, width = "15", activebackground = '#D0D0D0')


        self.id_field.grid(row=0, column=1, pady = ("10","0"))
        self.filename_field.grid(row=1, column=1)
        self.form_field.grid(row=1, column=2)
        self.title_field.grid(row=2, column=1)
        self.owner_field.grid(row=3, column=1)
        self.licence_field.grid(row=4, column=1, sticky="ew") #the 'sticky="ew"' makes the licence dropdown menu and colour dropdown the same width as the entry fields.
        self.colour_field.grid(row=5, column=1, sticky="ew")
        validate_button.place (relx=0.3, rely=0.9, anchor=CENTER)
        csv_button.place (relx=0.7, rely=0.9, anchor=CENTER)

    #----help events. This is the extra feature---------------------------------------------#

        def darkgray_text(event=None):
            helpbutton.config(fg="#585858") #changes to a dark grey colour when the label is hovered over 

        def gray_text(event=None):
            helpbutton.config(fg="#A9A9A9") #default colour is a light grey, so it doesn't stand out too much, but enough for a user to see it when they need help

        def callback(event):
            webbrowser.open_new(r"https://creativecommons.org/licenses/") #help link to the creative commons website, with more info about the types of licenses

        helpbutton = Label(window,text="What is this?", font =(None,8))

        helpbutton.bind("<Enter>",darkgray_text)
        helpbutton.bind("<Leave>",gray_text)
        helpbutton.bind("<Button-1>",callback)
        helpbutton.place(relx=0.85, rely=0.52, anchor=CENTER) #placed next to the licence field for convenience

        window.mainloop()

##------ event --------------------------------------------------#



    def doSubmit(self):
        #this is the callback method for the 'Submit' button

        #makes sure user enters values for all fields
        if len(self.id_field.get()) <1 or len(self.filename_field.get()) <1 or len(self.title_field.get()) <1 or len(self.owner_field.get()) <1:
            tkinter.messagebox.showwarning('Warning','Please enter a value for all fields.')

        #splits and counts the number of items given for these fields, and puts into an array
        filename = self.filename_field.get().split()
        name = self.owner_field.get().split()
        title = self.title_field.get().split()

        items_for_filename = len(filename)
        items_for_name = len(name)
        items_for_title = len(title)

        #only allows the "-" to be put in. "-" is the most commonly used character in filenames, so I restricted it to only this particular character
        invalidChars = set(string.punctuation.replace("-","_"))
        invalidChars2 = set(string.punctuation)



        #if the count of items is 0 in the array, the user will be told to put in more characters 
        if items_for_name == 0 or items_for_title == 0 or items_for_filename == 0:
            tkinter.messagebox.showwarning('Warning','Please put more letters or numbers in for either the filename, title or owner.')

        #doesn't allow any other special character except for the '-' character for the filename
        elif any(char in invalidChars for char in self.filename_field.get()):
            tkinter.messagebox.showwarning('Warning',"Only '-' characters allowed for the Filename.")

        #doesn't allow for any special characters for the owner name. Owner name doesn't accept names with 2 parts, eg Mary-jane, but will accept 'Maryjane'
        elif any(char in invalidChars2 for char in self.owner_field.get()):
            tkinter.messagebox.showwarning('Warning',"No special characters in the Owner name.")

        #if user puts only spaces and digits, the program tells user to put in at least one alphabetical letter as well.
        elif all(x.isspace() or x.isdigit() for x in self.owner_field.get()):
            tkinter.messagebox.showinfo('Notice','You can include integers in the owner field, however you must accompany them with letters as well.')

        #if user puts only digits, they will be told to put in an alphabetical letter as well.
        elif (self.owner_field.get().isdigit()) or (self.title_field.get().isdigit()):
            tkinter.messagebox.showwarning('Warning',"Integers must be accompanied with an alphabetical letter for the Owner and Title fields.")

        else:
            
            #only allows integer input for the image id field. once validation is all complete, message will pop up saying the values are accepted.
            try:
                validated_id = int(self.id_field.get())
                id_float = float(self.id_field.get())

                #program checks if the integer put in is negative. If it's negative, the program tells user to type in a bigger number than 0. Must also be an integer.
                if id_float < 0:
                    tkinter.messagebox.showinfo('Notice', 'ID number(s) must be more than 0.')
                else:
                    self.ready_to_write= True #the program is now ready to write the csv
                    tkinter.messagebox.showinfo('Notice','Submission successful.')
                    self.recordlist.append(Image(self.id_field.get(),self.filename_field.get(),  form.get(), self.title_field.get(), self.owner_field.get(), licence.get(), colour.get()))
            

            except:
                tkinter.messagebox.showwarning('Warning','Please enter an integer for the ID number.')
                self.id_field.delete(0, END)#this deletes the incorrect input, so users can type in a different values straight away


    def writetocsv(self):
        #this is the callback method for the 'write to csv' button

        import csv
        file_name = 'imagesinfo.csv'

        if self.ready_to_write:
            ofile = open(file_name, 'a') #'a' means it appends the data in, so it won't erase the previous data that has been put in.
            writer = csv.writer(ofile, delimiter=',', lineterminator = '\n')
            tkinter.messagebox.showinfo("Notice",file_name+ " has been opened and edited successfully.")

            for record in self.recordlist:
                writer.writerow([record.get_id(),record.get_filename(), record.get_form(), record.get_title(),record.get_owner(), record.get_licence(), record.get_colour()])

            #the commands to clear the fields. Done at the end just before "write to csv" is pressed and after "submit" is pressed, just in case any last min changes are made
                self.id_field.delete(0, END)
                self.filename_field.delete(0, END)
                self.title_field.delete(0, END)
                self.owner_field.delete(0, END)

            ofile.close()

        else:
            tkinter.messagebox.showwarning('Warning', 'You need to validate your data.')

        self.ready_to_write= False


#initialises the programme
GUI()
