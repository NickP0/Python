# Credit Risk Model Data Preprocessing with NumPy
Please check the Jupyter Notebook (pre-processing-loan-data.ipynb) for a  walkthrough of how the preprocessing was done. The notebook provides step-by-step explanations and code examples for each preprocessing task, including data loading and manipulation, currency conversion, variable quantification, and checkpoint creation.
- loan-data.csv: Contains loan data records.
- loan-data-dictionary.xlsx: Provides a dictionary explaining the columns in the loan data.
- EUR-USD.csv: Contains currency exchange rate data.
- loan-data-preprocessed-FINAL.csv: Contains the pre-processed data in csv format. 

- USD to EUR Conversion: All USD values in the loan data are converted to EUR using the exchange rates provided in EUR-USD.csv.
- Variable Quantification: String variables are quantified by converting them into integers for numerical representation. This allows for easier analysis and modeling.
- **Checkpoint Files**
  - To ensure no data is lost during preprocessing, a few .npz files were created as checkpoints at various stages of the data processing/

