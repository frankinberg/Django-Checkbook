from django.db import models


class Account(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    initial_deposit = models.DecimalField(max_digits=15, decimal_places=2)

    Accounts = models.Manager()

    # Allows references to a specific account be returned
    # as the owner's name not the primary key
    def __str__(self):
        return str(self.first_name) + ' ' + str(self.last_name)


TransactionTypes = [('Deposit', 'Deposit'), ('Withdraw', 'Withdraw')]


class Transaction(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=10, choices=TransactionTypes)
    amount = models.DecimalField(max_digits=15, decimal_places=2)
    description = models.CharField(max_length=100)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    Transactions = models.Manager()
