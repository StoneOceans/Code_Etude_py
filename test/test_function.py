from datetime import datetime
import pandas as pd
import numpy as np
import unittest

class TestVolData(unittest.TestCase):
        # This method will be used to set up the DataFrame for testing
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
                        output = pd.concat([output, df_dictionary], ignore_index=True)
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

        output['HeurePremiereBaliseActive_realise'] = output['HeurePremiereBaliseActive_realise'].astype('Int64')
        self.output['HeurePremiereBaliseActive_final'] = self.output['HeurePremiereBaliseActive_final'].astype('Int64')
        self.output['HeurePremiereBalise_final'] = self.output['HeurePremiereBalise_final'].astype('Int64')
        self.output['dateRelative_realise'] = self.output['dateRelative_realise'].astype('Int64')
        self.output['dateRelative_final'] = self.output['dateRelative_final'].astype('Int64')

pd.testing.assert_frame_equal(self.output['HeurePremiereBaliseActive_realise'], self.output['HeurePremiereBaliseActive_realise'])
pd.testing.assert_frame_equal(self.output['HeurePremiereBaliseActive_final'], self.output['HeurePremiereBaliseActive_final'])

if __name__ == '__main__':
    unittest.main()
