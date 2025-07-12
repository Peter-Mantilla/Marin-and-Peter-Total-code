import matplotlib.pyplot as plt
import pandas as pd
import tkinter as tk
from tkinter import messagebox



dataset = {
1: '/Users/petermantilla/Documents/py_scripts/class projects/Day 8/ARPU.CSV',
2: '/Users/petermantilla/Documents/py_scripts/class projects/Day 8/Conversion.CSV',
3: '/Users/petermantilla/Documents/py_scripts/class projects/Day 8/User_Revenue.CSV',
}

#dataset[1]

#used_csv = dataset[put number here needed] 
#function to handle button click

#df1=pd.read_csv('/Users/petermantilla/Documents/py_scripts/class projects/Day 8/ARPU.CSV')

'''
def show_line_chart(data): # currently unused and here for future development
    
    df1= pd.read_csv(dataset[data])
    print(df1)
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(df1['UserID'], df1['revenueperuser'], marker='o', linestyle='-', color='b')
    ax.set_title('Revenue thingy')
    ax.set_xlabel('UserID')
    ax.set_ylabel('revenueperuser')
    ax.grid(True)
    plt.show()
'''
#show_line_chart(1)
def Bar_Thing(data):

    df1= pd.read_csv(dataset[data])
    fig, ax = plt.subplots(figsize=(12,6))
    ax.bar(df1['UserID'], df1['revenueperuser'])
    ax.set_title('NEW THING')
    ax.set_xlabel('UserID')
    ax.set_ylabel('revenueperuser')
    ax.grid(False)
    plt.xticks(rotation = 45)
    plt.tight_layout()
    plt.show()

def Bar_Graph_Grouped():
        # Load the data
    df = pd.read_csv(dataset[2])

    # Group by 'Source' and sum the 'SessionCount'
    source_totals = df.groupby('Source')['SessionCount'].sum()

    # Plot
    plt.figure(figsize=(12, 6))
    source_totals.plot(kind='bar', color='skyblue', edgecolor='black')

    plt.title('Total Session Count by Source')
    plt.xlabel('Source')
    plt.ylabel('Total Session Count')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Add value labels on top of each bar
    for index, value in enumerate(source_totals):
        plt.text(index, value + 3, str(value), ha='center', va='bottom', fontweight='bold')

    plt.show()



   

def Line_Multi_Graph():
    df = pd.read_csv(dataset[3])
    df['LastPurchaseDate'] = pd.to_datetime(df['LastPurchaseDate'], errors='coerce')
    df['ItemsPurchased'] = df['ItemsPurchased'].fillna('')
    df = df.assign(Item=df['ItemsPurchased'].str.split(',')).explode('Item')
    df['Item'] = df['Item'].str.strip()
    df = df[df['Item'] != '']
    revenue_df = df.groupby(['LastPurchaseDate', 'Item'])['TotalSpent'].sum().reset_index()
    pivot_df = revenue_df.pivot(index='LastPurchaseDate', columns='Item', values='TotalSpent').fillna(0)

    plt.figure(figsize=(12, 6))
    ax = plt.gca()  # get current axis from the figure

    pivot_df.plot(marker='*', ax=ax)  # plot on the existing axis

    plt.title('Revenue Over Time by Item Purchased')
    plt.xlabel('Date')
    plt.ylabel('Revenue ($)')
    plt.grid(True)
    plt.legend(title='Item')
    plt.tight_layout()
    plt.xticks(rotation=45)
    plt.show()

 #note funtion opens to the objectives window rather than KPI, varibles were named earlier in development and would be a hassle to change
def send_KPI_mainpage(root): # creates the second page when the more imformation button is clicked
    
    root.destroy()
    rootKPI = tk.Tk()
    rootKPI.geometry("400x300")
    rootKPI.title("Objectives")
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
    process_button = tk.Button(rootKPI, text="Process", command=lambda: process_input(KPI_pick.get(),rootKPI), font=("Helvetica", 12))
    process_button.pack(pady=10)
    rootKPI.mainloop()
    print("please work")


def process_input(user_input,root): #function used to find user selection, also checks to see if there even is text in the box
    print("test pray")
    print(user_input)
    if user_input.strip() == "":
        messagebox.showerror("Input Error", "Please enter some text.")
    elif(user_input.lower() == "profit"):
        profit_window(root)
    elif(user_input.lower() == "player growth" or user_input.lower() == "playergrowth" ):
        player_growth_window(root)
    else: 
        messagebox.showerror("Input Error", "Invalid Input")
        placeholder = user_input
        #result_label.config(text=f"Processed Text: {user_input.upper()}")

def profit_window(rootKPI): #creates the wind to select the graph you wish to view for the objective of Profit
    rootKPI.destroy()
    
    rootProfit = tk.Tk()
    rootProfit.title("Profit's KPI's")
    rootProfit.geometry("400x300")
    
    lable_ARPU = tk.Label(rootProfit, text="ARPU")
    lable_ARPU.pack(pady=2)
    
    button_ARPU = tk.Button(rootProfit, text="See Graph",command= lambda: Bar_Thing(1))
    button_ARPU.pack(pady=2)

    lable_Coversion = tk.Label(rootProfit,text="Conversion")
    lable_Coversion.pack(pady=2)

    button_Coversion = tk.Button(rootProfit, text="See Graph",command= Bar_Graph_Grouped)
    button_Coversion.pack(pady=2)

    lable_Revenue = tk.Label(rootProfit,text="Revenue")
    lable_Revenue.pack(pady=2)

    button_Revenue = tk.Button(rootProfit, text="See Graph",command= Line_Multi_Graph)
    button_Revenue.pack(pady=2)
    
    rootProfit.mainloop
    print("Profit window opened")
    

#Unfinished and non usable
def player_growth_window(rootKPI): #Unfinished
    rootKPI.destroy()
    
    rootGrowth = tk.Tk()
    rootGrowth.title("Profit's KPI's")
    rootGrowth.geometry("400x300")
    
    lable_KPI4 = tk.Label(rootGrowth, text="NaN")
    lable_KPI4.pack(pady=2)
    
    button_KPI4 = tk.Button(rootGrowth, text="See Graph",command= lambda: Bar_Thing(1))
    button_KPI4.pack(pady=2)

    lable_KPI5 = tk.Label(rootGrowth,text="NaN")
    lable_KPI5.pack(pady=2)

    button_KPI5 = tk.Button(rootGrowth, text="See Graph",command= Bar_Graph_Grouped)
    button_KPI5.pack(pady=2)

    lable_KPI6 = tk.Label(rootGrowth,text="NaN")
    lable_KPI6.pack(pady=2)

    button_KPI6 = tk.Button(rootGrowth, text="NaN",command= lambda: Line_Multi_Graph)
    button_KPI6.pack(pady=2)
    
    rootGrowth.mainloop
    print("Growth window opened")
    

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
