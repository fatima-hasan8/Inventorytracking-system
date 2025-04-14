# Inventory Tracking System – Stage 1

## 📌 Goal
Build a CLI-based inventory system for a single kiryana store.

## ✅ Features
- Add new products
- Stock in inventory
- Record product sales
- Manually remove stock
- Store data in SQLite database (`inventory.db`)

## 🗃️ Data Model
- `Product`: name, SKU, current quantity
- `StockMovement`: product_id, type (IN, SALE, REMOVE), quantity, timestamp

## ▶️ How to Run
1. Set up environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install sqlalchemy
