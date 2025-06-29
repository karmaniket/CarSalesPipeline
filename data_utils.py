import pandas as pd

def load_and_clean_data(csv_path):
    df = pd.read_csv(csv_path, low_memory=False) 
    df.rename(columns={
        'Brand': 'brand',
        'Country': 'country',
        'Year': 'year',
        'Model': 'model',
        'Mileage': 'mileage',
        'Color': 'color'
    }, inplace=True)
    # Remove missing values
    df.dropna(subset=['year', 'country', 'brand'], inplace=True)
    # Convert year to int and strip whitespace from strings
    df['year'] = df['year'].astype(int)
    df['brand'] = df['brand'].str.strip()
    df['country'] = df['country'].str.strip()
    # Aggregate sales
    df = (
        df.groupby(['year', 'country', 'brand'], as_index=False)
          .size()
          .rename(columns={'size': 'sales'})
    )
    return df
