from datetime import datetime
import pandas as pd
import numpy as np
import unittest

class TestVolData(unittest.TestCase):

    def setUp(self):
        # This method will be used to set up the DataFrame for testing
        self.output = pd.DataFrame()

        with open('RDVC-20230522.pln', 'r') as fichier:
            tableau_vol = {}
            for ligne in fichier:
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
                        self.output = pd.concat([self.output, df_dictionary], ignore_index=True)
                    tableau_vol = {}
                    isprevu = False
                    isrealise = False
                    isfinal = False

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

                if words[0] == "20":
                    tableau_vol['callSign_' + etat] = words[1]
                    tableau_vol['dep_' + etat] = words[2]
                    tableau_vol['arr_' + etat] = words[3]
                    tableau_vol['numCautra_' + etat] = words[4]
                    tableau_vol['dateRelative_' + etat] = words[5]
                    tableau_vol['typeAvion_' + etat] = words[6]
                    tableau_vol['work_' + etat] = words[7]

                if words[0] == "21":
                    tableau_vol['heuresDep_' + etat] = words[1]
                    tableau_vol['RFL_' + etat] = words[2]
                    tableau_vol['vitesse_' + etat] = words[3]
                    tableau_vol['EOBT_' + etat] = words[4]

                if words[0] == "22":
                    tableau_vol['regleVol_' + etat] = words[1]
                    tableau_vol['typeVol_' + etat] = words[2]
                    tableau_vol['HeurePremiereBaliseActive_' + etat] = words[10]

                if words[0] == "23":
                    if "??" in words[4]:
                        tableau_vol['adresseModeS_' + etat] = np.NaN
                    else:
                        tableau_vol['adresseModeS_' + etat] = words[4]

                if words[0] == "24":
                    tableau_vol['numeroPLNM_' + etat] = words[1]
                    tableau_vol['flightID_' + etat] = words[2]

        self.output['HeurePremiereBaliseActive_realise'] = self.output['HeurePremiereBaliseActive_realise'].astype('Int64')
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

        self.output['heure_de_reference'] = self.output.apply(calcul_HeureDeReference, axis=1)

    def test_same_final_and_prevu_LRQ267G(self):
        # Rule: LRQ267G should have the same values for 'final' and 'prevu'
        lrq267g = self.output[self.output['callSign_prevu'] == 'LRQ267G']
        self.assertTrue(lrq267g['isFinal'].iloc[0] == lrq267g['isPrevu'].iloc[0])

    def test_heure_de_reference_EZY37KC(self):
        # Rule: EZY37KC should have an heure_de_reference equal to a float of -1440
        ezy37kc = self.output[self.output['callSign_prevu'] == 'EZY37KC']
        self.assertEqual(ezy37kc['heure_de_reference'].iloc[0], -1440.0)

    def test_heure_de_reference_TRA79Y(self):
        # Rule: TRA79Y should have an heure_de_reference equal to a float of 1720
        tra79y = self.output[self.output['callSign_prevu'] == 'TRA79Y']
        self.assertEqual(tra79y['heure_de_reference'].iloc[0], 1720.0)

if __name__ == '__main__':
    unittest.main()
