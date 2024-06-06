import pandas as pd
import numpy as np
from datetime import datetime, timedelta

def read_and_process_file(fichier_a_deposee):
    output = pd.DataFrame()
    tableau_vol = {}
    
    with open(fichier_a_deposee, 'r') as fichier:
        for ligne in fichier:
            words = ligne.split()
            if not words:
                continue

            if words[0] == "02":
                date_str = words[1]
                date_obj = datetime.strptime(date_str, "%d-%m-%Y")
                date_fichier = date_obj.timetuple().tm_yday

            elif words[0] == "05":
                if tableau_vol:
                    tableau_vol["isPrevu"] = isprevu
                    tableau_vol["isRealise"] = isrealise
                    tableau_vol["isFinal"] = isfinal
                    df_dictionary = pd.DataFrame([tableau_vol])
                    output = pd.concat([output, df_dictionary], ignore_index=True)
                tableau_vol = {}
                isprevu, isrealise, isfinal = False, False, False

            elif words[0] == "11":
                etat = 'prevu'
                isprevu = True

            elif words[0] == "12":
                etat = 'realise'
                isrealise = True

            elif words[0] == "13":
                if len(words) > 1 and words[1] == "=":
                    for key in list(tableau_vol.keys()):
                        if '_prevu' in key:
                            tableau_vol[key.replace('_prevu', '_final')] = tableau_vol[key]
                etat = 'final'
                isfinal = True

            elif words[0] in ["14", "20", "21", "22", "23", "24", "31", "32", "33", "36", "41", "71", "72", "80", "81", "82", "84"]:
                tableau_vol = process_lines(words, ligne, tableau_vol, etat)

    return output

def process_lines(words, ligne, tableau_vol, etat):
    if words[0] == "20":
        tableau_vol['callSign_' + etat] = words[1]
        tableau_vol['dep_' + etat] = words[2]
        tableau_vol['arr_' + etat] = words[3]
        tableau_vol['numCautra_' + etat] = words[4]
        tableau_vol['dateRelative_' + etat] = words[5]
        tableau_vol['typeAvion_' + etat] = words[6]
        tableau_vol['work_' + etat] = words[7]
        tableau_vol['work1_' + etat] = words[8].strip().ljust(9) if words[8][:2] != '??' else None

    elif words[0] == "21":
        tableau_vol['heuresDep_' + etat] = words[1]
        tableau_vol['RFL_' + etat] = words[2]
        tableau_vol['vitesse_' + etat] = words[3]
        tableau_vol['EOBT_' + etat] = words[4]

    elif words[0] == "22":
        tableau_vol['regleVol_' + etat] = words[1]
        tableau_vol['typeVol_' + etat] = words[2]
        tableau_vol['HeurePremiereBaliseActive_' + etat] = words[10]
        tableau_vol['IFPL_' + etat] = words[3].strip().ljust(10) if words[3][:2] != '??' else None
        tableau_vol['plnActive_' + etat] = words[4]
        tableau_vol['plnAnnule_' + etat] = words[5]
        tableau_vol['dateBlock_' + etat] = parse_date_block(words[7])

    elif words[0] == "23":
        tableau_vol['adresseModeS_' + etat] = words[4] if "??" not in words[4] else np.NaN

    elif words[0] == "24":
        tableau_vol['numeroPLNM_' + etat] = words[1]
        tableau_vol['flightID_' + etat] = words[2]

    elif words[0] == "31":
        tableau_vol['balise_' + etat] = words[1]

    elif words[0] == "32":
        tableau_vol['HeurePremiereBalise_' + etat] = words[1]

    elif words[0] == "33":
        tableau_vol['listeBalises_' + etat] = words[1]

    elif words[0] == "36":
        tableau_vol['indicateur_' + etat] = words[1]

    elif words[0] == "41":
        tableau_vol['carte_' + etat] = words[1]

    elif words[0] == "71":
        tableau_vol['centreTraverse_' + etat] = words[1]

    elif words[0] == "72":
        tableau_vol['listeRangPremier_' + etat] = words[1]

    elif words[0] == "80":
        tableau_vol['rangTransaction_' + etat] = words[1]

    elif words[0] == "81":
        tableau_vol = process_case_81(ligne, tableau_vol)

    elif words[0] == "82":
        tableau_vol['heure'] = (words[1][:2])
        tableau_vol['minute'] = (words[1][3:])
        tableau_vol['accuseTrt_' + etat] = words[1]
        if "CCR:" in ligne:
            tableau_vol['ccrArrival'] = words[words.index("CCR:") + 1]

    elif words[0] == "84":
        tableau_vol['final_' + etat] = words[1]

    return tableau_vol

