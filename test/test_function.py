# test_script.py

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


if __name__ == "__main__":
    pytest.main()
