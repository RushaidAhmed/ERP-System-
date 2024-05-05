import pandas as pd
import pytest
from DataProcessingApplication import SalesAnalysis, SupplyChainAnalysis

@pytest.fixture
def sales_data():
    data = pd.DataFrame({
        'Order Date': pd.to_datetime(['01-01-2020', '02-01-2020']),
        'Quantity Ordered': [2, 3],
        'Price Each': [10.0, 15.0]
    })
    return data

def test_sales_data_processing(sales_data):
    processor = SalesAnalysis()
    monthly_data, yearly_data, fig1, fig2 = processor.process_data(sales_data)
    assert not monthly_data.empty, "Monthly data should not be empty"
    assert not yearly_data.empty, "Yearly data should not be empty"
    assert monthly_data['Total_Sales'].sum() == 5, "Total sales should be the sum of quantities"

@pytest.fixture
def supply_data():
    data = pd.DataFrame({
        'VendorName': ['Vendor A', 'Vendor B'],
        'Price': [120.0, 150.0],
        'PurchasePrice': [100.0, 110.0]
    })
    return data

def test_supply_chain_processing(supply_data):
    processor = SupplyChainAnalysis()
    result = processor.process_data(supply_data)
    assert not result.empty, "Resulting DataFrame should not be empty"

    # Ensure the DataFrame is sorted as expected by the application logic
    expected_top_vendor = 'Vendor B'
    actual_top_vendor = result.iloc[0]['VendorName']
    assert actual_top_vendor == expected_top_vendor, f"Top vendor should be {expected_top_vendor}"

    expected_top_spending = 150.0  # This should match the top vendor's total spending
    actual_top_spending = result.iloc[0]['Total_Spending']
    assert actual_top_spending == expected_top_spending, f"Total spending for {expected_top_vendor} should be {expected_top_spending}"
