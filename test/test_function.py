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

def test_calcul_HeureDeReference():
    test_data = [
        {'dateRelative_realise': 0, 'HeurePremiereBaliseActive_realise': 900, 'HeurePremiereBaliseActive_final': np.nan, 'HeurePremiereBalise_final': np.nan, 'expected': 900},
        {'dateRelative_realise': 1, 'HeurePremiereBaliseActive_realise': 900, 'HeurePremiereBaliseActive_final': np.nan, 'HeurePremiereBalise_final': np.nan, 'expected': 900 - 1440},
        {'dateRelative_realise': -1, 'HeurePremiereBaliseActive_realise': 900, 'HeurePremiereBaliseActive_final': np.nan, 'HeurePremiereBalise_final': np.nan, 'expected': 900 + 1440},
        {'dateRelative_realise': np.nan, 'HeurePremiereBaliseActive_realise': np.nan, 'HeurePremiereBaliseActive_final': 1000, 'HeurePremiereBalise_final': np.nan, 'dateRelative_final': 0, 'expected': 1000},
        {'dateRelative_realise': np.nan, 'HeurePremiereBaliseActive_realise': np.nan, 'HeurePremiereBaliseActive_final': 1000, 'HeurePremiereBalise_final': np.nan, 'dateRelative_final': 1, 'expected': 1000 - 1440},
        {'dateRelative_realise': np.nan, 'HeurePremiereBaliseActive_realise': np.nan, 'HeurePremiereBaliseActive_final': 1000, 'HeurePremiereBalise_final': np.nan, 'dateRelative_final': -1, 'expected': 1000 + 1440}
    ]

    df = pd.DataFrame(test_data)
    df['heure_de_reference'] = df.apply(calcul_HeureDeReference, axis=1)

    for _, row in df.iterrows():
        assert row['heure_de_reference'] == row['expected'], f"Expected {row['expected']} but got {row['heure_de_reference']}"

def test_calcul_DateDeReference():
    date_obj = datetime(2023, 5, 22)
    test_data = [
        {'dateRelative_realise': 0, 'dateRelative_final': np.nan, 'expected': date_obj},
        {'dateRelative_realise': 1, 'dateRelative_final': np.nan, 'expected': date_obj - timedelta(days=1)},
        {'dateRelative_realise': -1, 'dateRelative_final': np.nan, 'expected': date_obj + timedelta(days=1)},
        {'dateRelative_realise': np.nan, 'dateRelative_final': 0, 'expected': date_obj},
        {'dateRelative_realise': np.nan, 'dateRelative_final': 1, 'expected': date_obj - timedelta(days=1)},
        {'dateRelative_realise': np.nan, 'dateRelative_final': -1, 'expected': date_obj + timedelta(days=1)}
    ]

    df = pd.DataFrame(test_data)
    df['date_de_reference'] = df.apply(lambda row: calcul_DateDeReference(row, date_obj), axis=1)

    for _, row in df.iterrows():
        assert row['date_de_reference'] == row['expected'], f"Expected {row['expected']} but got {row['date_de_reference']}"

if __name__ == "__main__":
    pytest.main()
