import pandas as pd
import pytest
from io import StringIO
from DataIngection import CSVDataIngestion

# Test for CSV Data Ingestion
@pytest.fixture
def csv_data():
    data = """Order Date,Quantity Ordered,Price Each
    01/02/19,2,11.95
    04/02/19,1,99.99
    """
    return StringIO(data)

def test_ingest_valid_csv(csv_data, capsys):  # Include capsys here
    ingestion = CSVDataIngestion()
    result = ingestion.ingest_data(csv_data)
    assert not result.empty, "The DataFrame should not be empty"
    assert result.iloc[0]['Quantity Ordered'] == 2, "Quantity should match the input data"
    assert 'Data ingestion successful.' in capsys.readouterr().out, "Success message should be printed"


def ingest_data(self, file_path):
    try:
        data = pd.read_csv(file_path)
        print("Data ingestion successful.")
        return data
    except FileNotFoundError:
        raise ValueError("File not found")
    except pd.errors.ParserError:
        raise ValueError("Error parsing file")

