import pandas as pd
import streamlit as st

# Define a Streamlit app
def main():
    st.title("Valid8ME Data Merge")

    # File upload widgets
    st.write("Upload Master Data (file1):")
    file1 = st.file_uploader("Upload Master Data", type=['xlsx'])

    st.write("Upload Valid8Me Output (file2):")
    file2 = st.file_uploader("Upload Valid8Me Output", type=['xlsx'])

    # Load data button
    if st.button("Clean Data Process"):
        if file1 is not None and file2 is not None:
            # Read the Excel files into Pandas DataFrames
            df1 = pd.read_excel(file1)
            df2 = pd.read_excel(file2)

            try:
                # Merge the DataFrames based on different columns using outer join
                merged_df = pd.merge(df1, df2, on=['Form_instance_ID', 'Page name'], how='outer')

                # Fill missing values in df1 with values from df2
                merged_df = df2.combine_first(df1)

                # Save the merged DataFrame to a new Excel file
                merged_file_path = "merged_file.xlsx"
                merged_df.to_excel(merged_file_path, index=False)

                # Provide a link to download the CSV file
                csv_data = merged_df.to_csv(index=False).encode('utf-8')
                st.download_button(label="Download CSV", data=csv_data, file_name="Valid8MeAggregate.csv", mime="text/csv")

                st.success("Merged Excel file saved successfully.")
            except Exception as e:
                st.warning("Merge failed. Please ensure that both files have the necessary columns for merging.")
        else:
            st.warning("Please upload both Master Data and Valid8Me Output files.")

if __name__ == "__main__":
    main()
