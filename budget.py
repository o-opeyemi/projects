# Categories
class Category:
    # Instances to be created by default for each categories
    def __init__(self, category):
        self.category = category
        self.ledger = []
    
    # To get the overall transactions in a category
    def __str__(self):
        title = ""
        category_length = len(self.category)
        stars_needed = 30 - category_length
        initial_star_count = stars_needed//2
        initial_stars = "*" * initial_star_count
        final_stars = "*" * (stars_needed - initial_star_count)
        title += initial_stars + self.category + final_stars
        for i in self.ledger:
            amount = i["amount"]
            description = i["description"]
            amount_length = len(str(amount))
            description_length = len(str(description))
            max_description_length = 30 - amount_length
            if description_length > max_description_length:
                description = description[0:max_description_length-3] + "..."
                spaces = ""
            else:
                spaces = " " * (max_description_length - description_length)
            transaction_line = description + spaces + str(amount)
            title += "\n" + transaction_line
        total = "Total: " + str(self.get_balance())
        title += "\n" + total
        return title
    
    # To get the name of the category in strings
    def name(self):
        return self.category

    # Desposit function
    def deposit(self, amount, description=""):
        deposit_data = {}
        deposit_data["amount"] = amount
        deposit_data["description"] = description
        self.ledger.append(deposit_data)
        return self.ledger
    
    # Withdrawal function
    def withdraw(self, amount, description=""):
        balance = self.get_balance()
        if amount <= balance:
            withdraw_amount = float("-" + str(amount))
            withdraw_data = {}
            withdraw_data["amount"] = withdraw_amount
            withdraw_data["description"] = description
            self.ledger.append(withdraw_data)
            return True
        else: 
            return False

    # To get balance of a particular category
    def get_balance(self):
        balance = 0
        for transactions in self.ledger:
            amount = transactions["amount"]
            balance = balance + amount
        return balance

    # To transfer to a particular category from current category
    def transfer(self, amount, category):
        balance = self.get_balance()
        description = "Transfer to " + category.name().capitalize()
        if amount <= balance:
            self.withdraw(amount, description)
            deposit_description = "Transfer from " + self.name().capitalize()
            category.deposit(amount, deposit_description)
            return True
        else:
            return False
    
    # To check if a particualar category still has funds
    def check_funds(self, amount):
        query = [trx for trx in self.ledger if trx["amount"]  == amount]
        if len(query) == 0:
            return False
        else:
            return True
    
    # To get all withdrawals made by current category
    def get_expenses(self):
        balance = self.get_balance()
        credit = 0
        for i in self.ledger:
            amount = i["amount"]
            if str(amount)[0] == "-":
                pass
            else:
                credit += amount
        expenses = credit - balance
        return expenses

# Bar chart on categories expenses
def create_spend_chart(categories):
    master = []
    total_expenses = 0
    for i in categories:
        category_expenses = int(round(i.get_expenses(), 0))
        total_expenses = total_expenses + i.get_expenses()
        sub_master = []
        sub_master.append(i.name().capitalize())
        sub_master.append(category_expenses)
        master.append(sub_master)
    for i in master:
        percentage = round((i[1]/total_expenses) * 100, 0)
        percentage_length = len(str(round(percentage)))
        zeros = "0" * (percentage_length - 1)
        percentage_initial =str(percentage)[0]
        percentage = int(percentage_initial + zeros)
        i.append(percentage)
    value = 100
    chart = ""
    for i in range(11):
        if len(str(value)) == 2:
            bar_line = " " + str(value) + "|"
        elif len(str(value)) == 1:
            bar_line = "  " + str(value) + "|" 
        else:
            bar_line = str(value) + "|"  
        max_height = 0
        description = []
        for i in master:
            if value <= i[2]:
                bar_line += " o "
            else:
                pass
            desc_category = []
            for i in i[0]:
                desc_category.append(i)
            description.append(desc_category)
        value = value - 10
        bar_line += "\n" 
        chart += bar_line
        bar_description = ""
    rearrange = []
    chart +="   ----------"
    print(chart)
    max_height = 0
    for i in description:
        if len(i) >= max_height:
            max_height = len(i)
        else:
            pass
    description_spaces = "    "
    for desc_index in range(max_height):
        index_list = []
        for i in description:
            try:
                index_list.append(i[desc_index])
            except IndexError:
                index_list.append(" ")
                pass
            else:
                pass
        rearrange.append(index_list)
    bar_chart = "Percentage spent by category"
    description_line = ""
    for i in rearrange:
        description_line += description_spaces
        for characer in i:
            description_line += " " + characer + " "
        description_line += "\n"
    print(description_line)
    bar_line += "\n" + description_line