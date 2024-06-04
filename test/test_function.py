# test_script.py

import pytest
import pandas as pd
import numpy as np
from src.stanToCSV import read_and_process_file, convert_and_calculate

# Expected values for testing
def expected_heure_de_reference1():
    return 902.0

def expected_heure_de_reference_1():
    return 1720.0

def expected_heure_de_reference0():
    return 0.0

# Function to calculate heure_de_reference
def calcul_HeureDeReference(row):
    try:
        if not pd.isna(row['dateRelative_realise']) and not pd.isnull(row['dateRelative_realise']):
            if not pd.isna(row['HeurePremiereBaliseActive_realise']) and not pd.isnull(row['HeurePremiereBaliseActive_realise']):
                if row['dateRelative_realise'] == 0:
                    return int(row['HeurePremiereBaliseActive_realise'])
                elif row['dateRelative_realise'] == 1:
                    return int(row['HeurePremiereBaliseActive_realise']) - 1440
                elif row['dateRelative_realise'] == -1:
                    return int(row['HeurePremiereBaliseActive_realise']) + 1440
            elif not pd.isna(row['HeurePremiereBaliseActive_final']) and not pd.isnull(row['HeurePremiereBaliseActive_final']):
                if row['dateRelative_realise'] == 0:
                    return int(row['HeurePremiereBaliseActive_final'])
                elif row['dateRelative_realise'] == 1:
                    return int(row['HeurePremiereBaliseActive_final']) - 1440
                elif row['dateRelative_realise'] == -1:
                    return int(row['HeurePremiereBaliseActive_final']) + 1440
            elif not pd.isna(row['HeurePremiereBalise_final']) and not pd.isnull(row['HeurePremiereBalise_final']):
                if row['dateRelative_realise'] == 0:
                    return int(row['HeurePremiereBalise_final'])
                elif row['dateRelative_realise'] == 1:
                    return int(row['HeurePremiereBalise_final']) - 1440
                elif row['dateRelative_realise'] == -1:
                    return int(row['HeurePremiereBalise_final']) + 1440
        elif not pd.isna(row['dateRelative_final']) and not pd.isnull(row['dateRelative_final']):
            if not pd.isna(row['HeurePremiereBaliseActive_realise']) and not pd.isnull(row['HeurePremiereBaliseActive_realise']):
                if row['dateRelative_final'] == 0:
                    return int(row['HeurePremiereBaliseActive_realise'])
                elif row['dateRelative_final'] == 1:
                    return int(row['HeurePremiereBaliseActive_realise']) - 1440
                elif row['dateRelative_final'] == -1:
                    return int(row['HeurePremiereBaliseActive_realise']) + 1440
            elif not pd.isna(row['HeurePremiereBaliseActive_final']) and not pd.isnull(row['HeurePremiereBaliseActive_final']):
                if row['dateRelative_final'] == 0:
                    return int(row['HeurePremiereBaliseActive_final'])
                elif row['dateRelative_final'] == 1:
                    return int(row['HeurePremiereBaliseActive_final']) - 1440
                elif row['dateRelative_final'] == -1:
                    return int(row['HeurePremiereBaliseActive_final']) + 1440
            elif not pd.isna(row['HeurePremiereBalise_final']) and not pd.isnull(row['HeurePremiereBalise_final']):
                if row['dateRelative_final'] == 0:
                    return int(row['HeurePremiereBalise_final'])
                elif row['dateRelative_final'] == 1:
                    return int(row['HeurePremiereBalise_final']) - 1440
                elif row['dateRelative_final'] == -1:
                    return int(row['HeurePremiereBalise_final']) + 1440
    except Exception as e:
        return None  # Handle any exceptions gracefully

# Mock functions for testing
def mock_read_and_process_file(file_name):
    data = {
        'callSign_prevu': ['EIN545', 'TRA79Y', '160B'],
        'dateRelative_realise': [0, 1, -1],
        'HeurePremiereBaliseActive_realise': [900, 3160, np.nan],
        'HeurePremiereBaliseActive_final': [np.nan, np.nan, 1440],
        'HeurePremiereBalise_final': [np.nan, np.nan, np.nan],
        'dateRelative_final': [np.nan, np.nan, np.nan],
    }
    return pd.DataFrame(data)

def mock_convert_and_calculate(df):
    df['heure_de_reference'] = df.apply(calcul_HeureDeReference, axis=1)
    return df

# Test cases

def test_calcul_HeureDeReference():
    data = {
        'dateRelative_realise': [0, 1, -1, 0, 1, -1],
        'HeurePremiereBaliseActive_realise': [900, 3160, 0, np.nan, np.nan, np.nan],
        'HeurePremiereBaliseActive_final': [np.nan, np.nan, np.nan, 1440, 2880, -1440],
        'HeurePremiereBalise_final': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        'dateRelative_final': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        'expected': [900, 1720, 1440, 1440, 1440, 0]
    }
    df = pd.DataFrame(data)
    df['heure_de_reference'] = df.apply(calcul_HeureDeReference, axis=1)


def test_calculHeureDeReference():
    output = read_and_process_file("RDVC-20230522.pln")
    output = convert_and_calculate(output)
    # Mock DataFrame for testing calcul_HeureDeReference function
    data = {
        'dateRelative_realise': [0, 1, -1, 0, 1, -1],
        'HeurePremiereBaliseActive_realise': [900, 3160, 0, np.nan, np.nan, np.nan],
        'HeurePremiereBaliseActive_final': [np.nan, np.nan, np.nan, 1440, 2880, -1440],
        'HeurePremiereBalise_final': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        'dateRelative_final': [np.nan, np.nan, np.nan, np.nan, np.nan, np.nan],
        'expected': [900, 1720, 1440, 1440, 1440, 0]
    }
    output['heure_de_reference'] = output.apply(calcul_HeureDeReference, axis=1)
    
    for _, row in output.iterrows():
        assert row['heure_de_reference'] == row['expected'], f"Expected {row['expected']} but got {row['heure_de_reference']}"

if __name__ == "__main__":
    pytest.main()
