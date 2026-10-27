
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


class RetailAnalyzer:

    def __init__(self):
        self.data = None

    # Load dataset
    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)

            required_columns = [
                "Date", "Product", "Category",
                "Price", "Quantity Sold", "Total Sales"
            ]

            if not all(col in self.data.columns for col in required_columns):
                print("Error: CSV columns are incorrect.")
                self.data = None
                return

            self.data["Date"] = pd.to_datetime(
                self.data["Date"], errors="coerce"
            )

            for col in ["Price", "Quantity Sold"]:
                self.data[col] = pd.to_numeric(
                    self.data[col], errors="coerce"
                )

            self.data = self.data.dropna(
                subset=["Date", "Product", "Category",
                        "Price", "Quantity Sold"]
            ).copy()

            self.data["Total Sales"] = (
                self.data["Price"] * self.data["Quantity Sold"]
            )

            print("\nDataset loaded successfully!")
            print("Total records:", len(self.data))

        except FileNotFoundError:
            print("Error: CSV file not found.")
        except Exception as e:
            print("Error:", e)

    # Calculate metrics
    def calculate_metrics(self):
        if self.data is None or self.data.empty:
            print("Please load a valid dataset first.")
            return

        sales = self.data["Total Sales"]

        popular_product = (
            self.data.groupby("Product")["Quantity Sold"]
            .sum().idxmax()
        )

        sales_array = sales.to_numpy()

        print("\n----- SALES METRICS -----")
        print(f"Total Sales: Rs. {sales.sum():.2f}")
        print(f"Average Sale: Rs. {sales.mean():.2f}")
        print("Most Popular Product:", popular_product)
        print(f"Highest Sale: Rs. {np.max(sales_array):.2f}")
        print(f"Lowest Sale: Rs. {np.min(sales_array):.2f}")

    # Filter data
    def filter_data(self):
        if self.data is None or self.data.empty:
            print("Please load a valid dataset first.")
            return

        print("\n1. Filter by Category")
        print("2. Filter by Date Range")

        choice = input("Enter choice: ")

        if choice == "1":
            print("Categories:", self.data["Category"].unique())
            category = input("Enter category: ").strip()

            result = self.data[
                self.data["Category"].str.lower() == category.lower()
            ]

        elif choice == "2":
            try:
                start = pd.to_datetime(input("Start date (YYYY-MM-DD): "))
                end = pd.to_datetime(input("End date (YYYY-MM-DD): "))

                if start > end:
                    print("Start date must be before end date.")
                    return

                result = self.data[
                    self.data["Date"].between(start, end)
                ]

            except (ValueError, TypeError):
                print("Invalid date.")
                return

        else:
            print("Invalid choice.")
            return

        if result.empty:
            print("No matching records found.")
        else:
            print(result.to_string(index=False))
            print("Filtered Total Sales:", result["Total Sales"].sum())

    # Display summary
    def display_summary(self):
        if self.data is None or self.data.empty:
            print("Please load a valid dataset first.")
            return

        print("\n----- DATA SUMMARY -----")
        print("\nFirst 5 Records:")
        print(self.data.head())

        print("\nDataset Shape:", self.data.shape)

        print("\nColumn Information:")
        self.data.info()

        print("\nMissing Values:")
        print(self.data.isnull().sum())

        print("\nDescriptive Statistics:")
        print(self.data.describe().to_string())

        print("\nSales by Category:")
        print(self.data.groupby("Category")["Total Sales"].sum())

    # Handle missing values
    def handle_missing_data(self):
        if self.data is None:
            print("Please load a dataset first.")
            return

        print("\nMissing values before cleaning:")
        print(self.data.isnull().sum())

        self.data["Product"] = self.data["Product"].fillna("Unknown")
        self.data["Category"] = self.data["Category"].fillna("Unknown")

        for col in ["Price", "Quantity Sold"]:
            self.data[col] = self.data[col].fillna(
                self.data[col].median()
            )

        self.data["Total Sales"] = (
            self.data["Price"] * self.data["Quantity Sold"]
        )

        print("\nMissing values handled.")
        print(self.data.isnull().sum())

    # Generate visualizations
    def visualize_data(self):
        if self.data is None or self.data.empty:
            print("Please load a valid dataset first.")
            return

        # Bar chart
        category_sales = self.data.groupby("Category")["Total Sales"].sum()
        category_sales.plot(kind="bar", title="Sales by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Sales")
        plt.tight_layout()
        plt.show()

        # Line graph
        daily_sales = self.data.groupby("Date")["Total Sales"].sum().sort_index()
        daily_sales.plot(kind="line", marker="o", title="Daily Sales Trend")
        plt.xlabel("Date")
        plt.ylabel("Total Sales")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()

        # Heatmap
        plt.figure(figsize=(7, 5))
        sns.heatmap(
            self.data[["Price", "Quantity Sold", "Total Sales"]].corr(),
            annot=True,
            cmap="coolwarm",
            fmt=".2f"
        )
        plt.title("Sales Correlation Heatmap")
        plt.tight_layout()
        plt.show()

    # Save visualization
    def save_visualization(self):
        if self.data is None or self.data.empty:
            print("Please load a valid dataset first.")
            return

        os.makedirs("output", exist_ok=True)

        category_sales = self.data.groupby("Category")["Total Sales"].sum()

        plt.figure(figsize=(8, 5))
        category_sales.plot(kind="bar", title="Sales by Category")
        plt.xlabel("Category")
        plt.ylabel("Total Sales")
        plt.tight_layout()

        path = os.path.abspath("output/sales_chart.png")
        plt.savefig(path)
        plt.close()

        print("Chart saved at:", path)


def main():
    analyzer = RetailAnalyzer()

    while True:
        print("\n===== RETAIL SALES DATA ANALYZER =====")
        print("1. Load Dataset")
        print("2. Calculate Sales Metrics")
        print("3. Filter Sales Data")
        print("4. Display Summary")
        print("5. Handle Missing Data")
        print("6. Generate Visualizations")
        print("7. Save Visualization")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            path = input("Enter CSV file path: ")
            analyzer.load_data(path)

        elif choice == "2":
            analyzer.calculate_metrics()

        elif choice == "3":
            analyzer.filter_data()

        elif choice == "4":
            analyzer.display_summary()

        elif choice == "5":
            analyzer.handle_missing_data()

        elif choice == "6":
            analyzer.visualize_data()

        elif choice == "7":
            analyzer.save_visualization()

        elif choice == "8":
            print("Thank you for using Retail Sales Data Analyzer!")
            break

        else:
            print("Invalid choice. Enter 1 to 8.")


if __name__ == "__main__":
    main()

