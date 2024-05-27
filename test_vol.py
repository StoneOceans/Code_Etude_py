# test_vol.py

import pytest
from src.mains import parse_pln_file
import pandas as pd


def test_parse_pln_file():
    """Tests the parse_pln_file function with sample data."""

    # Prepare a sample file content
    sample_content = """
    05
    11
    20 ETH575 KORD HAAB 9273 -1 B788 0000 ETAOU 0
    21 -525 350 485 -525
    22 I S AA47735238 0 0 FPL 21052023 SANDY 0 0 21-05-2023 00:00
    23 0 0 0 ??????
    24  -1 ???????? 0
    2R LASAT390
    31 SANDY MOTOX RUCAC LESDO RANUX ETINO NEBAX LASAT DEVDI 
    32 -105 -162 -161 -149 -142 -138 -131 -128 -64 
    33 370 370 370 370 370 370 370 370 370 
    36 0 0 0 0 0 0 0 0 0 
    41 HN YR HE GL 5M 
    71 EGGG REIM ZURI 
    72 1 2 5 
    13
    20 ETH575 KORD HAAB 9273 -1 B788 1152 ETAOU 0
    21 -525 350 485 -525
    22 I S AA47735238 0 0 FPL 21052023 SANDY 0 0 21-05-2023 00:00
    23 0 0 0 ??????
    24  -1 ???????? 0
    2R LASAT390
    31 SANDY MOTOX RUCAC LESDO RANUX ETINO NEBAX LASAT DEVDI 
    32 -113 -113 -112 -100 -93 -89 -82 -79 -72 
    33 370 390 390 390 390 390 390 390 370 
    36 0 0 0 0 0 0 0 0 0 
    41 HN GL HR HE 5M 
    71 EGGG REIM ZURI 
    72 1 2 5 
    12
    20 ETH575 KORD HAAB  -1 -1 B788 0000 ETAOU 0
    21 -525 390 485 -525
    22 I S AA47735238 1 0 FPL 21052023 MOTOX 1 1328 21-05-2023 00:00
    23 0 0 0 ??????
    24  -1 ???????? 0
    2R ??
    31 MOTOX PTGEO PTGEO PTGEO PTGEO PTGEO PTGEO PTGEO 
    32 -112 -112 -112 -101 -90 -83 -78 
    33 390 390 390 390 390 390 390 
    36 0 0 0 0 0 0 0 0 0 
    41 HN HR KF HE HH 
    71 REIM 
    72 1 
    14
    80 1
    81 O8271PE99 211810         O8271     211810 EUCHZMFP (ACH-ETH575-KORD1515-HAAB -8/IS-9/B788/H-10/SADE1E3FGHIJ2J3J4J5J7LM1M2OP1P2P3RVWXYZ/LB1D1-14/SOVED/2053F370 -15/N0485F350 ELX DCT MBS DCT 47N080W 5130N07000W DCT JANJO/M084F370 56N050W 57N040W 57N030W 56N020W PIKIL DCT SOVED/M084F370 DCT NIBOG DCT SOSIM L15 MOTOX UL15 NEBAX DCT LASAT/N0475F390 DCT DEVDI DCT ODINA DCT LEVDI DCT NIMAN DCT ARLOS UN4 SALUN N705 MMA/N0482F410 N705 BOPIX N710 TAKRI P751 LXR M999 JDW G650 RASKA/N0487F400 UG650 KONET/
    82 18:10 TRANSACTION NO 2   CCR: EGGG REIM ZURI
    83 ETH575 LETAOUI 1B788479 370             212152F    S KORDHAABYW
    84 ETH575 LETAOUI 1B788480 370     370     212207SANDYS KORDHAABYW
    """
    
    # Write the sample content to a temporary file
    with open('sample_test_file.pln', 'w') as file:
        file.write(sample_content)

    # Call the function with the temporary file
    output_df = parse_pln_file('sample_test_file.pln')

    # Create the expected dataframe manually (you might need to adjust this based on your actual expected output)
    expected_data = {
        'callsignprevu': ['ETH575'],
        'depprevu': ['KORD'],
        'arrprevu': ['HAAB'],
        'numcautraprevu': ['9273'],
        'typeavionprevu': ['B788'],
        'workprevu': ['ETAOU'],
        'heuresdedepprevu': ['-525'],
        'RFLprevu': ['350'],
        'vitesseprevu': ['485'],
        'EOBTprevu': ['-525'],
        'regledevolprevu': ['I'],
        'typedevolprevu': ['S'],
        'IFPLprevu': ['AA47735238'],
        'PLN_activeprevu': ['0'],
        'PLN_annuleprevu': ['0'],
        'date_blockprevu': ['21052023'],
        'adressemodeprevu': [pd.NA],
        'numeroPLNMprevu': [pd.NA],
        'FlightIDprevu': [pd.NA],
        'baliseprevu': ['SANDY'],
        'listhourprevu': ['-105'],
        'listedesbalistesprevu': ['370'],
        'indicateurprevu': ['0'],
        'carteprevu': ['HN'],
        'centretraverséprevu': ['EGGG'],
        'listederangpremierprevu': ['1'],
        'rangtransactionprevu': [pd.NA],
        'heure': [pd.NA],
        'minute': [pd.NA],
        'accusetrtprevu': [pd.NA],
        'ccr_arrival': [pd.NA],
        'finalprevu': [pd.NA]
    }

    expected_df = pd.DataFrame(expected_data)

    # Compare the resulting dataframe with the expected dataframe
    pd.testing.assert_frame_equal(output_df, expected_df)

if __name__ == "__main__":
    pytest.main()
