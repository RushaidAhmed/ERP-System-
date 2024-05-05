# tests/test_integration.py
import pytest
from DataIngection import CSVDataIngestion
from DataProcessingApplication import SalesAnalysis, SupplyChainAnalysis

def test_end_to_end():
    """ Test the end-to-end data flow from ingestion to processing """
    # Ingest data
    ingestor = CSVDataIngestion()
    data = ingestor.ingest_data('sales_data.csv')

    # Process data
    processor = SalesAnalysis()
    monthly_data, yearly_data, _, _ = processor.process_data(data)

    # Validate results
    assert not monthly_data.empty, "Monthly data should not be empty after processing"
    assert not yearly_data.empty, "Yearly data should not be empty after processing"

def test_supply_chain_integration():
    """ Test the end-to-end data flow from ingestion to processing for supply chain data """
    # Ingest data
    ingestor = CSVDataIngestion()
    data = ingestor.ingest_data('supplychain.csv')

    # Process data
    processor = SupplyChainAnalysis()
    vendor_summary = processor.process_data(data)

    # Validate results
    assert not vendor_summary.empty, "Vendor summary should not be empty after processing"
    assert 'Total_Spending' in vendor_summary.columns, "Total_Spending column should exist in the output"
    assert 'Average_Purchase_Price' in vendor_summary.columns, "Average_Purchase_Price column should exist in the output"
    # Ensure data processing correctness
    assert vendor_summary['Total_Spending'].dtype == 'float64', "Total_Spending should be a float type"
    assert vendor_summary['Average_Purchase_Price'].dtype == 'float64', "Average_Purchase_Price should be a float type"
    # Additional checks can be added here to validate specific business rules or data integrity concerns.
