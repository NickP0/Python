# Credit Risk Model Data Preprocessing with NumPy
- loan-data.csv: Contains loan data records.
- loan-data-dictionary.xlsx: Provides a dictionary explaining the columns in the loan data.
- EUR-USD.csv: Contains currency exchange rate data.


- USD to EUR Conversion: All USD values in the loan data are converted to EUR using the exchange rates provided in EUR-USD.csv.
- Variable Quantification: String variables are quantified by converting them into integers for numerical representation. This allows for easier analysis and modeling.
- **Checkpoint Files**
  - To ensure no data is lost during preprocessing, a few .npz files are created as checkpoints at various stages of data processing:

