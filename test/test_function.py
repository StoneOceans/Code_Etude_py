# test_script.py
import pandas as pd
import numpy as np
import pytest
from src.stanToCSV import read_and_process_file, convert_and_calculate

def test_heure_de_reference():
    output = read_and_process_file("RDVC-20230522.pln")
    output = convert_and_calculate(output)
    # Assuming filter_and_analyze has been applied and output DataFrame is filtered
    heure_de_reference1 = output.loc[output['callSign_prevu'] == 'EIN545', 'heure_de_reference'].values[0]
    heure_de_reference_1=output.loc[output['callSign_prevu'] == 'TRA79Y', 'heure_de_reference'].values[0]
    heure_de_reference0=output.loc[output['callSign_prevu'] == '160B', 'heure_de_reference'].values[0]
    assert heure_de_reference1 == 902.0, "heure_de_reference for EIN545 is not equal to 902"
    assert heure_de_reference_1 == 1720.0, "heure_de_reference for EIN545 is not equal to 902"
    assert heure_de_reference0 == 0.0, "heure_de_reference for EIN545 is not equal to 902"


def test_calcul_HeureDeReference():
    output = read_and_process_file("RDVC-20230522.pln")

    df = pd.DataFrame(output)
    df['heure_de_reference'] = df.apply(calcul_HeureDeReference, axis=1)
    
    for _, row in df.iterrows():
        assert row['heure_de_reference'] == row['expected'], f"Expected {row['expected']} but got {row['heure_de_reference']}"

if __name__ == "__main__":
    pytest.main()
