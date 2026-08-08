from abc import ABC, abstractmethod

# Strategy Interface
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

# Concrete Strategies
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount:.2f} using Credit Card")

class DebitCardPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount:.2f} using Debit Card")

class UPIPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount:.2f} using UPI")

class NetBankingPayment(PaymentStrategy):
    def pay(self, amount):
        print(f"Paying ${amount:.2f} using Net Banking")

# Context
class PaymentProcessor:
    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    def process_payment(self, amount):
        if self.strategy is None:
            print("Please select a payment method.")
        else:
            self.strategy.pay(amount)
            print(f"Your payment of ${amount:.2f} has been processed successfully.")
            print("-" * 50)

# Main Program
processor = PaymentProcessor()

strategies = {
    1: CreditCardPayment(),
    2: DebitCardPayment(),
    3: UPIPayment(),
    4: NetBankingPayment()
}

while True:
    print("========== PAYMENT MENU ==========")
    print("1. Credit Card")
    print("2. Debit Card")
    print("3. UPI")
    print("4. Net Banking")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice (1-5): "))
    except ValueError:
        print("Invalid input! Please enter a number between 1 and 5.")
        continue

    if choice == 5:
        print("Thank you for using the Payment System!")
        break

    if choice not in strategies:
        print("Invalid choice! Please select a valid option.")
        continue

    try:
        amount = float(input("Enter the amount to pay: $"))
    except ValueError:
        print("Invalid amount! Please enter a valid number.")
        continue

    if amount <= 0:
        print("Amount must be greater than 0.")
        continue

    processor.set_strategy(strategies[choice])
    processor.process_payment(amount)