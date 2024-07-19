class Company:
    def __init__(self, total_revenue, total_expenses, tax_rate):
        self.total_revenue = total_revenue
        self.total_expenses = total_expenses
        self.tax_rate = tax_rate

    def calculate_profit_loss(self):
        return self.total_revenue - self.total_expenses

    def calculate_tax(self):
        tax = self.calculate_profit_loss()
        return  self.tax_rate * tax

    def print_details(self):
        print(f"Total Revenue: {self.total_revenue}")
        print(f"Total Expenses: {self.total_expenses}")
        profit_or_loss = self.calculate_profit_loss()
        if profit_or_loss > 0:
            print(f"The company made a profit of: ", profit_or_loss)
        elif profit_or_loss < 0:
            print(f"The company incurred a loss of: ", -profit_or_loss)
        else:
            print("The company broke even (no profit, no loss).")
        total_tax = self.calculate_tax()
        print(f"Total Tax: {total_tax}")

total_revenue = float(input("Enter the total revenue of the company: "))
total_expenses = float(input("Enter the total expenses of the company: "))
tax_rate = float(input("Enter the tax rate (as a decimal) : "))
company = Company(total_revenue, total_expenses, tax_rate) 

print("\nCompany Financial Details:")
company.print_details()
