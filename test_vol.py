import pytest
from src.mains import parse_pln_file
import pandas as pd

def test_parse_pln_file():
    # Prepare a sample file content
    sample_content = """\
05
11
20 ETH575 KORD HAAB 9273 -1 B788 0000 ETAOU 0
21 -525 350 485 -525
22 I S AA47735238 0 0 FPL 21052023 SANDY 0 0 21-05-2023 00:00
23 0 0 0 ??????
24   -1 ???????? 0
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
24   -1 ???????? 0
2R LASAT390
31 SANDY MOTOX RUCAC LESDO RANUX ETINO NEBAX LASAT DEVDI 
32 -113 -113 -112 -100 -93 -89 -82 -79 -72 
33 370 390 390 390 390 390 390 390 370 
36 0 0 0 0 0 0 0 0 0 
41 HN GL HR HE 5M 
71 EGGG REIM ZURI 
72 1 2 5 
12
20 ETH575 KORD HAAB   -1 -1 B788 0000 ETAOU 0
21 -525 390 485 -525
22 I S AA47735238 1 0 FPL 21052023 MOTOX 1 1328 21-05-2023 00:00
23 0 0 0 ??????
24   -1 ???????? 0
2R ??
31 MOTOX PTGEO PTGEO PTGEO PTGEO PTGEO PTGEO 
32 -112 -112 -112 -101 -90 -83 -78 
33 390 390 390 390 390 390 390 
36 0 0 0 0 0 0 0 
41 HN HR KF HE HH 
71 REIM 
72 1 
14
80 1
81 O8248PE99 211808         O8248     211808 EUCHZMFP (FPL-ETH575-IS -B788/H-SADE1E3FGHIJ2J3J4J5J7LM1M2OP1P2P3RVWXYZ/LB1D1 -KORD1515 -N0485F350 ELX DCT MBS DCT 47N080W 5130N07000W DCT JANJO/M084F370 DCT 56N050W 57N040W 57N030W 56N020W DCT PIKIL/N0479F370 DCT SOVED DCT NIBOG/N0479F370 DCT SOSIM L15 MOTOX UL15 NEBAX DCT LASAT/N0475F390 DCT DEVDI DCT ODINA DCT LEVDI DCT NIMAN DCT ARLOS UN4 SALUN N705 MMA/N0482F410 N705 BOPIX N710 TAKRI P751 LXR M999 JDW G650 RASKA/N0487F400 UG650 KONET/N0482F390 DCT
82 18:08 TRANSACTION NO 1   CCR: EGGG REIM ZURI
83 ETH575 LETAOUI  B788479 370             212152F    S KORDHAABYW
84 ETH575 LETAOUI  B788479 370             212152F    S KORDHAABYW
80 2
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
