# Author: Aman Verma
# Description: This is a Python Desktop Application which reads the Excel and CSV datasets and
# compute correlation between the data and visualize the data using charts and plots.
# Importing various GUI and data manipulation libraries
from tkinter import *
from tkinter import messagebox
import tkinter as tk
from tkinter import filedialog as fd
import pandas as pd
from pandastable import Table
import matplotlib.pyplot as plot


# Browsing the input file
def browse():
    name = str(fd.askopenfilename(filetypes=[('Excel/CSV Files', '*.xlsx; *xls; *.csv')]))
    # If file is selected
    if (name != ""):
        messagebox.showinfo("Selected File: ", name)
        readFile(name)


# Reading the file
def readFile(loc):
    # Object of pandas table
    global pt

    # Read Excel File
    if (loc.endswith('.xlsx') or loc.endswith('.xls')):
        df = pd.read_excel(loc)
        # Put the data in the table
        pt = Table(frame, dataframe=df, showstatusbar=True, height=200)
        pt.show()
    # Read CSV File
    elif loc.endswith('.csv'):
        df = pd.read_csv(loc, header=None)
        # Put the data in the table
        pt = Table(frame, dataframe=df, showstatusbar=True, height=200)
        pt.show()

    btnCor['state'] = tk.NORMAL
    btnRankCor['state'] = tk.NORMAL
    # Draw the table in case multiple files are being opened using the application
    pt.redraw()


# For computation of Karl Pearson Correlation with the selected data from the table
def karlCor():
    data = pt.getSelectedDataFrame()
    if data.empty:
        messagebox.showerror("Karl Pearson Correlation (Coefficients)", "Data not Selected.")
    else:
        res = data.corr(method="pearson")
        print(res.to_string())
        # messagebox.showinfo("Karl Pearson Correlation (Coefficients)", res.to_string())
        showRes(res.to_string())


# For computation of Rank Correlation with the selected data from the table
def rankCor():
    data = pt.getSelectedDataFrame()
    if data.empty:
        messagebox.showerror("Rank Correlation (Coefficients)", "Data not Selected.")
    else:
        res = data.corr(method="spearman")
        print(res.to_string())
        # messagebox.showinfo("Rank Correlation (Coefficients)", res.to_string())
        showRes(res.to_string())


# For displaying the correlation results in a new window withd double scroll view
def showRes(resStr):
    rootRes = Tk()
    rootRes.title("Result")
    rootRes.minsize(300, 100)
    rootRes.maxsize(500, 300)

    # Create horizontal and vertical scroll bars
    SVBar = tk.Scrollbar(rootRes)
    SVBar.pack(side=tk.RIGHT, fill="y")
    SHBar = tk.Scrollbar(rootRes, orient=tk.HORIZONTAL)
    SHBar.pack(side=tk.BOTTOM, fill="x")

    # Put the result in the Box
    TBox = tk.Text(rootRes, yscrollcommand=SVBar.set, xscrollcommand=SHBar.set, wrap="none", font=('Consolas', 10))
    TBox.pack(expand=0, fill=tk.BOTH, padx=10, pady=10)
    TBox.insert(tk.END, resStr)

    # Configure the scrollbars
    SHBar.config(command=TBox.xview)
    SVBar.config(command=TBox.yview)

    rootRes.mainloop()


# Enable the Visualize button when any radio button is pressed
def enableVis():
    if (btnVisual['state'] == tk.DISABLED):
        btnVisual['state'] = tk.NORMAL


