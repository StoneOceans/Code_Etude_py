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

if __name__ == "__main__":
    pytest.main()
