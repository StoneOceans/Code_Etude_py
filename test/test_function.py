# test_script.py

import pytest
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from src.stanToCSV import read_and_process_file, convert_and_calculate
def expected_heure_de_reference1():
    return 902.0

def expected_heure_de_reference_1():
    return 1720.0

def expected_heure_de_reference0():
    return 0.0

def test_heure_de_reference():
    output = read_and_process_file("RDVC-20230522.pln")
    output = convert_and_calculate(output)
    
    # Assuming filter_and_analyze has been applied and output DataFrame is filtered
    heure_de_reference1 = output.loc[output['callSign_prevu'] == 'EIN545', 'heure_de_reference'].values[0]
    heure_de_reference_1 = output.loc[output['callSign_prevu'] == 'TRA79Y', 'heure_de_reference'].values[0]
    heure_de_reference0 = output.loc[output['callSign_prevu'] == '160B', 'heure_de_reference'].values[0]
    
    assert heure_de_reference1 == expected_heure_de_reference1(), "heure_de_reference for EIN545 is not equal to 902"
    assert heure_de_reference_1 == expected_heure_de_reference_1(), "heure_de_reference for TRA79Y is not equal to 1720"
    assert heure_de_reference0 == expected_heure_de_reference0(), "heure_de_reference for 160B is not equal to 0"

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

def test_calcul_HeureDeReference():
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
