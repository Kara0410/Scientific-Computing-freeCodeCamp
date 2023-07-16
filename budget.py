class Category:
    def __init__(self, category: str):

        # list of categories
        self.category_list = ["Food", "Clothing", "Entertainment"]
        self.ledger = []
        # balance of the category
        self.balance = 0

        # if category doesn't exist create it
        if category in self.category_list:
            self.category = category
        else:
            self.category_list.append(category)
            self.category = category

    def deposit(self, amount: float, description: str = ""):
        self.balance += amount
        return self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount: float, description: str = ""):
        if self.check_funds(amount=amount) is True:
            self.balance -= amount
            self.balance = round(self.balance, 2)
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return self.balance

    def transfer(self, amount: float, rec_category: object):
        if self.check_funds(amount=amount) is True:
            # transfers from the "self" category the amount x to rec_category.category,
            # which is the name of the other category
            self.withdraw(amount=amount, description=f"Transfer to {rec_category.category}")
            rec_category.deposit(amount, f"Transfer from {self.category}")
            return True
        else:
            return False

    def check_funds(self, amount):
        if amount > self.balance:
            return False
        else:
            return True

    def __str__(self) -> str:

        # Adding the title to the print line
        print_line = f"{self.category.center(30, '*')}\n"

        # Print the ledger items
        for transfer in self.ledger:
            transfer_des = transfer["description"]
            # adjusting the lenght of the current transfer description
            if len(transfer_des) <= 23:
                description = f"{transfer_des}" + " " * (23 - len(transfer_des))
            else:
                description = transfer_des[:23]

            amount = '{:.2f}'.format(transfer['amount']).rjust(7)
            transfer_line = f"{description}{amount}\n"
            print_line += transfer_line

        # Print the category total
        total = '{:.2f}'.format(self.balance)
        total_line = f"Total: {total}"

        return print_line + total_line


def create_spend_chart(categories: object):
    # Calculate the total amount spent by each category
    category_spending = {}
    total_spending = 0

    for category in categories:
        spending = 0
        for each_transfer in category.ledger:
            # check if the amount of transfer was an withdraw
            if each_transfer['amount'] < 0:
                spending -= each_transfer['amount']
        category_spending[category.category] = round(spending, 2)
        total_spending += spending

    # Calculate the percentage spent by each category
    category_percentages = {}
    for category in categories:
        percentage = (category_spending[category.category] / total_spending) * 100
        category_percentages[category.category] = round(percentage, 2)

    # Create the bar chart
    chart = "Percentage spent by category\n"
    for i in range(100, -10, -10):
        chart += str(i).rjust(3) + "| "
        for category in categories:
            if category_percentages[category.category] >= i:
                chart += "o  "
            else:
                chart += "   "
        chart += "\n"

    # Add the horizontal line and category names
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    max_category_name_length = max(len(category.category) for category in categories)
    for i in range(max_category_name_length):
        chart += "     "
        for category in categories:
            if i < len(category.category):
                chart += category.category[i] + "  "
            else:
                chart += "   "
        if i != max_category_name_length - 1:
            chart += "\n"

    return chart
