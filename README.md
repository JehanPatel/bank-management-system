
![Downloads](https://img.shields.io/github/downloads/JehanPatel/bank-management-system/total) ![Contributors](https://img.shields.io/github/contributors/JehanPatel/bank-management-system?color=dark-green) ![Forks](https://img.shields.io/github/forks/JehanPatel/bank-management-system?style=social) ![Stargazers](https://img.shields.io/github/stars/JehanPatel/bank-management-system?style=social) ![Issues](https://img.shields.io/github/issues/JehanPatel/bank-management-system) 

## Table Of Contents

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [Roadmap](#roadmap)
* [Contributing](#contributing)
* [Authors](#authors)

## About The Project

This application handles some of the basics operations of a bank, such as customer's deposit and withdraw, money transaction history, ability to modify the account details. It is a very simplistic bank management system made with Python,PyQt5 and MYSQL.


## Getting Started

To get started, install the following modules onto your computer 

### Prerequisites

- `pip install mysql.connector`
- `pip install datetime`
- `pip install pyqt5`

Make the following in MYSQL:

```bash
   Database name: bank
   Table name: bank, transaction
```
Note: UserName is the Primary Key in bank Table and UserName1 is the Foreign key in transaction Table.    

## bank table

![image](https://user-images.githubusercontent.com/90050088/218821639-e48c2860-05d9-4712-851f-208255d7cf9d.png)

## transaction table

![image](https://user-images.githubusercontent.com/90050088/218821772-fd81acde-3449-4a23-aea0-a2adbae49526.png)

### Installation

- Download the folder.
- Open cmd and run all installation's using `pip` command.
- Update username and password to your MYSQL server in bank.py
- Open cmd from the bank.py file location.
- Type `python bank.py` to run the file

## Roadmap

See the [open issues](https://github.com/JehanPatel/bank-management-system/issues) for a list of proposed features (and known issues).

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.
* If you have suggestions for adding or removing projects, feel free to [open an issue](https://github.com/JehanPatel/bank-management-system/issues/new) to discuss it, or directly create a pull request after you edit the *README.md* file with necessary changes.
* Please make sure you check your spelling and grammar.
* Create individual PR for each suggestion.
* Please also read through the [Code Of Conduct](https://github.com/JehanPatel/bank-management-system/blob/main/CODE_OF_CONDUCT.md) before posting your first idea as well.

## Authors

* **Jehan Patel** - *CSE Core student* - [Jehan Patel](https://github.com/JehanPatel) 
* **Neel Jain** - *CSE Core student* - [Neel Jain](https://github.com/Neel-2002) 
* **Abhinav** - *CSE Core student* - [Abhinav](https://github.com/Abhinav4291) 
* **Juss Patel** - *Student* - [Juss Patel](https://github.com/jusspatel) 

