"""
    CS121 W18
    INVESTMENT CALCULATOR
    PYTHON 3.6.4
"""

from tkinter import *  # import all definitions from tkinter


class InvestmentCalc:
    def __init__(self):
        window = Tk()  # create window
        window.title("Investment Calculator")  # set title

        Label(window, text="Investment Amount").grid(row=1, column=1, sticky=W)
        Label(window, text="Years").grid(row=2, column=1, sticky=W)
        Label(window, text="Annual Interest Rate").grid(
            row=3, column=1, sticky=W)
        Label(window, text="Future Value").grid(row=4, column=1, sticky=W)

        self.investmentAmountVar = StringVar()
        Entry(window, textvariable=self.investmentAmountVar,
              justify=RIGHT).grid(row=1, column=2)
        self.yearsVar = StringVar()
        Entry(window, textvariable=self.yearsVar,
              justify=RIGHT).grid(row=2, column=2)
        self.annualInterestRateVar = StringVar()
        Entry(window, textvariable=self.annualInterestRateVar,
              justify=RIGHT).grid(row=3, column=2)

        self.futureValueVar = StringVar()
        lblFutureValue = Label(window, textvariable=self.futureValueVar).grid(
            row=4, column=2, sticky=E)
        btCalculate = Button(window, text="Calculate", command=self.calcValue).grid(
            row=6, column=2, sticky=E)

        window.mainloop()  # create event loop

    def calcValue(self):
        futureValue = self.getFutureValue(float(self.investmentAmountVar.get()), float(
            self.annualInterestRateVar.get()) / 1200, int(self.yearsVar.get()))
        self.futureValueVar.set(format(futureValue, "10.2f"))

    def getFutureValue(self, investmentAmount, monthlyInterestRate, years):
        futureValue = investmentAmount * \
            ((1 + monthlyInterestRate) ** (years * 12))
        return futureValue


InvestmentCalc()  # create GUI
