import pytest
from test.mains import parse_pln_file
import pandas as pd

def test_parse_pln_file():
    # Prepare a sample file content
    sample_content = """\
02 22-05-2023
05
11
20 AA1234 DEP ARR 1234 A320 WORK ??WORK
21 1200 350 500 EOBT
22 REG1 TYPE1 ?? 1 0 ?? 22052023
23 0001 12345678 ADRSMODE
24 PLN123 FlightID
31 BALISE
32 1200
33 BALISTES
36 INDICATEUR
41 CARTE
71 CENTRE
72 RANG
80 TRANSACTION
81 PART-INFO
82 1200 CCR: ARR
84 FINAL
"""
    # Write the sample content to a temporary file
    with open('sample_test_file.pln', 'w') as file:
        file.write(sample_content)

    # Call the function with the temporary file
    output_df = parse_pln_file('sample_test_file.pln')

    # Check the expected values in the dataframe
    expected_data = {
        'callsignprevu': ['AA1234'],
        'depprevu': ['DEP'],
        'arrprevu': ['ARR'],
        'numcautraprevu': ['1234'],
        'typeavionprevu': ['A320'],
        'workprevu': ['WORK'],
        'work1prevu': [''],
        'heuresdedepprevu': ['1200'],
        'RFLprevu': ['350'],
        'vitesseprevu': ['500'],
        'EOBTprevu': ['EOBT'],
        'regledevolprevu': ['REG1'],
        'typedevolprevu': ['TYPE1'],
        'IFPLprevu': [''],
        'PLN_activeprevu': ['1'],
        'PLN_annuleprevu': ['0'],
        'date_blockprevu': ['22052023'],
        'adressemodeprevu': ['ADRSMODE'],
        'numeroPLNMprevu': ['PLN123'],
        'FlightIDprevu': ['FlightID'],
        'baliseprevu': ['BALISE'],
        'listhourprevu': ['1200'],
        'listedesbalistesprevu': ['BALISTES'],
        'indicateurprevu': ['INDICATEUR'],
        'carteprevu': ['CARTE'],
        'centretraverséprevu': ['CENTRE'],
        'listederangpremierprevu': ['RANG'],
        'rangtransactionprevu': ['TRANSACTION'],
        'heure': ['12'],
        'minute': ['00'],
        'accusetrtprevu': ['1200'],
        'ccr_arrival': ['ARR'],
        'finalprevu': ['FINAL']
    }

    expected_df = pd.DataFrame(expected_data)

    # Compare the resulting dataframe with the expected dataframe
    pd.testing.assert_frame_equal(output_df, expected_df)

if __name__ == "__main__":
    pytest.main()
