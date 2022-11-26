from tkinter import *
import PIL.Image
import PIL.ImageTk
import matplotlib.pyplot as plt
def displayInfo(chosen_topics, pages_topics, sol_potential_readers, number_pages): 

    # Pie chart, where the slices will be ordered and plotted counter-clockwise:

    labels = []
    for i in range(len(chosen_topics)):
        labels.append(chosen_topics[i] + " (" + str(pages_topics[i]) + " pages)")

    number_pages = int(number_pages)
    sizes = []
    for i in pages_topics:
        sizes.append((100*i)/number_pages)


    explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

    
    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    fig1.canvas.manager.set_window_title('Newspaper Problem Result')
    fig1.suptitle('Newspaper Problem', fontsize=14, fontweight='bold')
    ax1.set_title('Number of maximum readers: '+ str(sol_potential_readers))

    plt.show()