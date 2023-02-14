# bank-management-system
This application handles some of the basics operations of a bank, such as customer's deposit and withdraw, money transaction history, ability to modify the account details. It is a very simplistic bank management system made with Python,PyQt5 and MYSQL.

## Installation

Download the following modules using cmd:

```bash
  pip install mysql.connector
  pip install datetime
  pip install pyqt5
```
Make the following in MYSQL:

```bash
   Database name: bank
   Table name: bank, transaction
```
Note: UserName is the Primary Key in bank Table and UserName1 is the Foreign key in transaction Table.    

bank table

![image](https://user-images.githubusercontent.com/90050088/218821639-e48c2860-05d9-4712-851f-208255d7cf9d.png)

transaction table

![image](https://user-images.githubusercontent.com/90050088/218821772-fd81acde-3449-4a23-aea0-a2adbae49526.png)
