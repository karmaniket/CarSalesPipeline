from data_utils import load_and_clean_data
from insights import (
    get_top_per_country_year, get_global_top,
    get_total_sales, get_comparison_data, predict_sales
)
from plotting import (
    plot_global_top, plot_heatmap, plot_country_trend,
    plot_total_sales_bar, plot_comparison, plot_prediction
)
import os

# Parameters for analysis
COUNTRY = "USA"
BRAND = "Toyota"
COMPARISON_COUNTRIES = ['USA']
COMPARISON_BRANDS = ['Toyota', 'Volkswagen', 'Ford', 'Chrysler', 'Lexus', 'Chevrolet']
COMPARISON_YEARS = [2020, 2021, 2022, 2023, 2024]
PREDICT_YEAR = 2025
TOTAL_SALES_YEAR = 2024

os.makedirs("dataset", exist_ok=True)
df = load_and_clean_data("dataset/car_sales_dataset_with_person_details.csv")
if df.empty:
    print("Error: No data loaded. Please check the dataset file.")
    exit(1)

df.to_csv("dataset/cleaned_data.csv", index=False)

# heatmap of top brands per country/year
top_per_country_year = get_top_per_country_year(df)
if not top_per_country_year.empty:
    top_per_country_year.to_csv("dataset/top_brands_per_country_year.csv", index=False)
    try:
        plot_heatmap(top_per_country_year)
    except Exception as e:
        print("Heatmap plot failed:", e)

# global top brands
global_top = get_global_top(top_per_country_year)
if not global_top.empty:
    global_top.to_csv("dataset/global_top_brands.csv", index=False)
    try:
        plot_global_top(global_top)
    except Exception as e:
        print("Global top plot failed:", e)

# trend for a specific country
if COUNTRY in top_per_country_year['country'].values:
    try:
        plot_country_trend(top_per_country_year, COUNTRY)
    except Exception as e:
        print(f"Trend plot for {COUNTRY} failed:", e)

# comparison plot for selected countries, brands, and years
plot_data = get_comparison_data(df, COMPARISON_COUNTRIES, COMPARISON_BRANDS, COMPARISON_YEARS)
if plot_data:
    try:
        plot_comparison(plot_data, COMPARISON_COUNTRIES, COMPARISON_BRANDS, COMPARISON_YEARS)
    except Exception as e:
        print("Comparison plot failed:", e)

# Predict sales for a brand in a country
predicted = predict_sales(df, COUNTRY, BRAND, PREDICT_YEAR)
if predicted is not None:
    print(f"Predicted sales for {BRAND} in {COUNTRY} in {PREDICT_YEAR}: {predicted}")
    try:
        plot_prediction(df, COUNTRY, BRAND, PREDICT_YEAR, predicted)
    except Exception as e:
        print("Prediction plot failed:", e)
else:
    print(f"Not enough data to make a prediction for {BRAND} in {COUNTRY}.")

# total sales for a specific brand/country/year
total_sales = get_total_sales(df, COUNTRY, BRAND, TOTAL_SALES_YEAR)
if total_sales is not None:
    try:
        plot_total_sales_bar(BRAND, COUNTRY, TOTAL_SALES_YEAR, total_sales)
    except Exception as e:
        print("Total sales bar plot failed:", e)
    print(f"Total sales of {BRAND} in {COUNTRY} in {TOTAL_SALES_YEAR}: {total_sales}")
else:
    print(f"No sales data for {BRAND} in {COUNTRY} in {TOTAL_SALES_YEAR}.")
