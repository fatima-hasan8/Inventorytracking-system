# inventory.py
from models import Session, Product, StockMovement

def add_product(name, sku):
    session = Session()
    if session.query(Product).filter_by(sku=sku).first():
        print("SKU already exists.")
        return
    product = Product(name=name, sku=sku)
    session.add(product)
    session.commit()
    print("✅ Product added.")

def stock_in(sku, qty):
    session = Session()
    product = session.query(Product).filter_by(sku=sku).first()
    if product:
        product.current_quantity += qty
        movement = StockMovement(product_id=product.id, type='IN', quantity=qty)
        session.add(movement)
        session.commit()
        print("✅ Stock updated.")
    else:
        print("❌ Product not found.")

def sell_product(sku, qty):
    session = Session()
    product = session.query(Product).filter_by(sku=sku).first()
    if product and product.current_quantity >= qty:
        product.current_quantity -= qty
        movement = StockMovement(product_id=product.id, type='SALE', quantity=qty)
        session.add(movement)
        session.commit()
        print("✅ Sale recorded.")
    else:
        print("❌ Not enough stock or product not found.")

def remove_stock(sku, qty):
    session = Session()
    product = session.query(Product).filter_by(sku=sku).first()
    if product and product.current_quantity >= qty:
        product.current_quantity -= qty
        movement = StockMovement(product_id=product.id, type='REMOVE', quantity=qty)
        session.add(movement)
        session.commit()
        print("✅ Stock manually removed.")
    else:
        print("❌ Not enough stock or product not found.")

# CLI
if __name__ == "__main__":
    print("📦 Inventory Tracking CLI")
    while True:
        print("\nCommands: add | in | sell | remove | exit")
        cmd = input("Enter command: ").strip().lower()
        if cmd == "add":
            name = input("Product name: ")
            sku = input("SKU: ")
            add_product(name, sku)
        elif cmd == "in":
            sku = input("SKU: ")
            qty = int(input("Quantity to stock in: "))
            stock_in(sku, qty)
        elif cmd == "sell":
            sku = input("SKU: ")
            qty = int(input("Quantity to sell: "))
            sell_product(sku, qty)
        elif cmd == "remove":
            sku = input("SKU: ")
            qty = int(input("Quantity to remove: "))
            remove_stock(sku, qty)
        elif cmd == "exit":
            break
        else:
            print("❓ Invalid command.")
