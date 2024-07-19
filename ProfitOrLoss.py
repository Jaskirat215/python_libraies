class Company:
    def __init__(self, totalrevenue, totalexpenses):
        self.totalrevenue = totalrevenue
        self.totalexpenses = totalexpenses

    def calculate(self):
        return self.totalrevenue - self.totalexpenses

    def printdetails(self):
        print(f"Total Revenue: {self.totalrevenue}")
        print(f"Total Expenses: {self.totalexpenses}")
        profitorloss = self.calculate()
        if profitorloss > 0:
            print(f"The company made a profit of: ",profitorloss)
        elif profitorloss < 0:
            print(f"The company incurred a loss of: ",-profitorloss)
        else:
            print("The company broke even (no profit, no loss).")

totalrevenue = float(input("Enter the total revenue of the company: "))
totalexpenses = float(input("Enter the total expenses of the company: "))
company = Company(totalrevenue, totalexpenses)
print("\nCompany Financial Details:")
company.printdetails()
