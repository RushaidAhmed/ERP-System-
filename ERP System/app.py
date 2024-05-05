import streamlit as st
import pandas as pd
from DataProcessingApplication import SalesAnalysis, SupplyChainAnalysis
from DataIngection import CSVDataIngestion, DataIngestionStrategy

# Initialize the Streamlit app
def main():
    st.title('Data Analysis Application')

    # File upload section
    st.header('Upload your data file')
    file_type = st.radio("Choose the type of data to analyze:", ('Sales', 'Supply Chain'))
    data_file = st.file_uploader("Upload a CSV file", type=['csv'])

    # Processing strategy selection and output
    if data_file is not None:
        ingection = CSVDataIngestion()
        data = ingection.ingest_data(data_file)


        # Display the complete dataset in the application
        st.write("### Full Dataset")
        st.dataframe(data)  # Displaying the full data table

        if file_type == 'Sales':
            processor = SalesAnalysis()
            monthly_data, yearly_data, fig1, fig2 = processor.process_data(data)

            # Display processed data
            st.write("### Monthly Sales Data")
            st.dataframe(monthly_data)
            st.write("### Yearly Sales Data")
            st.dataframe(yearly_data)

            # Display plots
            st.write("### Monthly Sales Plot")
            st.pyplot(fig1)
            st.write("### Yearly Sales Plot")
            st.pyplot(fig2)

        elif file_type == 'Supply Chain':
            processor = SupplyChainAnalysis()
            vendor_summary = processor.process_data(data)

            # Filtering options
            min_spending = st.sidebar.slider("Minimum Total Spending", float(vendor_summary['Total_Spending'].min()), float(vendor_summary['Total_Spending'].max()), float(vendor_summary['Total_Spending'].min()))
            vendor_summary = vendor_summary[vendor_summary['Total_Spending'] >= min_spending]

            # Sorting options
            sort_by = st.sidebar.radio("Sort by", ('Total_Spending', 'Average_Purchase_Price'))
            sort_order = st.sidebar.radio("Sort order", ('Ascending', 'Descending'))
            if sort_order == 'Ascending':
                vendor_summary = vendor_summary.sort_values(by=sort_by, ascending=True)
            else:
                vendor_summary = vendor_summary.sort_values(by=sort_by, ascending=False)

            # Display results
            st.write("### Supply Chain Analysis")
            st.dataframe(vendor_summary)

    st.sidebar.title("About")
    st.sidebar.info(
        "This application is built using Streamlit and demonstrates the use of the Strategy Pattern for data ingestion and processing.")

if __name__ == "__main__":
    main()