def process_case_81(ligne, tableau_vol):
    parts = ligne.split("-")
    last_word = parts[0].split()[-1]
    if "ABI" in ligne:
        tableau_vol['typePln'] = "ABI"
    if "(FPL" in parts[0] or "(CHG)" in parts[0]:
        tableau_vol['case7'] = parts[1]
        tableau_vol['case8'] = parts[2]
        tableau_vol['case9'] = parts[3]
        tableau_vol['case10'] = parts[4]
        tableau_vol['case13'] = parts[5]
        tableau_vol['case15'] = parts[6]
        if len(parts) > 8:
            tableau_vol['case16'] = parts[7]
            tableau_vol['case18'] = parts[8]
            if tableau_vol['case18'] == "RPL":
                tableau_vol['typePln'] = "RPL"
    elif "(APL" in parts[0]:
        tableau_vol['case7'] = parts[1]
        tableau_vol['case8'] = parts[2]
        tableau_vol['case9'] = parts[3]
        tableau_vol['case10'] = parts[4]
        tableau_vol['case13'] = parts[5]
        tableau_vol['case15'] = parts[6]
        tableau_vol['typePln'] = "APL"
        if len(parts) > 8:
            tableau_vol['case16'] = parts[7]
            tableau_vol['case18'] = parts[-1]

    return tableau_vol

def parse_date_block(date_str):
    if '??' in date_str:
        return None
    elif len(date_str) == 8:
        date_obj = datetime.strptime(date_str, '%d%m%Y')
        return date_obj.timetuple().tm_yday
    else:
        return date_str.strip().ljust(6)

def convert_and_calculate(df):
    df['HeurePremiereBaliseActive_realise'] = df['HeurePremiereBaliseActive_realise'].astype('Int64')
    df['HeurePremiereBaliseActive_final'] = df['HeurePremiereBaliseActive_final'].astype('Int64')
    df['HeurePremiereBalise_final'] = df['HeurePremiereBalise_final'].astype('Int64')
    df['dateRelative_realise'] = df['dateRelative_realise'].astype('Int64')
    df['dateRelative_final'] = df['dateRelative_final'].astype('Int64')

    def calcul_HeureDeReference(row):
        try:
            date_relative = row['dateRelative_realise'] if not pd.isna(row['dateRelative_realise']) else row['dateRelative_final']
            if not pd.isna(date_relative):
                heure_active = row['HeurePremiereBaliseActive_realise'] if not pd.isna(row['HeurePremiereBaliseActive_realise']) else \
                    row['HeurePremiereBaliseActive_final'] if not pd.isna(row['HeurePremiereBaliseActive_final']) else \
                    row['HeurePremiereBalise_final']
                if not pd.isna(heure_active):
                    return int(heure_active) + (1440 if date_relative == -1 else -1440 if date_relative == 1 else 0)
        except Exception:
            return None

    df['heure_de_reference'] = df.apply(calcul_HeureDeReference, axis=1)

    def calcul_DateDeReference(row):
        try:
            date_relative = row['dateRelative_realise'] if not pd.isna(row['dateRelative_realise']) else row['dateRelative_final']
            if not pd.isna(date_relative):
                if date_relative == 0:
                    return pd.Timestamp(date_obj)
                elif date_relative == 1:
                    return pd.Timestamp(date_obj - timedelta(days=1))
                elif date_relative == -1:
                    return pd.Timestamp(date_obj + timedelta(days=1))
        except Exception as e:
            return None

    df['date_de_reference'] = df.apply(calcul_DateDeReference, axis=1)

def filter_and_analyze(df):
    df_filtre = df.dropna(subset=['heure_de_reference']).copy()
    df_filtre['transmission'] = df_filtre.apply(
        lambda row: 'ABI' if not pd.isna(row['case7']) else ('RPL' if row['typePln'] == 'RPL' else 'AUTRE'), axis=1)

    transmissions_count = df_filtre['transmission'].value_counts()
    df_filtre.sort_values(by=['heure_de_reference'], inplace=True)
    return df_filtre, transmissions_count
