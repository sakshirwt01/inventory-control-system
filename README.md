# 📦 Inventory Control System (Python)

A **console-based Inventory Management System** built using **Python** and **file handling (Pickle)**.
This project simulates real-world inventory operations like product management, stock tracking, and sales processing.

## 🚀 Features

✔️ Add, update, and delete products
✔️ Manage stock with minimum stock alerts
✔️ Sell products with automatic stock deduction
✔️ Generate sales reports
✔️ Low stock alert system
✔️ Persistent data storage using binary files

## 🧠 Project Concept

This system is designed to demonstrate how **basic database-like operations** can be implemented using Python file handling.

It manages three core modules:

* **Products** → Stores product details
* **Stock** → Tracks quantity and availability
* **Sales** → Records transactions and billing

## 🛠️ Technologies Used

* Python
* File Handling (Pickle Module)
* OS Module

## 📂 Project Structure

```
inventory-control-system/
│
├── main.py              # Main application file
├── products.bin         # Product data storage
├── stock.bin            # Stock data storage
├── sales.bin            # Sales records
├── temp.bin             # Temporary file for updates
└── README.md
```

## ▶️ How to Run

1. Clone the repository:

```
git clone https://github.com/sakshirwt01/inventory-control-system.git
```

2. Navigate to project folder:

```
cd inventory-control-system
```

3. Run the program:

```
python main.py
```

---

## 📸 Sample Functionalities

* Add new product with details
* Update product price
* Add and manage stock
* Sell products with billing
* View sales reports
* Get alerts for low stock

## ⚠️ Note

* This project uses **binary files instead of a database**
* Data files (`.bin`) are auto-generated when the program runs
* Do not manually edit `.bin` files

## 💡 Future Improvements

* Convert to **SQLite / MySQL database**
* Add GUI (Tkinter / Web App)
* Add authentication system
* Improve data structure using dictionaries

## 👩‍💻 Author

**Sakshi Rawat**
Aspiring Data Analyst | Python Enthusiast

## 🌟 Show Your Support

If you like this project:
⭐ Star the repository
🔁 Share it with others
💬 Give feedback

## 📬 Connect With Me

* LinkedIn: (https://www.linkedin.com/in/sakshi-rawat91)

✨ *This project is part of my learning journey in Python and Data Analytics.*
