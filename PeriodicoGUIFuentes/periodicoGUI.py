from tkinter import *
import PIL.Image
import PIL.ImageTk
from EntryWithPlaceholder import EntryWithPlaceholder
from Periodico import periodico

main_window = Tk()
# Define image background
background_image= PIL.Image.open("PeriodicoGUIFuentes/images/background.png")
newspaper_photo = PIL.ImageTk.PhotoImage(background_image)

# Frame with background image
label = Label(main_window, image=newspaper_photo)
label.image = newspaper_photo
frame = Frame(label, bg="")
frame.place(width=800, height=700)  
label.pack(fill="both", expand=True)

# Frame of form
form = Frame(frame,bg="white", width=500,height=700)
form.place(x=150,y=120)

#Title: newspaper problem
title = Label(form, text="Newspaper problem", bg="#fff",fg="#765706", font='Helvetica 15 bold')
title.place(relx=0.5, y=30,anchor=CENTER)

#Topics
topics = Label(form, text="Topics:", bg="#fff",fg="#765706", font='Helvetica 12')
topics_field = EntryWithPlaceholder(form, "International, National, Local, Sport, Culture")
topics.place(x=50, y=50)
topics_field.place(x=50, y=80, width=400, height=40)
topics_field.configure(highlightbackground="#CCCCCC", highlightcolor="#CCCCCC")

#Minimum number of pages
min_nb_pages = Label(form, text="Minimum number of pages per topic:", bg="#fff", fg="#765706", font='Helvetica 12')
min_nb_field = EntryWithPlaceholder(form, "2,3,4,5,6")
min_nb_pages.place(x=50, y=140)
min_nb_field.place(x=50, y=170, width=400, height=40)
min_nb_field.configure(highlightbackground="#CCCCCC", highlightcolor="#CCCCCC")

#Maximum number of pages
max_nb_pages = Label(form, text="Maximum number of pages per topic:", bg="#fff", fg="#765706", font='Helvetica 12')
max_nb_field = EntryWithPlaceholder(form, "3,5,6,7,8")
max_nb_pages.place(x=50, y=230)
max_nb_field.place(x=50, y=260, width=400, height=40)
max_nb_field.configure(highlightbackground="#CCCCCC", highlightcolor="#CCCCCC")

#Potential readers 
potential_readers = Label(form, text="Potential readers", bg="#fff", fg="#765706", font='Helvetica 12')
potential_readers_field = EntryWithPlaceholder(form, "2000, 3000, 4000, 5000, 6000")
potential_readers.place(x=50, y=320)
potential_readers_field.place(x=50, y=350, width=400, height=40)
potential_readers_field.configure(highlightbackground="#CCCCCC", highlightcolor="#CCCCCC")

#Number of pages
number_pages = Label(form, text="Number of pages", bg="#fff", fg="#765706", font='Helvetica 12')
number_pages_field = EntryWithPlaceholder(form, "10")
number_pages.place(x=50, y=410)
number_pages_field.place(x=50, y=440, width=400, height=40)
number_pages_field.configure(highlightbackground="#CCCCCC", highlightcolor="#CCCCCC")


solve_button = Button(text="Solve", borderwidth=0, bg="#00A8E7", fg="white", command=lambda: periodico(number_pages_field.get(), topics_field.get(), min_nb_field.get(), max_nb_field.get(), potential_readers_field.get()))
solve_button.place(x=370, y=620)

main_window.geometry("800x800")
main_window.title('Newspaper Problem')
main_window.mainloop()