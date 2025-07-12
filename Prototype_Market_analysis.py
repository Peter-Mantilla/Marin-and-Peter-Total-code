import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from tkinter import messagebox


#Please note this code is a prototype and work in progress with all fetures yet to be fully implimented. 


#function to handle button click

df1=pd.read_csv('/Users/petermantilla/Documents/py_scripts/class projects/Day 8/ARPU.CSV')


def show_line_chart(): # currently unused and here for future development
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(df1['User'], df1['Money'], marker='o', linestyle='-', color='b')
    ax.set_title('Revenue thingy')
    ax.set_xlabel('User')
    ax.set_ylabel('Money')
    ax.grid(True)



def send_KPI_mainpage(root): # creates the second page when the more imformation button is clicked
    root.destroy()
    rootKPI = tk.Tk()
    rootKPI.geometry("400x300")
    rootKPI.title("KPI")
    #Im asking because each of our two 
    #Labels for objectives(objectives have yet to be implimented)
    Buisness_title1 = tk.Label(rootKPI, text="Choose from the list below")
    Buisness_title1.pack(padx=5)
    
    KPI_label1 = tk.Label(rootKPI, text="'Profit'")
    KPI_label1.pack(padx=5)

    KPI_label2 = tk.Label(rootKPI, text="'Player Growth'")
    KPI_label2.pack(padx=5)

    #KPI_label3 = tk.Label(rootKPI, text="'User Revenue'")
    #KPI_label3.pack(padx=5)
    
    

    #creates a entry box for selecting objecetives 
    KPI_pick = tk.Entry(rootKPI)
    KPI_pick.pack(pady=10)

    #processes the text in the entry box when user clicks
    process_button = tk.Button(rootKPI, text="Process", command=lambda: process_input(KPI_pick.get()), font=("Helvetica", 12))
    process_button.pack(pady=10)
    print("please work")
    rootKPI.mainloop()


def process_input(user_input): #function still developing, will be used to find user selection, also checks to see if there even is text in the box
    print("test pray")
    print(user_input)
    if user_input.strip() == "":
        messagebox.showerror("Input Error", "Please enter some text.")
    elif(user_input.lower() == "profit"):
        profit_window()
    elif(user_input.lower() == "player growth" or user_input.lower() == "playergrowth" ):
        player_growth_window()
    else: 
        messagebox.showerror("Input Error", "Invalid Input")
        placeholder = user_input
        #result_label.config(text=f"Processed Text: {user_input.upper()}")

def profit_window():
    print("PROFIT!!1")
    x=1


def player_growth_window():
    print("GROWTH!!!!")
    x=1









def main_window():
    #Create the main window
    root = tk.Tk()
    root.title("Simple Tkinter GUI")
    root.geometry("400x300")

    #Add a title label
    title_label = tk.Label(root, text="Welcome to Four Player",font=("Helvetica", 25))
    title_label.pack()

    title_label2 = tk.Label(root, text="Pong",font=("Helvetica", 50))
    title_label2.pack(pady=5)

    go_game = tk.Button(root, text="Start Game",font=("Helvetica", 12))
    go_game.pack(pady=20)

    go_KPI = tk.Button(root, text="More imformation",font=("Helvetica", 12),command=lambda: send_KPI_mainpage(root))
    go_KPI.pack(pady=20)



    '''
    currently unused code below
    #Add an entry widget for user input
    #entry_label = tk.Label(root, text="Enter some text:", font=("Helvetica",
    #12))
    #entry_label.pack(pady=5)
    #entry = tk.Entry(root, width=40)
    #entry.pack(pady=5)

    #Add a button to process the input
    #process_button = tk.Button(root, text="Process", command=process_input,
    #font=("Helvetica", 12))
    #process_button.pack(pady=10)


    #Add a label to display the result
    #result_label = tk.Label(root, text="", font=("Helvetica", 12))
    #result_label.pack(pady=10)
    '''

    #Start the Tkinter main event loop
    root.mainloop()


main_window()
