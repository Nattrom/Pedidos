# Order Management System in Python

📌 Description

This project consists of a Python-based system designed to register customers, products, and orders, ensuring structured control over sales during a workday.

The system automates total calculation per order and generates a consolidated report upon completion.

🎯 Objective
To optimize the order registration process, avoiding manual errors and providing clear information regarding:

* Registered customers
  
* Products sold
  
* Revenue generated
  
* Final reports

🧱 Technologies Used

* Python
  
* Dictionaries
  
* Tuples
  
⚙️ System Structure

1. Customer Registration: Stores customers in a dictionary containing: ID, Name, and Email.
   
2. Product Registration: Products are stored as tuples: (product_id, name, price).
   
3. Order Creation: Links Customer, Product, and Quantity. It automatically calculates: total = price * quantity.
   
4. Order Inquiry: Displays Customer, Product, Quantity, and Total.
   
5. Revenue Calculation: Sums all orders placed.
   
6. Final Report: Includes total orders, total revenue, orders per customer, and products sold.

🚫 Constraints Met

* No lists were used.
  
* Only dictionaries and tuples were utilized.
  
* All functions receive parameters.
  
* All functions return values.
  
▶️ Execution

Run the Python file:
python sistema_pedidos.py

👥 Team Members

- Valery Rhenals Reales: Customer and product registration implementation.
  
- Natalia Romerin Rincon: Order creation and inquiry implementation.

- Jefri Calderin Ortiz: Revenue calculation and reporting module implementation.
  
📊 Expected Result

The system will display:

-Order list

-Total revenue

-Structured final report

✅ Conclusion

This system improves order organization, reduces human error, and facilitates decision-making through clear reporting.
