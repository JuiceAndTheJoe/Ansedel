from tkinter import *
from tkinter import messagebox

from PIL import Image, ImageDraw, ImageFont

# GUI properties, ofta använda siffror
root = Tk()
root.title('Fyll ansedel - Ulla Kron')
root.geometry("800x790")
left = 110
right = 350

# Add text to font
def add_it():    
    my_image = Image.open("ansedel.png")
    text_font = ImageFont.truetype("georgia.ttf", 31)
    child_font = ImageFont.truetype("georgia.ttf", 25)
    edit_image = ImageDraw.Draw(my_image)

    # innehåller variabelnamn och textposition (x,y) för personen
    varDict = { 
    name_entry: (left, 95), nr_entry: (520, 95), 
    dad_entry: (left, 155), mom_entry: (left, 215), 
    when_entry: (left, 275), where_entry: (right, 275), 
    dop_entry: (left, 335), faddrar_entry: (left, 395), 
    faddrar_entry2: (left, 455), gift_entry: (left, 510),
    g_where_entry: (right, 510), partner_entry:(left, 570), 
    dead_entry: (left, 630), d_where_entry:(right, 630), 
    bury_entry: (left, 690), job_entry: (left, 750)
    }
    for i, j in varDict.items(): # för varje variabel och dess (x,y); lägg den på plats i ansedeln
        entry = i.get()
        edit_image.text((j), entry, ("black"), font=text_font)
    
    # samma procedur för barnen, ville ha lite mindre teckenstorlek - därav separat dict & loop.
    barnDict = {    
    ch_entry1: (left-50, 810), ch_entry2: (left-50, 837),
    ch_entry3: (left-50, 864), ch_entry4: (left-50, 891),
    ch_entry5: (right, 810), ch_entry6: (right, 837),
    ch_entry7: (right, 864), ch_entry8: (right, 891)
    }
    for i, j in barnDict.items():
        child = i.get()
        edit_image.text((j), child, ("black"), font=child_font)

    my_image.save(str(name_entry.get()) + ".png")    
    messagebox.showinfo("Ansedel skapad", "Ansedel för " + str(name_entry.get()) + " har skapats. Filnamn: " + str(name_entry.get()) + ".png")
    
    for i in varDict:
        i.delete(0, END)    # tömmer inmatningsfälten
    for i in barnDict:
        i.delete(0,END)

# Text labels
titel = Label(root, text="Fyll ansedel - Ulla Kron", font=("Segoe UI", 24))
titel.pack()

def labels(a, eks, why):    #tar in argument för text, x och y och skapar labels.
   a = Label(root, text=a, font=("Segoe UI", 16))
   a.place(x = eks, y = why)

label_tuples = [("Namn:", 15, 70),    ("Nr:", 660, 70),    
                ("Fader:", 15, 110),    ("Moder:", 15, 150),    
                ("Född:", 15, 190),    ("Ort:", 500, 190),    
                ("Döpt:", 15, 230),    ("Faddrar:", 15, 270),    
                ("Gift:", 15, 330),    ("Ort:", 500, 330),    
                ("Partner:", 15, 370),    ("Död:", 15, 410),    
                ("Ort:", 500, 410),    ("Begravd:", 15, 450),    
                ("Titel/Yrke:", 15, 490),    ("Barn:", 15, 530),    
                ("1.", 20, 570),    ("2.", 20, 610),    
                ("3.", 20, 650),    ("4.", 20, 690),    
                ("5.", 400, 570),    ("6.", 400, 610),    
                ("7.", 400, 650),    ("8.", 400, 690),]

for label_text, x, y in label_tuples:
    labels(label_text, x, y)


entries = [("name_entry", 100, 70), ("nr_entry", 700, 70),            
           ("dad_entry", 100, 110), ("mom_entry", 100, 150),           
           ("when_entry", 100, 190), ("where_entry", 550, 190),           
           ("dop_entry", 100, 230), ("faddrar_entry", 100, 270),           
           ("faddrar_entry2", 330, 270), ("gift_entry", 100, 330),           
           ("g_where_entry", 550, 330), ("partner_entry", 100, 370),           
           ("dead_entry", 100, 410), ("d_where_entry", 550, 410),           
           ("bury_entry", 110, 450), ("job_entry", 120, 490),           
           ("ch_entry1", 55, 570), ("ch_entry2", 55, 610),           
           ("ch_entry3", 55, 650), ("ch_entry4", 55, 690),           
           ("ch_entry5", 430, 570), ("ch_entry6", 430, 610),           
           ("ch_entry7", 430, 650), ("ch_entry8", 430, 690)]

for entry in entries:
    entry_widget = Entry(root, font=("Segoe UI", 16))
    entry_widget.place(x=entry[1], y=entry[2])
    locals()[entry[0]] = entry_widget

# klar-knapp
my_button = Button(root, text="Klart", command=add_it, font=("Segoe UI", 20), background="#20a39e", foreground="white")
my_button.place(x=700, y=680)

root.mainloop()