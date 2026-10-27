# Retail Sales Data Analyzer

## Project Overview
The Retail Sales Data Analyzer is a Python-based project that analyzes retail sales data using Pandas, NumPy, Matplotlib, and Seaborn. It calculates sales metrics, filters records, handles missing values, displays summary statistics, and generates visualizations.

## Objectives
- Analyze retail sales data.
- Calculate total and average sales.
- Identify the most popular product.
- Filter sales by category and date range.
- Display dataset information and descriptive statistics.
- Handle missing values.
- Generate and save sales graphs.

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn

## Project Structure

```text
Retail_Sales_Analyzer/
│
├── retail_analyzer.py
├── retail_sales.csv
├── README.md
│
└── output/
    └── sales_chart.png
```

## Features

1. **Load Dataset:** Reads retail sales data from a CSV file.
2. **Calculate Sales Metrics:** Calculates total sales, average sale, highest sale, lowest sale, and most popular product.
3. **Filter Sales Data:** Filters records by product category or date range.
4. **Display Summary:** Displays the first five records, dataset shape, column information, missing values, descriptive statistics, and category-wise sales.
5. **Handle Missing Data:** Checks and handles missing values.
6. **Generate Visualizations:** Creates bar charts, line graphs, and a correlation heatmap.
7. **Save Visualization:** Saves a sales chart as a PNG image.
8. **Exit:** Closes the program.

## Dataset Information

The dataset contains the following columns:

- `Date`: Date of the sale.
- `Product`: Name of the product.
- `Category`: Product category.
- `Price`: Price per unit.
- `Quantity Sold`: Number of units sold.
- `Total Sales`: Total sales amount.

## Installation

Install the required libraries using:

```bash
pip install pandas numpy matplotlib seaborn
```

## How to Run

Open the project folder in VS Code and run the following command in the terminal:

```bash
python retail_analyzer.py
```

If Python is not recognized on Windows, use the installed Anaconda Python executable:

```powershell
C:\Users\abc\anaconda3\python.exe retail_analyzer.py
```

Follow the menu displayed in the terminal and enter the required option.

When loading the dataset, provide the path to `retail_sales.csv`.

## Sales Calculation

The program calculates total sales using the formula:

**Total Sales = Price × Quantity Sold**

For example, if the price is ₹500 and 10 units are sold:

Total Sales = 500 × 10 = ₹5,000

## Expected Results

For the provided sample dataset:

- Total Sales: ₹551,400
- Average Sale: ₹36,760
- Most Popular Product by Quantity Sold: Mouse
- Highest Individual Sale: ₹150,000
- Lowest Individual Sale: ₹4,000

## Conclusion

The Retail Sales Data Analyzer demonstrates how Python libraries can be used for data cleaning, data analysis, statistical summaries, filtering, and visualization. It provides a simple menu-driven interface for understanding retail sales performance.

This project is developed for learning and practicing Python data analysis concepts.
