import tkinter as tk
from tkinter import *
import scipy.stats as st
from scipy.stats import norm, t, chi2


def initNormalGUI():
    frameNormal.pack(pady=10)
    frameChiSq.pack_forget()
    frameT.pack_forget()
    btnNormal.configure(bg='green')
    btnChiSq.configure(bg='#f0f0ed')
    btnT.configure(bg='#f0f0ed')


def initChiSqGUI():
    frameNormal.pack_forget()
    frameChiSq.pack(pady=10)
    frameT.pack_forget()
    btnNormal.configure(bg='#f0f0ed')
    btnChiSq.configure(bg='green')
    btnT.configure(bg='#f0f0ed')


def initTGUI():
    frameNormal.pack_forget()
    frameChiSq.pack_forget()
    frameT.pack(pady=10)
    btnNormal.configure(bg='#f0f0ed')
    btnChiSq.configure(bg='#f0f0ed')
    btnT.configure(bg='green')


def normalP():
    z_score = float(enter_z.get())
    p = norm.sf(abs(z_score)) * 2
    res_p1.delete(0, END)
    res_p1.insert(0, str(p))


def Chi2P():
    t_value = float(enter_chi.get())
    df_value = float(enter_dfC.get())
    p = chi2.sf(abs(t_value), df=df_value)
    res_p2.delete(0, END)
    res_p2.insert(0, str(p))


def tProb():
    t_value = float(enter_T.get())
    df_value = float(enter_dfT.get())
    p = t.sf(abs(t_value), df=df_value) * 2
    res_p3.delete(0, END)
    res_p3.insert(0, str(p))


root = Tk()
root.minsize(500, 400)
root.title("Distribution and Probability")

title = Label(
    root, text='Interpreting P-Values', font=('Segoe UI', 16))
title.pack(pady=15)

# Choosing Calculator
optFrame = Frame(root)
optFrame.pack()

btnNormal = Button(optFrame, text='Normal Distribution',
                   command=initNormalGUI, font=('Segoe UI', 12))
btnNormal.grid(row=0, column=0, padx=5)

btnChiSq = Button(optFrame, text='Chi-Square Distribution',
                  font=('Segoe UI', 12), command=initChiSqGUI)
btnChiSq.grid(row=0, column=1, padx=5)

btnT = Button(optFrame, text='T Distribution',
              command=initTGUI, font=('Segoe UI', 12))
btnT.grid(row=0, column=2, padx=5)

# Calculators Window
calcFrame = Frame(root, width=350, height=100)
calcFrame.pack(pady=10)

# Normal Calculator
frameNormal = Frame(calcFrame)

label_z = Label(frameNormal, text='Z-Score ', font=('Segoe UI', 12))
label_z.grid(row=1, column=0, pady=5)
enter_z = Entry(frameNormal, font=('Segoe UI', 12))
enter_z.grid(row=1, column=1, pady=5)

calcBtn1 = Button(frameNormal, text='Calculate', font=('Segoe UI', 12), command=normalP)
calcBtn1.grid(row=2, column=1, pady=5)

label_p1 = Label(frameNormal, text='Net Probability ', font=('Segoe UI', 12))
label_p1.grid(row=3, column=0, pady=5)
res_p1 = Entry(frameNormal, font=('Segoe UI', 12))
res_p1.grid(row=3, column=1, pady=5)

# Chi-Sq Calculator
frameChiSq = Frame(calcFrame)

label_chi = Label(frameChiSq, text='Chi Value ', font=('Segoe UI', 12))
label_chi.grid(row=1, column=0, pady=5)
enter_chi = Entry(frameChiSq, font=('Segoe UI', 12))
enter_chi.grid(row=1, column=1, pady=5)

label_dfC = Label(frameChiSq, text='Degree of Freedom ', font=('Segoe UI', 12))
label_dfC.grid(row=2, column=0, pady=5)
enter_dfC = Entry(frameChiSq, font=('Segoe UI', 12))
enter_dfC.grid(row=2, column=1, pady=5)

calcBtn2 = Button(frameChiSq, text='Calculate', font=('Segoe UI', 12), command=Chi2P)
calcBtn2.grid(row=3, column=1, pady=5)

label_p2 = Label(frameChiSq, text='Net Probability ', font=('Segoe UI', 12))
label_p2.grid(row=4, column=0, pady=5)
res_p2 = Entry(frameChiSq, font=('Segoe UI', 12))
res_p2.grid(row=4, column=1, pady=5)

# T Calculator
frameT = Frame(calcFrame)

label_T = Label(frameT, text='T Value ', font=('Segoe UI', 12))
label_T.grid(row=1, column=0, pady=5)
enter_T = Entry(frameT, font=('Segoe UI', 12))
enter_T.grid(row=1, column=1, pady=5)

label_dfT = Label(frameT, text='Degree of Freedom ', font=('Segoe UI', 12))
label_dfT.grid(row=2, column=0, pady=5)
enter_dfT = Entry(frameT, font=('Segoe UI', 12))
enter_dfT.grid(row=2, column=1, pady=5)

calcBtn3 = Button(frameT, text='Calculate', font=('Segoe UI', 12), command=tProb)
calcBtn3.grid(row=3, column=1, pady=5)

label_p3 = Label(frameT, text='Net Probability ', font=('Segoe UI', 12))
label_p3.grid(row=4, column=0, pady=5)
res_p3 = Entry(frameT, font=('Segoe UI', 12))
res_p3.grid(row=4, column=1, pady=5)

root.mainloop()
