import pandas as pd

def load_and_preprocess_data(file_path):
    data = pd.read_csv(file_path)

    # Drop unnecessary index column
    if 'Unnamed: 0' in data.columns:
        data = data.drop(columns=['Unnamed: 0'])

    # Normalize gallons to millions
    gallon_columns = ['gallons_from_great_lakes', 'gallons_from_groundwater',
                      'gallons_from_inland_surface', 'total_gallons_all_sources']
    data[gallon_columns] = data[gallon_columns] / 1_000_000  # convert to million gallons

    # Standardize industry names
    industry_mapping = {
        'Commercial-Institutional': 'Commercial-Institutional',
        'Industrial-Manufacturing': 'Industrial-Manufacturing',
        'Irrigation': 'Irrigation'
    }
    def standardize_industry(name):
        name_clean = str(name).strip().title()
        return industry_mapping.get(name_clean, name_clean)
    data['industry'] = data['industry'].apply(standardize_industry)

    # Ensure year column is integer
    data['year'] = data['year'].astype(str).str.strip().astype(int)

    return data