# For visualizing the data using plots and charts
def visualizeData():
    # Get the dataset and the visualization option
    opt = str(option.get())
    data = pt.getSelectedDataFrame()

    if data.empty:
        messagebox.showerror("Data Visualization", "No Data Selected.")
        return

    # To plot the charts and bars we need numerical values only
    numericCols = []

    # Getting the columns which contain numeric values
    cols = data.columns.tolist()
    for col in cols:
        cells = data[col].tolist()
        dt = type(cells[0])
        if (dt == int or dt == float):
            numericCols.append(col)

    # Visualizing data according to the option
    if (opt == "1"):
        # Getting the first two numeric columns for scatter plot
        x = data[numericCols[0]].tolist()
        y = data[numericCols[1]].tolist()
        plot.scatter(x, y)
        plot.xlabel(numericCols[0])
        plot.ylabel(numericCols[1])
        plot.title('Scatter Plot')
        plot.show()
    elif (opt == "2"):
        # The first numeric column is plotted in histogram
        x = data[numericCols[0]].tolist()
        plot.hist(x, stacked=False)
        plot.xlabel(numericCols[0])
        plot.title('Histogram')
        plot.show()
    elif (opt == "3"):
        # Getting the first two numeric columns for line plot and sorting the data before plotting
        data.sort_values(by=[numericCols[0], numericCols[1]], inplace=True)
        x = data[numericCols[0]].tolist()
        y = data[numericCols[1]].tolist()
        plot.plot(x, y)
        plot.xlabel(numericCols[0])
        plot.ylabel(numericCols[1])
        plot.title('Line Plot')
        plot.show()
    elif (opt == "4"):
        # Getting the first two numeric columns for bar chart
        x = data[numericCols[0]].tolist()
        y = data[numericCols[1]].tolist()
        plot.bar(x, y, width=0.2)
        plot.xlabel(numericCols[0])
        plot.ylabel(numericCols[1])
        plot.title('Bar Chart')
        plot.show()
    elif (opt == "5"):
        # The first numeric column is used as label and second numeric column is used in the chart
        x = data[numericCols[0]].tolist()
        y = data[numericCols[1]].tolist()
        plot.pie(y, labels=x)
        plot.xlabel(numericCols[0])
        plot.title('Pie Chart')
        plot.show()


# Setting up GUI widgets
root = Tk()
root.title('Correlation using Python')
root.minsize(600, 650)
root.maxsize(600, 650)

infoLabel = Label(root, text='Select Excel/CSV file', font=('Calibri', 16))
infoLabel.pack(pady=10)

browseBtn = Button(root, text='Browse', command=browse)
browseBtn.pack(pady=5)

frame = tk.Frame(root)
frame.pack(fill='both', pady=10)

frameBtn = tk.Frame(root)
frameBtn.pack(fill="x", side="bottom", pady=10)

instr = Label(frameBtn, text="Select Data from table and perform following operations")
instr.pack(pady=5)

btnCor = Button(frameBtn, text="Karl-Pearson Correlation", command=karlCor, state=tk.DISABLED)
btnCor.pack(pady=5)

btnRankCor = Button(frameBtn, text="Rank Correlation", command=rankCor, state=tk.DISABLED)
btnRankCor.pack(pady=5)

top = Frame(frameBtn)
bottom = Frame(frameBtn)
top.pack(side=TOP)
bottom.pack(side=BOTTOM, fill=BOTH, expand=True)

option = IntVar()
r1 = Radiobutton(root, text="Scatter Plot", variable=option, value=1, command=enableVis)
r1.pack(in_=top, side=LEFT)
r2 = Radiobutton(root, text="Histogram", variable=option, value=2, command=enableVis)
r2.pack(in_=top, side=LEFT)
r3 = Radiobutton(root, text="Line Plot", variable=option, value=3, command=enableVis)
r3.pack(in_=top, side=LEFT)
r4 = Radiobutton(root, text="Bar Chart", variable=option, value=4, command=enableVis)
r4.pack(in_=top, side=LEFT)
r5 = Radiobutton(root, text="Pie Chart", variable=option, value=5, command=enableVis)
r5.pack(in_=top, side=LEFT)

btnVisual = Button(frameBtn, text="Visualization", command=visualizeData, state=tk.DISABLED)
btnVisual.pack(pady=5)

btnQuit = Button(frameBtn, text="Quit", command=root.destroy)
btnQuit.pack(pady=5)

# Starting the Tkinter application
root.mainloop()
