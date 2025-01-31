# 🕵️‍♂️ Web Scraping & Data Extraction using Selenium & Pandas

## 📌 Introduction
This script automates the process of extracting **seat allotment data** from the **RTE 25 Uttar Pradesh** website. The data is scraped using **Selenium**, and then the extracted table is converted into a **CSV file** using **Pandas**. The script interacts with the dropdowns, selects values, and captures the table rows for processing.

## 🛠 Installation

### Prerequisites
Ensure you have the following dependencies installed:

```
pip install selenium pandas
```
## 🎯 Functionality
- Automates website interaction using Selenium.
- Selects dropdown values dynamically for district and lottery.
- Extracts tabular data and converts it into a structured DataFrame using Pandas.
- Saves the extracted data into a CSV file called data.csv.

## ⚡ Customization
-Modify the select1.select_by_value("188") to change the district.
-Modify the select2.select_by_value("2") to change the lottery selection.
-Adjust the sleep() intervals for more optimized execution depending on your internet speed.

## 🔗 Dependencies
- 🐍 Python 3.x
- 🎮 Selenium
- 📊 Pandas

## 📜 License
This project is open-source under the MIT License. Feel free to modify and distribute it.

## File Structure
```
📂 web-scraping-project/
├── main.py              # Main script for web scraping
└── data.csv             # Output CSV file with extracted data
```
