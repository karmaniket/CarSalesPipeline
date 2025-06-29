# Car Sales Data Analysis

Analyze and visualize trends in a large synthetic car sales dataset. This project provides a modular pipeline for data cleaning, insight extraction, and visualization, enabling you to explore car sales patterns, compare brands, and predict future sales.

---

## Visualization

<table><tr><td>
      <h3 align="center">Global Top Brand</h3>
      <img width="auto" src="output\global_top_brand.png">
    </td><td>
      <h3 align="center">Top Selling Brand</h3>
      <img width="auto" src="output\top_selling_brand_usa.png">  </td>
  </tr>
    <tr><td>
      <h3 align="center">Sales Comparison</h3>
      <img width="auto" src="output\sales_comparison.png">
    </td><td>
      <h3 align="center">Future Prediction</h3>
      <img width="auto" src="output\usa_toyota_2025_prediction.png">
    </td></tr>
</table>

---

## Features

- **Data Cleaning:** Standardizes and aggregates raw sales data for analysis.
- **Insight Extraction:** Find top brands by country/year, global leaders, and sales totals.
- **Visualization:** Generate heatmaps, bar charts, line plots, and prediction plots.
- **Sales Prediction:** Predict future sales for a brand in a country using linear regression.
- **Customizable:** Easily change countries, brands, and years for your analysis.

---

## Directory Structure

```
.
├── dataset.py         # Script to download the dataset from KaggleHub
    └── car_sales_dataset_with_person_details.csv  # (Downloaded dataset)
├── data_utils.py      # Data loading and cleaning functions
├── insights.py        # Data querying and insight functions 
├── plotting.py        # All plotting functions (plots saved to output/)
├── main.py            # Main script
├── dataset/           # Folder for all CSV files
├── output/            # Folder for generated plots
```

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/karmaniket/CarSalesPipeline.git
cd CarSalesPipeline
```

### 2. Install Requirements

Install all dependencies with:

```bash
pip install pandas matplotlib seaborn kagglehub scikit-learn
```

### 3. Download the Dataset

Run the following to download the dataset from KaggleHub:

```bash
python dataset.py
```

This will download the dataset and print the file path. The CSV will be placed in the `dataset/` folder.

---

## How to Use

### 1. Configure Your Analysis

Open `main.py` and edit the parameters at the top to select the country, brand, years, and brands you want to analyze:

```python
COUNTRY = "USA"
BRAND = "Toyota"
COMPARISON_COUNTRIES = ['USA']
COMPARISON_BRANDS = ['Toyota', 'Volkswagen', 'Ford', 'Chrysler', 'Lexus', 'Chevrolet']
COMPARISON_YEARS = [2020, 2021, 2022, 2023, 2024]
PREDICT_YEAR = 2025
TOTAL_SALES_YEAR = 2024
```

### 2. Select the Insights/Plots to Run

In `main.py`, comment or uncomment the function calls to run only the analyses or plots you want.  
Each block is independent and can be enabled/disabled as needed.

### 3. Run the Main Script

```bash
python main.py
```

This will generate the selected plots (saved in `output/`) and print insights to the console.

---

## Example Analyses

- Compare sales for selected countries, brands, and years.
- Show total sales for a specific brand/country/year.
- Visualize the global top brand by number of countries each year.
- Heatmap of top brands by country and year.
- Trend of top-selling brands in a specific country.
- Predict future sales for a brand in a country for a specific year (using linear regression).

---

## Customization

- To analyze different countries, brands, or years, change the lists in `main.py`.
- To generate a different plot, comment/uncomment the relevant function calls in `main.py`.
- All plots are saved in the `output/` directory for easy access.

---

## File Descriptions

- `dataset.py` : Downloads the dataset from KaggleHub.
- `data_utils.py` : Loads and cleans the raw dataset, standardizing columns and aggregating sales.
- `insights.py` : Provides functions to extract insights (top brands, global leaders, sales totals, predictions).
- `plotting.py` : Contains all plotting functions (heatmaps, bar charts, line plots, prediction plots).
- `main.py` : The main entry point. Edit this file to select and run your desired analyses.
- `dataset/` : Stores the raw and cleaned CSV files.
- `output/` : Stores all generated plots.

---

## Requirements

- Python 3.7+
- pandas
- matplotlib
- seaborn
- kagglehub
- scikit-learn

---

> [!Note]
> All plots are saved in the `output/` directory.
> The code is modular: data loading, insights, and plotting are separated for clarity and maintainability.
> The dataset is synthetic and intended for demonstration and educational purposes.

---

## License

This project is for educational and demonstration purposes only.