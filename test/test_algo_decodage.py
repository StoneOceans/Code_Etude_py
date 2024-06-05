# test_script.py
import pandas as pd
import numpy as np
import pytest
from src.stanToCSV import read_and_process_file, convert_and_calculate

output = read_and_process_file("RDVC-20230522.pln")
output = convert_and_calculate(output)

def test_dateRelative_realise_HeurePremiereBaliseActive_realise_jourdarchive():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'SWR9G', 'heure_de_reference'].values[0]
    assert heure_de_reference == 465.0, "heure_de_reference for SWR9G is not equal to 465.0"

def test_dateRelative_final_HeurePremiereBaliseActive_realise_veille():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'AFR903A', 'heure_de_reference'].values[0]
    assert heure_de_reference == 365.0, "heure_de_reference for AFR903A is not equal to 365.0"
    
def test_dateRelative_realise_HeurePremiereBaliseActive_realise_lendemain():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'EZY37KC', 'heure_de_reference'].values[0]
    assert heure_de_reference == -1440.0, "heure_de_reference for EZY37KC is not equal to -1440.0"
    
def test_dateRelative_realise_HeurePremiereBaliseActive_realise_veille():
    heure_de_reference=output.loc[output['callSign_prevu'] == 'TRA79Y', 'heure_de_reference'].values[0]
    assert heure_de_reference == 1720.0, "heure_de_reference for TRA79Y is not equal to 1720.0"
    
def test_dateRelative_realise_HeurePremiereBaliseActive_final_jourdarchive():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'SWR9G', 'heure_de_reference'].values[0]
    assert heure_de_reference == 465.0, "heure_de_reference for SWR9G is not equal to 465.0"
    
def test_dateRelative_realise_HeurePremiereBaliseActive_final_lendemain():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'EZY37KC', 'heure_de_reference'].values[0]
    assert heure_de_reference == -1440.0, "heure_de_reference for EZY37KC is not equal to -1440.0"
    
def test_dateRelative_realise_HeurePremiereBaliseActive_final_veille():
    heure_de_reference=output.loc[output['callSign_prevu'] == 'TRA79Y', 'heure_de_reference'].values[0]
    assert heure_de_reference == 1720.0, "heure_de_reference for TRA79Y is not equal to 1720.0"
    
def test_dateRelative_realise_HeurePremiereBalise_final_jourdarchive():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'SWR9G', 'heure_de_reference'].values[0]
    assert heure_de_reference == 465.0, "heure_de_reference for SWR9G is not equal to 465.0"
    
def test_dateRelative_realise_HeurePremiereBalise_final_lendemain():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'EZY37KC', 'heure_de_reference'].values[0]
    assert heure_de_reference == -1440.0, "heure_de_reference for EZY37KC is not equal to -1440.0"
    
def test_dateRelative_realise_HeurePremiereBalise_final_veille():
    heure_de_reference=output.loc[output['callSign_prevu'] == 'TRA79Y', 'heure_de_reference'].values[0]
    assert heure_de_reference == 1720.0, "heure_de_reference for TRA79Y is not equal to 1720.0"
    
def test_dateRelative_final_HeurePremiereBaliseActive_realise_jourdarchive():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'SWR9G', 'heure_de_reference'].values[0]
    assert heure_de_reference == 465.0, "heure_de_reference for SWR9G is not equal to 465.0"
    
def test_dateRelative_final_HeurePremiereBaliseActive_realise_lendemain():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'EZY37KC', 'heure_de_reference'].values[0]
    assert heure_de_reference == -1440.0, "heure_de_reference for EZY37KC is not equal to -1440.0"
    
def test_dateRelative_final_HeurePremiereBaliseActive_realise_veille():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'AFR903A', 'heure_de_reference'].values[0]
    assert heure_de_reference == 365.0, "heure_de_reference for AFR903A is not equal to 365.0"
    
def test_dateRelative_final_HeurePremiereBaliseActive_final_jourdarchive():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'AFR903A', 'heure_de_reference'].values[0]
    assert heure_de_reference == 365.0, "heure_de_reference for AFR903A is not equal to 365.0"
    
def test_dateRelative_final_HeurePremiereBaliseActive_final_lendemain():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'EZY37KC', 'heure_de_reference'].values[0]
    assert heure_de_reference == -1440.0, "heure_de_reference for EZY37KC is not equal to -1440.0"
    
def test_dateRelative_final_HeurePremiereBaliseActive_final_veille():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'EFW2865', 'heure_de_reference'].values[0]
    assert heure_de_reference == 2665.0, "heure_de_reference for EFW2865 is not equal to 2665.0"
    
def test_dateRelative_final_HeurePremiereBalise_final_jourdarchive():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'AFR903A', 'heure_de_reference'].values[0]
    assert heure_de_reference == 365.0, "heure_de_reference for AFR903A is not equal to 365.0"
    
def test_dateRelative_final_HeurePremiereBalise_final_lendemain():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'EZY37KC', 'heure_de_reference'].values[0]
    assert heure_de_reference == -1440.0, "heure_de_reference for EZY37KC is not equal to -1440.0"
    
def test_dateRelative_final_HeurePremiereBalise_final_veille():
    heure_de_reference = output.loc[output['callSign_prevu'] == 'EFW2865', 'heure_de_reference'].values[0]
    assert heure_de_reference == 2665.0, "heure_de_reference for EFW2865 is not equal to 2665.0"
    
def test_dateRelative_realise_jourdarchive():
    date_de_reference = df.loc[df['callSign_prevu'] == '160B', 'date_de_reference'].values[0]
    assert date_de_reference == datetime(2023, 5, 22), "date_de_reference for EFW2865 is not equal to '2023-05-22'"

def test_dateRelative_realise_lendemain():
    date_de_reference = df.loc[df['callSign_prevu'] == '160B', 'date_de_reference'].values[0]
    assert date_de_reference == datetime(2023, 5, 22), "date_de_reference for 160B is not equal to '2023-05-22'"

def test_dateRelative_realise_veille():
    date_de_reference = df.loc[df['callSign_prevu'] == '160B', 'date_de_reference'].values[0]
    assert date_de_reference == datetime(2023, 5, 22), "date_de_reference for 160B is not equal to '2023-05-22'"

def test_dateRelative_final_jourdarchive():
    date_de_reference = df.loc[df['callSign_prevu'] == '160B', 'date_de_reference'].values[1]
    assert date_de_reference == datetime(2023, 5, 22), "date_de_reference for 160B is not equal to '2023-05-22'"

def test_dateRelative_final_lendemain():
    date_de_reference = df.loc[df['callSign_prevu'] == '160B', 'date_de_reference'].values[2]
    assert date_de_reference == datetime(2023, 5, 22), "date_de_reference for 160B is not equal to '2023-05-21'"

def test_dateRelative_final_veille():
    date_de_reference = df.loc[df['callSign_prevu'] == '160B', 'date_de_reference'].values[3]
    assert date_de_reference == datetime(2023, 5, 22), "date_de_reference for 160B is not equal to '2023-05-23'"

