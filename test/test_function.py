import pytest
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

if __name__ == "__main__":
    pytest.main()
