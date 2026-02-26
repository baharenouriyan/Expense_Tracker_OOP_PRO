class Transaction:
    def init(self, amount, type_, description):
        self.amount = amount
        self.type = type_  # "Income" یا "Expense"
        self.description = description

    def str(self):
   
     return f"{self.type}: {self.description} - {self.amount}"
