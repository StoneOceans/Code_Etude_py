import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import plotly.graph_objects as go

def read_and_process_file(fichier_a_deposee):
    output = pd.DataFrame()
    tableau_vol = {}
    
    with open(fichier_a_deposee, 'r') as fichier:
        for ligne in fichier:
            words = ligne.split()
            if words[0] == "02":
                date_obj = datetime.strptime(words[1], "%d-%m-%Y")
                date_fichier = date_obj.timetuple().tm_yday
            elif words[0] == "05":
                if tableau_vol:
                    df_dictionary = pd.DataFrame([tableau_vol])
                    output = pd.concat([output, df_dictionary], ignore_index=True)
                tableau_vol = {}
                isprevu = isrealise = isfinal = False
            elif words[0] == "11":
                etat = 'prevu'
                isprevu = True
            elif words[0] == "12":
                etat = 'realise'
                isrealise = True
            elif words[0] == "13":
                etat = 'final'
                isfinal = True
            elif words[0] == "20":
                tableau_vol.update({
                    f'callSign_{etat}': words[1],
                    f'dep_{etat}': words[2],
                    f'arr_{etat}': words[3],
                    f'numCautra_{etat}': words[4],
                    f'dateRelative_{etat}': words[5],
                    f'typeAvion_{etat}': words[6],
                    f'work_{etat}': words[7],
                    f'work1_{etat}': words[8].strip().ljust(9) if words[8][:2] != '??' else None
                })
            elif words[0] == "21":
                tableau_vol.update({
                    f'heuresDep_{etat}': words[1],
                    f'RFL_{etat}': words[2],
                    f'vitesse_{etat}': words[3],
                    f'EOBT_{etat}': words[4]
                })
            elif words[0] == "22":
                tableau_vol.update({
                    f'regleVol_{etat}': words[1],
                    f'typeVol_{etat}': words[2],
                    f'HeurePremiereBaliseActive_{etat}': words[10],
                    f'IFPL_{etat}': words[3].strip().ljust(10) if words[3][:2] != '??' else None,
                    f'plnActive_{etat}': words[4],
                    f'plnAnnule_{etat}': words[5],
                    f'dateBlock_{etat}': words[7][:4] + words[7][6:] if len(words[7]) == 8 else words[7].strip().ljust(6)
                })
            elif words[0] == "23":
                tableau_vol[f'adresseModeS_{etat}'] = words[4] if "??" not in words[4] else np.NaN
            elif words[0] == "24":
                tableau_vol.update({
                    f'numeroPLNM_{etat}': words[1],
                    f'flightID_{etat}': words[2]
                })
            elif words[0] == "31":
                tableau_vol[f'balise_{etat}'] = words[1]
            elif words[0] == "32":
                tableau_vol[f'HeurePremiereBalise_{etat}'] = words[1]
            elif words[0] == "33":
                tableau_vol[f'listeBalises_{etat}'] = words[1]
            elif words[0] == "36":
                tableau_vol[f'indicateur_{etat}'] = words[1]
            elif words[0] == "41":
                tableau_vol[f'carte_{etat}'] = words[1]
            elif words[0] == "71":
                tableau_vol[f'centreTraversé_{etat}'] = words[1]
            elif words[0] == "72":
                tableau_vol[f'listeRangPremier_{etat}'] = words[1]
            elif words[0] == "80":
                tableau_vol[f'rangTransaction_{etat}'] = words[1]
            elif words[0] == "81":
                parts = ligne.split("-")
                if len(parts) > 1:
                    tableau_vol.update({
                        'case7': parts[1],
                        'case8': parts[2],
                        'case9': parts[3],
                        'case10': parts[4],
                        'case13': parts[5],
                        'case15': parts[6],
                        'case16': parts[7] if len(parts) > 8 else None,
                        'case18': parts[8] if len(parts) > 8 else None
                    })
                else:
                    tableau_vol['typePln'] = 'ABI' if "ABI" in ligne else ('RPL' if parts[8] == "RPL" else "APL")
            elif words[0] == "82":
                tableau_vol.update({
                    'heure': words[1][:2],
                    'minute': words[1][3:],
                    f'accuseTrt_{etat}': words[1],
                    'ccrArrival': words[compteurCcr + 1] if "CCR:" in ligne else None
                })
            elif words[0] == "84":
                tableau_vol[f'final_{etat}'] = words[1]

    return output

def convert_and_calculate(df):
    df['HeurePremiereBaliseActive_realise'] = df['HeurePremiereBaliseActive_realise'].astype('Int64')
    df['HeurePremiereBaliseActive_final'] = df['HeurePremiereBaliseActive_final'].astype('Int64')
    df['HeurePremiereBalise_final'] = df['HeurePremiereBalise_final'].astype('Int64')
    df['dateRelative_realise'] = df['dateRelative_realise'].astype('Int64')
    df['dateRelative_final'] = df['dateRelative_final'].astype('Int64')

    def calcul_HeureDeReference(row):
        try:
            if not pd.isna(row['dateRelative_realise']):
                if not pd.isna(row['HeurePremiereBaliseActive_realise']):
                    return int(row['HeurePremiereBaliseActive_realise']) + (1440 if row['dateRelative_realise'] == -1 else -1440 if row['dateRelative_realise'] == 1 else 0)
                elif not pd.isna(row['HeurePremiereBaliseActive_final']):
                    return int(row['HeurePremiereBaliseActive_final']) + (1440 if row['dateRelative_realise'] == -1 else -1440 if row['dateRelative_realise'] == 1 else 0)
                elif not pd.isna(row['HeurePremiereBalise_final']):
                    return int(row['HeurePremiereBalise_final']) + (1440 if row['dateRelative_realise'] == -1 else -1440 if row['dateRelative_realise'] == 1 else 0)
            elif not pd.isna(row['dateRelative_final']):
                if not pd.isna(row['HeurePremiereBaliseActive_realise']):
                    return int(row['HeurePremiereBaliseActive_realise']) + (1440 if row['dateRelative_final'] == -1 else -1440 if row['dateRelative_final'] == 1 else 0)
                elif not pd.isna(row['HeurePremiereBaliseActive_final']):
                    return int(row['HeurePremiereBaliseActive_final']) + (1440 if row['dateRelative_final'] == -1 else -1440 if row['dateRelative_final'] == 1 else 0)
                elif not pd.isna(row['HeurePremiereBalise_final']):
                    return int(row['HeurePremiereBalise_final']) + (1440 if row['dateRelative_final'] == -1 else -1440 if row['dateRelative_final'] == 1 else 0)
        except Exception:
            return None

    df['heure_de_reference'] = df.apply(calcul_HeureDeReference, axis=1)
    return df

def filter_and_analyze(df):
    df_filtre = df.dropna(subset=['heure_de_reference']).copy()
    df_filtre['transmission'] = df_filtre.apply(
        lambda row: 'ABI' if not pd.isna(row['case7']) else ('RPL' if row['typePln'] == 'RPL' else 'AUTRE'), axis=1)

    transmissions_count = df_filtre['transmission'].value_counts()
    df_filtre.sort_values(by=['heure_de_reference'], inplace=True)
    return df_filtre, transmissions_count


def main():
    df = read_and_process_file('RDVC-20230522.pln')
    df = convert_and_calculate(df)
    df_filtre, transmissions_count = filter_and_analyze(df)
    visualize_data(transmissions_count)

if __name__ == "__main__":
    main()
