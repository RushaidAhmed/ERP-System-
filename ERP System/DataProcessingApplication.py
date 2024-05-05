import pandas as pd
import matplotlib.pyplot as plt
from abc import ABC, abstractmethod

# Interface
class DataProcess(ABC):
    @abstractmethod
    def process_data(self, data):
        """Process data and return analyzed results and figures."""
        pass

# Concrete class for Monthly Sales Analysis
class SalesAnalysis(DataProcess):
    def process_data(self, data):

        """Analyzes sales data and generates plots for monthly and yearly sales."""
        data['Order Date'] = pd.to_datetime(data['Order Date'])
        data['Month'] = data['Order Date'].dt.to_period('M').astype(str)
        data['Year'] = data['Order Date'].dt.year

        # Monthly analysis
        monthly_data = data.groupby('Month').agg(
            Total_Sales=('Quantity Ordered', 'sum')
        ).reset_index()

        # Yearly analysis
        yearly_data = data.groupby('Year').agg(
            Total_Sales=('Quantity Ordered', 'sum')
        ).reset_index()

        # Plotting monthly sales
        fig1, ax1 = plt.subplots(figsize=(12, 6))
        ax1.plot(monthly_data['Month'], monthly_data['Total_Sales'], marker='o')
        plt.title('Monthly Sales Analysis')
        plt.xlabel('Month')
        plt.ylabel('Total Sales')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.tight_layout()

        # Plotting yearly sales
        fig2, ax2 = plt.subplots(figsize=(10, 5))
        ax2.bar(yearly_data['Year'], yearly_data['Total_Sales'], color='skyblue')
        plt.title('Yearly Sales Analysis')
        plt.xlabel('Year')
        plt.ylabel('Total Sales')
        plt.grid(True)

        return monthly_data, yearly_data, fig1, fig2

# Similar adjustments for SupplyChainAnalysis class if needed


# Concrete class for Supply Chain Analysis
class SupplyChainAnalysis(DataProcess):
    def process_data(self, data):
        """Analyzes supply chain data for inventory management insights."""
        vendor_summary = data.groupby('VendorName').agg(Total_Spending=('Price', 'sum'),
                                                       Average_Purchase_Price=('PurchasePrice', 'mean')).reset_index()
        vendor_summary.sort_values(by='Total_Spending', ascending=False, inplace=True)
        print("Supply chain analysis complete.")
        return vendor_summary

# Additional analysis classes can be added here