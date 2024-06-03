from datetime import datetime
import pandas as pd
import numpy as np
import unittest


class TestVolData(unittest.TestCase):

    def setUp(self):
        # This method will be used to set up the DataFrame for testing
        vol_prevu = []
        vol_fini = []
        vol_termine = []
        tableau_vol = {}
        tableaux_vol = []
        iter = 0
        flag82 = False
        hneg = False
        compt82 = 0
        num81 = 0
        prevu = False
        termine = False
        final = False
        complet = 0
        output = pd.DataFrame()
        compteur = 0

        with open('RDVC-20230522.pln', 'r') as fichier:
            for i, ligne in enumerate(fichier):
                words = ligne.split()
                if words[0] == "02":
                    date_str = words[1]
                    date_obj = datetime.strptime(date_str, "%d-%m-%Y")
                    date_fichier = date_obj.timetuple().tm_yday
                if words[0] == "05":
                    if tableau_vol:
                        tableau_vol["isPrevu"] = isprevu
                        tableau_vol["isRealise"] = isrealise
                        tableau_vol["isFinal"] = isfinal
                        df_dictionary = pd.DataFrame([tableau_vol])
                        output = pd.concat([output, df_dictionary], ignore_index=True)
                    tableau_vol = {}
                    isprevu = False
                    isrealise = False
                    isfinal = False

                    balise = ''
                    hneg = False
                    flag82 = False
                    etat = ''
                if words[0] == "11":
                    etat = 'prevu'
                    isprevu = True
                if words[0] == "12":
                    etat = 'realise'
                    isrealise = True
                if words[0] == "13":
                    if len(words) > 1 and words[1] == "=":
                        for key in list(tableau_vol.keys()):
                            if '_prevu' in key:
                                tableau_vol[key.replace('_prevu', '_final')] = tableau_vol[key]
                    etat = 'final'
                    isfinal = True
                if words[0] == "14":
                    etat = 'transaction'
                if words[0] == "81":
                    pass
                if words[0] == "20":
                    tableau_vol['callSign_' + etat] = words[1]
                    tableau_vol['dep_' + etat] = words[2]
                    tableau_vol['arr_' + etat] = words[3]
                    tableau_vol['numCautra_' + etat] = words[4]
                    tableau_vol['dateRelative_' + etat] = words[5]
                    tableau_vol['typeAvion_' + etat] = words[6]
                    tableau_vol['work_' + etat] = words[7]
                    if words[8][:2] == '??':
                        pass
                    else:
                        tableau_vol['work1' + etat] = words[8].strip().ljust(9)
                if words[0] == "21":
                    tableau_vol['heuresDep_' + etat] = words[1]
                    tableau_vol['RFL_' + etat] = words[2]
                    tableau_vol['vitesse_' + etat] = words[3]
                    tableau_vol['EOBT_' + etat] = words[4]
                if words[0] == "22":
                    tableau_vol['regleVol_' + etat] = words[1]
                    tableau_vol['typeVol_' + etat] = words[2]
                    tableau_vol['HeurePremiereBaliseActive_' + etat] = words[10]
                    if words[3][:2] == '??':
                        pass
                    else:
                        tableau_vol['IFPL_' + etat] = words[3].strip().ljust(10)
                    tableau_vol['plnActive_' + etat] = words[4]
                    tableau_vol['plnAnnule_' + etat] = words[5]
                    if '??' in words[7]:
                        pass
                    elif len(words[7]) == 8:
                        date_str = words[7]
                        date_obj = datetime.strptime(date_str, '%d%m%Y')
                        day_vol = date_obj.timetuple().tm_yday
                        tableau_vol['dateBlock_' + etat] = words[7][:4] + words[7][6:]
                    else:
                        tableau_vol['dateBlock_' + etat] = words[7].strip().ljust(6)
                if words[0] == "23":
                    if "??" in words[4]:
                        tableau_vol['adresseModeS_' + etat] = np.NaN
                    else:
                        tableau_vol['adresseModeS_' + etat] = words[4]
                if words[0] == "24":
                    tableau_vol['numeroPLNM' + etat] = words[1]
                    tableau_vol['flightID' + etat] = words[2]
                if words[0] == "31":
                    tableau_vol['balise' + etat] = words[1]
                if words[0] == "32":
                    tableau_vol['HeurePremiereBalise_' + etat] = words[1]
                if words[0] == "33":
                    tableau_vol['listeBalises' + etat] = words[1]
                if words[0] == "36":
                    tableau_vol['indicateur' + etat] = words[1]
                if words[0] == "41":
                    tableau_vol['carte' + etat] = words[1]
                if words[0] == "71":
                    tableau_vol['centreTraversé' + etat] = words[1]
                if words[0] == "72":
                    tableau_vol['listeRangPremier' + etat] = words[1]
                if words[0] == "80":
                    tableau_vol['rangTransaction' + etat] = words[1]
                if words[0] == "81":
                    if len(words) >= 15:
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
                            else:
                                print(ligne)
                                compteur += 1
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
                            else:
                                print(ligne)
                                compteur += 1
                if words[0] == "82":
                    tableau_vol['heure'] = (words[1][:2])
                    tableau_vol['minute'] = (words[1][3:])
                    tableau_vol['accuseTrt' + etat] = words[1]
                    if "CCR:" in ligne:
                        compteurCcr = 0
                        for word in words:
                            compteurCcr += 1
                            if word == "CCR:":
                                break
                        tableau_vol['ccrArrival'] = words[compteurCcr]
                if words[0] == "84":
                    tableau_vol['final' + etat] = words[1]
        
        self.output['HeurePremiereBaliseActiv__realise'] = self.output['HeurePremiereBaliseActive_realise'].astype('Int64')
        self.output['HeurePremiereBaliseActive_final'] = self.output['HeurePremiereBaliseActive_final'].astype('Int64')
        self.output['HeurePremiereBalise_final'] = self.output['HeurePremiereBalise_final'].astype('Int64')
        self.output['dateRelative_realise'] = self.output['dateRelative_realise'].astype('Int64')
        self.output['dateRelative_final'] = self.output['dateRelative_final'].astype('Int64')

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

    output['heure_de_reference'] = output.apply(calcul_HeureDeReference, axis=1)

    pd.testing.assert_frame_equal(output['heure_de_reference']),output['heure_de_reference'])


if __name__ == '__main__':
    unittest.main()