from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def save_receipt_as_pdf(self, filename: str):
    pdf = canvas.Canvas(filename, pagesize=letter)
    text = pdf.beginText(40, 750)
    text.setFont("Helvetica", 12)

    receipt_lines = self.generate_receipt().split("\n")
    for line in receipt_lines:
        text.textLine(line)

    pdf.drawText(text)
    pdf.save()
    print(f"Receipt saved as {filename}")


class Item:
    def __init__(self, name: str, price: float, quantity: int):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_price(self) -> float:
        return self.price * self.quantity

import datetime

class Receipt:
    TAX_RATE = 0.10  # 10% tax
    DISCOUNT_RATE = 0.05  # 5% discount

    def __init__(self):
        self.items = []

    def add_item(self, item: Item):
        self.items.append(item)

    def calculate_subtotal(self) -> float:
        return sum(item.total_price() for item in self.items)

    def calculate_tax(self) -> float:
        return self.calculate_subtotal() * self.TAX_RATE

    def calculate_discount(self) -> float:
        return self.calculate_subtotal() * self.DISCOUNT_RATE

    def calculate_total(self) -> float:
        subtotal = self.calculate_subtotal()
        tax = self.calculate_tax()
        discount = self.calculate_discount()
        return subtotal + tax - discount

    def generate_receipt(self) -> str:
        receipt_lines = [f"Receipt - {datetime.datetime.now()}"]
        receipt_lines.append("-" * 30)
        for item in self.items:
            receipt_lines.append(f"{item.name} - {item.quantity} @ {item.price:.2f} each - Total: {item.total_price():.2f}")
        receipt_lines.append("-" * 30)
        receipt_lines.append(f"Subtotal: {self.calculate_subtotal():.2f}")
        receipt_lines.append(f"Tax (10%): {self.calculate_tax():.2f}")
        receipt_lines.append(f"Discount (5%): -{self.calculate_discount():.2f}")
        receipt_lines.append(f"Total: {self.calculate_total():.2f}")
        return "\n".join(receipt_lines)

    


    def save_as_pdf(self, filename: str):
        save_receipt_as_pdf(self, filename)

def main():
    receipt = Receipt()

    while True:
        name = input("Enter item name (or 'done' to finish): ")
        if name.lower() == 'done':
            break

        price = float(input("Enter item price: "))
        quantity = int(input("Enter item quantity: "))

        item = Item(name, price, quantity)
        receipt.add_item(item)

    # Display receipt
    print(receipt.generate_receipt())

    # Save to file
    print(receipt.save_as_pdf('receipt.pdf'))

if __name__ == "__main__":
    main()


