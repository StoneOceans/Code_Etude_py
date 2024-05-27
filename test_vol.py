# test_vol.py

import pytest
from src.mains import parse_pln_file
import pandas as pd


def test_parse_pln_file():

    output_df = parse_pln_file('sample_test_file.pln')

    # Debug print to check output dataframe
    print(output_df)
