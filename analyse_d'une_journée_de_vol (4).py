# -*- coding: utf-8 -*-
"""Analyse d'une journée de vol.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/10MmUd8fdtlzjsJslBK6FyaHaxSTCSENx
"""

from google.colab import drive
drive.mount('/content/drive')

from datetime import datetime
import pandas as pd
import numpy as np

pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 5000)
pd.set_option('display.width', 10000)
pd.options.display.max_colwidth = 1000

vol_prevu = []
vol_fini = []
vol_termine = []
tableau_vol={}
tableaux_vol=[]
iter =0
flag82=False
hneg = False
compt82 = 0
num81 = 0
prevu = False
termine=False
final=False
complet = 0
output = pd.DataFrame()
compteur = 0

with open('/content/drive/MyDrive/Colab Notebooks/RDVC-20230522.pln', 'r') as fichier:
#with open('/content/drive/MyDrive/DSNA/Redevances/RDVC-20230522.pln', 'r') as fichier:
    for i, ligne in enumerate(fichier):
        words = ligne.split()
        if words[0] == "02":
          date_str = words[1]
          date_obj = datetime.strptime(date_str, "%d-%m-%Y")
          date_fichier = date_obj.timetuple().tm_yday
        if words[0] == "05":
          if tableau_vol:
            #output = pd.concat([output, pd.DataFrame.from_dict(tableau_vol)], ignore_index=True)
            df_dictionary = pd.DataFrame([tableau_vol])
            output = pd.concat([output, df_dictionary], ignore_index=True)


          balise = ''
          hneg = False
          flag82=False
          etat = ''
        if words[0] == "11":
                etat='prevu'
        if words[0] == "12":
                etat = 'final'

        if words[0] == "13":
                etat='realise'

        if words[0] == "14":
                etat='transaction'

        if words[0] == "81":
                pass


        if words[0] == "20":
                tableau_vol['callsign'+etat]= words[1]
                tableau_vol['dep'+etat]= words[2]
                tableau_vol['arr'+etat]= words[3]
                tableau_vol['numcautra'+etat]= words[4]
                tableau_vol['typeavion'+etat]= words[6]
                tableau_vol['work'+etat]= words[7]
                if words[8][:2] == '??':
                  #tableau_vol['work1'+etat] = f"{' ' * 9}"
                  pass
                else:
                  tableau_vol['work1'+etat] = words[8].strip().ljust(9)


        if words[0] == "21":
                tableau_vol['heuresdedep'+etat]= words[1]
                tableau_vol['RFL'+etat]= words[2]
                tableau_vol['vitesse'+etat]= words[3]
                tableau_vol['EOBT'+etat]= words[4]
        if words[0] == "22":
                tableau_vol['regledevol'+etat]= words[1]
                tableau_vol['typedevol'+etat]= words[2]
                if words[3][:2] == '??':
                  #tableau_vol['IFPL'+etat] = f"{' ' * 10}"
                  pass
                else:
                  tableau_vol['IFPL_'+etat] = words[3].strip().ljust(10)
                tableau_vol['PLN_active'+etat]= words[4]
                tableau_vol['PLN_annule'+etat]= words[5]
                if '??' in words[7]:
                  #tableau_vol['date_block'+etat] = f"{' ' * 6}"
                  pass
                elif len(words[7])==8:
                  date_str = words[7]

                  # Convertir la chaîne en un objet datetime
                  date_obj = datetime.strptime(date_str, '%d%m%Y')

                  # Obtenir le numéro du jour dans l'année
                  day_vol = date_obj.timetuple().tm_yday
                  #if day_vol != date_fichier:
                  #  print('*********************Attention 22 ebot differend du jour du fichier', vol['id'])
                  #  prevu = False
                  #  termine = False
                  #  final = False
                  tableau_vol['date_block'+etat] = words[7][:4] + words[7][6:]
                else:
                  tableau_vol['date_block'+etat] = words[7].strip().ljust(6)



        if words[0] == "23":
            if "??" in words[4]:
                tableau_vol['adressemode'+etat]= np.NaN
            else:
                tableau_vol['adressemode'+etat]= words[4]
        if words[0] == "24":
                tableau_vol['numeroPLNM'+etat]= words[1]
                tableau_vol['FlightID'+etat]= words[2]
        if words[0] == "31":
                tableau_vol['balise'+etat]= words[1]
        if words[0] == "32":
                tableau_vol['listhour'+etat]= words[1]
        if words[0] == "33":
                tableau_vol['listedesbalistes'+etat]= words[1]
        if words[0] == "36":
                tableau_vol['indicateur'+etat]= words[1]
        if words[0] == "41":
                tableau_vol['carte'+etat]= words[1]
        if words[0] == "71":
                tableau_vol['centretraversé'+etat]= words[1]
        if words[0] == "72":
                tableau_vol['listederangpremier'+etat]= words[1]
        if words[0] == "80":
                tableau_vol['rangtransaction'+etat]= words[1]
        if words[0] == "81":
            if len(words) >= 15:
                parts = ligne.split("-")
                last_word = parts[0].split()[-1]
                if "(FPL" in parts[0] or "(CHG)" in parts[0]:
                  tableau_vol['case7']= parts[1]
                  tableau_vol['case8']= parts[2]
                  tableau_vol['case9']= parts[3]
                  tableau_vol['case10']= parts[4]
                  tableau_vol['case13']= parts[5]
                  tableau_vol['case15']= parts[6]
                  if len(parts)>8:
                    tableau_vol['case16']= parts[7]
                    tableau_vol['case18']= parts[8]
                  else:
                    print(ligne)
                    compteur += 1
                elif "(APL" in parts[0]:
                  tableau_vol['case7']= parts[1]
                  tableau_vol['case8']= parts[2]
                  tableau_vol['case9']= parts[3]
                  tableau_vol['case10']= parts[4]
                  tableau_vol['case13']= parts[5]
                  tableau_vol['case15']= parts[6]
                  if len(parts)>8:
                    tableau_vol['case16']= parts[7]
                    tableau_vol['case18']= parts[-1]
                  else:
                    print(ligne)
                    compteur += 1








        if words[0] == "82":
                tableau_vol['heure'] = (words[1][:2])
                tableau_vol['minute'] = (words[1][3:])
                tableau_vol['accusetrt'+etat]= words[1]
                if "CCR:" in ligne:
                  compteur_CCr = 0
                  for word in words:
                    compteur_CCr += 1
                    if word == "CCR:":
                      break
                  tableau_vol['ccr_arrival'] = words[compteur_CCr]
        if words[0] == "84":
                tableau_vol['final'+etat]= words[1]










print(output)
print(len(output))
#vol['time'] = f"{heure:02d}{minute:02d}"

vol_prevu = []
vol_fini = []
vol_termine = []
tableau_vol={}
tableaux_vol=[]
iter =0
flag82=False
hneg = False
compt82 = 0
num81 = 0
prevu = False
termine=False
final=False
complet = 0
output = pd.DataFrame()
compteur = 0

with open('/content/drive/MyDrive/Colab Notebooks/RDVC-20230522.pln', 'r') as fichier:
#with open('/content/drive/MyDrive/DSNA/Redevances/RDVC-20230522.pln', 'r') as fichier:
    for i, ligne in enumerate(fichier):
        words = ligne.split()
        if words[0] == "02":
          date_str = words[1]
          date_obj = datetime.strptime(date_str, "%d-%m-%Y")
          date_fichier = date_obj.timetuple().tm_yday
        if words[0] == "05":
          if tableau_vol:
            tableau_vol["isPrevu"]= isprevu
            tableau_vol["isRealise"] = isrealise
            tableau_vol["isFinal"] = isfinal
            #output = pd.concat([output, pd.DataFrame.from_dict(tableau_vol)], ignore_index=True)
            df_dictionary = pd.DataFrame([tableau_vol])
            output = pd.concat([output, df_dictionary], ignore_index=True)
          tableau_vol = {}
          isprevu = False
          isrealise= False
          isfinal= False


          balise = ''
          hneg = False
          flag82=False
          etat = ''
        if words[0] == "11":
                etat='prevu'
                isprevu = True
        if words[0] == "12":
                etat = 'realise'
                isrealise= True

        if words[0] == "13":
             if len(words) > 1 and words[1] == "=":
                for key in list(tableau_vol.keys()):
                    if '_prevu' in key:
                        tableau_vol[key.replace('_prevu', '_final')] = tableau_vol[key]
             etat='final'
             isfinal= True


        if words[0] == "14":
                etat='transaction'

        if words[0] == "81":
                pass


        if words[0] == "20":
                tableau_vol['callSign_'+etat]= words[1]
                tableau_vol['dep_'+etat]= words[2]
                tableau_vol['arr_'+etat]= words[3]
                tableau_vol['numCautra_'+etat]= words[4]
                tableau_vol['dateRelative_'+etat]= words[5]
                tableau_vol['typeAvion_'+etat]= words[6]
                tableau_vol['work_'+etat]= words[7]
                if words[8][:2] == '??':
                  #tableau_vol['work1'+etat] = f"{' ' * 9}"
                  pass
                else:
                  tableau_vol['work1'+etat] = words[8].strip().ljust(9)


        if words[0] == "21":
                tableau_vol['heuresDep_'+etat]= words[1]
                tableau_vol['RFL_'+etat]= words[2]
                tableau_vol['vitesse_'+etat]= words[3]
                tableau_vol['EOBT_'+etat]= words[4]
        if words[0] == "22":
                tableau_vol['regleVol_'+etat]= words[1]
                tableau_vol['typeVol_'+etat]= words[2]
                tableau_vol['HeurePremiereBaliseActive_'+etat] = words[10]
                if words[3][:2] == '??':
                  #tableau_vol['IFPL'+etat] = f"{' ' * 10}"
                  pass
                else:
                  tableau_vol['IFPL_'+etat] = words[3].strip().ljust(10)
                tableau_vol['plnActive_'+etat]= words[4]
                tableau_vol['plnAnnule_'+etat]= words[5]
                if '??' in words[7]:
                  #tableau_vol['date_block'+etat] = f"{' ' * 6}"
                  pass
                elif len(words[7])==8:
                  date_str = words[7]

                  # Convertir la chaîne en un objet datetime
                  date_obj = datetime.strptime(date_str, '%d%m%Y')

                  # Obtenir le numéro du jour dans l'année
                  day_vol = date_obj.timetuple().tm_yday
                  #if day_vol != date_fichier:
                  #  print('*********************Attention 22 ebot differend du jour du fichier', vol['id'])
                  #  prevu = False
                  #  termine = False
                  #  final = False
                  tableau_vol['dateBlock_'+etat] = words[7][:4] + words[7][6:]
                else:
                  tableau_vol['dateBlock_'+etat] = words[7].strip().ljust(6)



        if words[0] == "23":
            if "??" in words[4]:
                tableau_vol['adresseModeS_'+etat]= np.NaN
            else:
                tableau_vol['adresseModeS_'+etat]= words[4]
        if words[0] == "24":
                tableau_vol['numeroPLNM'+etat]= words[1]
                tableau_vol['flightID'+etat]= words[2]
        if words[0] == "31":
                tableau_vol['balise'+etat]= words[1]
        if words[0] == "32":
                tableau_vol['HeurePremiereBalise_'+etat]= words[1]
        if words[0] == "33":
                tableau_vol['listeBalises'+etat]= words[1]
        if words[0] == "36":
                tableau_vol['indicateur'+etat]= words[1]
        if words[0] == "41":
                tableau_vol['carte'+etat]= words[1]
        if words[0] == "71":
                tableau_vol['centreTraversé'+etat]= words[1]
        if words[0] == "72":
                tableau_vol['listeRangPremier'+etat]= words[1]
        if words[0] == "80":
                tableau_vol['rangTransaction'+etat]= words[1]
        if words[0] == "81":
            if len(words) >= 15:
                parts = ligne.split("-")
                last_word = parts[0].split()[-1]
                if "ABI" in ligne:
                  tableau_vol['typePln']= "ABI"
                if "(FPL" in parts[0] or "(CHG)" in parts[0]:
                  tableau_vol['case7']= parts[1]
                  tableau_vol['case8']= parts[2]
                  tableau_vol['case9']= parts[3]
                  tableau_vol['case10']= parts[4]
                  tableau_vol['case13']= parts[5]
                  tableau_vol['case15']= parts[6]
                  if len(parts)>8:
                    tableau_vol['case16']= parts[7]
                    tableau_vol['case18']= parts[8]
                    if tableau_vol['case18']== "RPL":
                      tableau_vol['typePln']="RPL"
                  else:
                    print(ligne)
                    compteur += 1
                elif "(APL" in parts[0]:
                  tableau_vol['case7']= parts[1]
                  tableau_vol['case8']= parts[2]
                  tableau_vol['case9']= parts[3]
                  tableau_vol['case10']= parts[4]
                  tableau_vol['case13']= parts[5]
                  tableau_vol['case15']= parts[6]
                  tableau_vol['typePln']= "APL"
                  if len(parts)>8:
                    tableau_vol['case16']= parts[7]
                    tableau_vol['case18']= parts[-1]
                  else:
                    print(ligne)
                    compteur += 1








        if words[0] == "82":
                tableau_vol['heure'] = (words[1][:2])
                tableau_vol['minute'] = (words[1][3:])
                tableau_vol['accuseTrt'+etat]= words[1]
                if "CCR:" in ligne:
                  compteurCcr = 0
                  for word in words:
                    compteurCcr += 1
                    if word == "CCR:":
                      break
                  tableau_vol['ccrArrival'] = words[compteurCcr]
        if words[0] == "84":
                tableau_vol['final'+etat]= words[1]





print(output)
print(len(output))
#vol['time'] = f"{heure:02d}{minute:02d}"

print(date_obj)

output.info()

output[output['callSign_prevu'] == 'EIN545']

print(len(output[output['HeurePremiereBalise_realise'].isna()]))

output['dateRelative_final'].value_counts()

output[output['dateRelative_realise'] == -1]



output['HeurePremiereBaliseActiv__realise'] = output['HeurePremiereBaliseActive_realise'].astype('Int64')
print(output['HeurePremiereBaliseActive_realise'])

output['HeurePremiereBaliseActive_final'] = output['HeurePremiereBaliseActive_final'].astype('Int64')
print(output['HeurePremiereBaliseActive_final'])

output['HeurePremiereBalise_final'] = output['HeurePremiereBalise_final'].astype('Int64')

output['dateRelative_realise'] = output['dateRelative_realise'].astype('Int64')
print(output['dateRelative_realise'])

output['dateRelative_final'] = output['dateRelative_final'].astype('Int64')
print(output['dateRelative_final'])

len(output['dateRelative_realise'])

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
print(output['heure_de_reference'].describe())

df_test= output[output['heure_de_reference'] >= 1440]

print(df_test[['callSign_prevu','dep_prevu','isRealise','heure_de_reference','dateRelative_realise', 'HeurePremiereBaliseActive_realise','HeurePremiereBaliseActive_final']])

df_test= output[output['heure_de_reference'] <= 0]

print(df_test[['callSign_prevu','isRealise','heure_de_reference','dateRelative_realise', 'HeurePremiereBaliseActive_realise','HeurePremiereBaliseActive_final']])

from datetime import datetime, timedelta
def calcul_DateDeReference(row):
    try:
      if not pd.isna(row['dateRelative_realise']) and not pd.isnull(row['dateRelative_realise']):
          if row['dateRelative_realise'] == 0:
                    return date_obj
          elif row['dateRelative_realise'] == 1:
                    return date_obj - timedelta(days=1)
          elif row['dateRelative_realise'] == -1:
                    return date_obj + timedelta(days=1)
      elif not pd.isna(row['dateRelative_final']) and not pd.isnull(row['dateRelative_final']):
          if row['dateRelative_final'] == 0:
                    return date_obj
          elif row['dateRelative_final'] == 1:
                    return date_obj - timedelta(days=1)
          elif row['dateRelative_final'] == -1:
                    return date_obj + timedelta(days=1)

    except Exception as e:
        return None

output['date_de_reference'] = output.apply(calcul_DateDeReference, axis=1)
print(output['date_de_reference'].describe())

output[output['callSign_prevu']== "TRA79Y"]

output[output['callSign_prevu']== "160B"]

def filtrer_vols(dataframe,filedate):
  """
  Sélectionne les lignes où la colonne `FLPL_DEPR_AIRP` commence par `LF` ou que la colonne `FLPL_ARRV_AIRP` commence par `L` ou `E` et que la colonne `FTFM_FIELD15` ou `CTFM_FIELD15` contient un des mots de la liste.

  Args:
    dataframe: Le DataFrame contenant les données de vol.

  Returns:
    Un DataFrame contenant les vols répondant aux conditions.
  """

  mots_recherches = ["ALGR"]
  #dataframe = dataframe[dataframe['date_block']==filedate]

  return dataframe.loc[
      ((dataframe['dep_realise'].str.startswith('LF')) |  # LF condition
      (dataframe['ccr_arrival'].str.contains('|'.join(mots_recherches)))) &  # Mots recherches condition
      (dataframe['PLN_activerealise'].str.contains('1')) &  # PLN_activerealise == 1 condition
      (dataframe['PLN_annulerealise'].str.contains('0'))  # PLN_annulerealise == 0 condition
  ]


# Appeler la fonction
df_stan_facture = filtrer_vols(output.copy(),20230522000000)

# Afficher le nombre de vols sélectionnés
print(f"Nombre de vols sélectionnés: {df_stan_facture.shape[0]}")

print(compteur)

output['typedevolprevu'].value_counts()

mots_recherches = ["ALGR"]

texte = output[((output['dep_realise'].str.startswith('LF')) |  # LF condition
      (output['ccr_arrival'].str.contains('|'.join(mots_recherches)))) &  # Mots recherches condition
      (output['PLN_activerealise'].str.contains('1'))]

print(len(texte))

texte.info()

"""t"""

display(texte)

eurocontrol = ['EB','ED','EF','EG','EH','EI','EK','EL','EN','EP','ES','EV','EY','LA','LB','LC','LD','LE','LG','LH','LI','LJ','LK','LM','LO','LP','LQ','LR','LS','LT','LU','LW','LY','LZ','UD','UG','GC']

print(compt82)

print(num81)

from datetime import datetime

date_str = "22-05-2023"
date_obj = datetime.strptime(date_str, "%d-%m-%Y")
day_of_year = date_obj.timetuple().tm_yday
print(day_of_year)

print(len(tableaux_vol))

output.info()

df_stan_facture = df_stan_facture.sort_values(by='callSign_prevu', ascending=True)

df_stan_facture = df_stan_facture.reset_index()

df_stan_facture.head()

df_stan_facture[df_stan_facture['callSign_final']=='THY54SK']

def generate_transmission_ecmonth(df):
  """
  Crée une nouvelle colonne "transmission" dans le DataFrame df avec la formule fournie.

  Args:
    df: Le DataFrame contenant les données de vol.

  Returns:
    Le DataFrame avec la nouvelle colonne "transmission".
  """

  # Initialiser le compteur de position
  num = 1

  # Créer une nouvelle colonne vide
  df['transmission'] = ''
  df['EOBT_prevu'] = df['EOBT_prevu'].fillna(0).astype(int)
  df['adressemode_prevu'] = df['adressemode_prevu'].fillna(f"{' ' * 6}")
  df['IFPL_prevu'] = df['IFPL_prevu'].fillna(f"{' ' * 10}")

  for index, row in df.iterrows():
    # Générer la partie numérique de la transmission
    num_str = f"{num:04d}"
    row['Sequence number'] = num_str
    heuredep = f"{num:04d}"
    row['heuresdedepprevu'] = heuredep


    # Concaténer les autres éléments de la transmission
    transmission = row['Sequence number']
    transmission += "F"
    transmission += row['heure']
    transmission += row['minute']
    transmission += row['dep_prevu']
    transmission += row['arr_prevu']
    transmission += row['callSign_prevu'].strip().ljust(9)
    transmission += 'Z'
    transmission += row['typeavion_prevu'].strip().ljust(7)
    transmission += 'Z  '
    transmission += str(row['RFLprevu']).strip().ljust(8)
    transmission +=  f"{' ' * 21}"
    transmission += str(row['date_block_prevu'])
    transmission += str(row['IFPL_prevu']).strip().ljust(10) + f"{' ' * 39}" + str(int(row['EOBT_prevu'])) + "    " + str(row['adressemode_prevu']).strip().ljust(6)

    # Incrémenter le compteur de position
    num += 1
    print(transmission)
    # Affecter la valeur à la cellule courante
    df.loc[index, 'transmission'] = transmission

  return df
df_stan_facture.fillna(0)
# Appeler la fonction
statut = 'F'


df_stan_final = generate_transmission_ecmonth(df_stan_facture.copy())
# Afficher les premières lignes du DataFrame
#print(df_ec_month['transmission'])

import plotly.graph_objects as go
import pandas as pd
from datetime import datetime

# Calculate the total number of flights
total_vols = len(output)

# Create the Plotly Indicator for total flights
fig_total = go.Figure()

fig_total.add_trace(go.Indicator(
    mode="number",
    value=total_vols,
    number={'valueformat': ",", 'font': {'size': 50}},
    title={"text": "Total Vols"},
    domain={'row': 0, 'column': 0}
))

fig_total.update_layout(
    grid={'rows': 1, 'columns': 1, 'pattern': "independent"},
    template={'data': {'indicator': [{
        'title': {'text': "Flights"},
        'mode': "number+delta+gauge"}]}}
)

# Display the total flights figure
fig_total.show()

# Define the code for Roissy (Charles de Gaulle)
roissy_code = 'LFPG'

# Filter the flights where departure or arrival airport is Roissy
flights_to_roissy = output[(output['dep_prevu'] == roissy_code) | (output['arr_prevu'] == roissy_code) |
                           (output['dep_final'] == roissy_code) | (output['arr_final'] == roissy_code)]

# Count the total number of flights for Roissy
total_flights_roissy = len(flights_to_roissy)

# Create the Plotly Indicator for Roissy flights
fig_roissy = go.Figure()

fig_roissy.add_trace(go.Indicator(
    mode="number",
    value=total_flights_roissy,
    title={"text": "Total Flights for Roissy (CDG)"},
    domain={'row': 0, 'column': 0}
))

fig_roissy.update_layout(
    grid={'rows': 1, 'columns': 1, 'pattern': "independent"},
    template={'data': {'indicator': [{
        'title': {'text': "Total Flights for Roissy"},
        'mode': "number+delta+gauge"}]}}
)

# Display the Roissy flights figure
fig_roissy.show()

arrival_to_roissy = output[(output['arr_prevu'] == roissy_code) |
                           (output['arr_final'] == roissy_code)]

# Count the total number of flights for Roissy
total_arrival_roissy = len(arrival_to_roissy)

# Create the Plotly Indicator for Roissy flights
fig_arrival_roissy = go.Figure()

fig_arrival_roissy.add_trace(go.Indicator(
    mode="number",
    value=total_arrival_roissy,
    title={"text": "Total arrival for Roissy (CDG)"},
    domain={'row': 0, 'column': 0}
))

fig_arrival_roissy.update_layout(
    grid={'rows': 1, 'columns': 1, 'pattern': "independent"},
    template={'data': {'indicator': [{
        'title': {'text': "Total arrival for Roissy"},
        'mode': "number+delta+gauge"}]}}
)

# Display the Roissy flights figure
fig_arrival_roissy.show()

nombre_lignes_deuxieme_colonne = sum(1 for ligne in tableaux_vol if len(ligne) > 2)

print("Nombre de lignes dans la deuxième colonne :", nombre_lignes_deuxieme_colonne)

for i, plan in enumerate(tableaux_vol):
  if len(plan)>1:
      if 'heure' not in plan[0][0]:
        print('pb enorme heure avec', plan)
      if plan[0][0]['heure']>23:
        plan[0][0]['heure'] = plan[1][0]['heure']
      if plan[0][0]['balise'] == 'PTGEO':
        plan[0][0]['balise'] = plan[1][0]['balise']
        print(' CS : ',plan[0][0]['id'], '   ', plan[1][0]['balise'])
        print(plan)

for i, plan in enumerate(tableaux_vol):
      if 'KFE022' in plan[0][0]['id']:
        print(plan)

liste_vols=[]
for plan in tableaux_vol:
  if plan[0][0]['id'] == 'KFE022  ':
    print(plan)
  liste_vols.append(plan[0][0])
liste_tri = sorted(liste_vols, key=lambda plan: plan["id"])

import re

# Vos expressions régulières
expression1 = r"\(FPL"
expression2 = r"\)"

# Exemple de tableau (vous pouvez le remplacer par votre propre tableau)
mon_tableau = ["(FPL avec l'expression)", "B et FPL", "C et D"]

for element in mon_tableau:
    if re.search(expression1, element) or re.search(expression2, element):
        print(f"Les expressions se trouvent dans l'élément : {element}")
    else:
        print(f"Aucune des expressions n'est présente dans l'élément : {element}")

qual = 0

qual = 0
expression1 = r"\(FPL"
expression2 = r"\)"
for i, plan in enumerate(liste_vols):
  if '81' in plan:
    if len(plan['81'])>9:
      print(plan['81'])
    test1 = False
    test2 = False
    for element in plan['81']:
        if re.search(expression1, element):
          test1 = True
        if re.search(expression2, element):
          test2 = True
    if test1 and test2:
      qual+=1

print(qual)

for i, plan in enumerate(liste_vols):
  if 'ACP2621' in plan['id']:
    print(plan['81'])

for i, plan in enumerate(liste_tri):
  if not 'heure' in plan:
    print(plan)

for i, plan in enumerate(liste_tri):
  if '81' in plan:
    print(plan)

def comparer_dob(dictionnaire1, dictionnaire2):
  """
  Compare deux dictionnaires et retourne celui avec la valeur 'dob' qui ne commence pas par '   '.

  Args:
    dictionnaire1: Le premier dictionnaire.
    dictionnaire2: Le deuxième dictionnaire.

  Returns:
    Le dictionnaire avec la valeur 'dob' qui ne commence pas par '   '.
  """
  if not dictionnaire1["jour"].startswith("   "):
    return dictionnaire1
  else:
    return dictionnaire2

def supprimer_doublons(dictionnaires):
  """
  Supprime les doublons dans une liste de dictionnaires.

  Args:
    dictionnaires: Une liste de dictionnaires.

  Returns:
    Une liste de dictionnaires sans doublons.
  """
  dictionnaires_sans_doublons = []
  ifplid_vus = set()
  for dictionnaire in dictionnaires:
    ifplid = dictionnaire["ifplid"]
    if ifplid not in ifplid_vus or ifplid == '          ':
      dictionnaires_sans_doublons.append(dictionnaire)
      ifplid_vus.add(ifplid)
    else:
      dictionnaire_existant = next(d for d in dictionnaires_sans_doublons if d["ifplid"] == ifplid)
      dictionnaire_a_conserver = comparer_dob(dictionnaire_existant, dictionnaire)
      dictionnaires_sans_doublons.remove(dictionnaire_existant)
      dictionnaires_sans_doublons.append(dictionnaire_a_conserver)
  return dictionnaires_sans_doublons

# Supprimer les doublons
liste_sans_doublons = supprimer_doublons(liste_tri)

# Afficher les résultats
print(f"Nombre de dictionnaires avant suppression: {len(liste_tri)}")
print(f"Nombre de dictionnaires après suppression: {len(liste_sans_doublons)}")



def supprimer_doublons(dictionnaires):
  """
  Supprime les doublons dans une liste de dictionnaires.

  Args:
    dictionnaires: Une liste de dictionnaires.

  Returns:
    Une liste de dictionnaires sans doublons.
  """
  dictionnaires_sans_doublons = []
  ifplid_dep_vus = set()
  for dictionnaire in dictionnaires:
    ifplid = dictionnaire["ifplid"]
    dep = dictionnaire["dep"]
    arrive = dictionnaire["arrive"]
    # Utiliser un tuple (ifplid, dep) pour vérifier les doublons
    if (ifplid, dep, arrive) not in ifplid_dep_vus or ifplid == '          ':
      dictionnaires_sans_doublons.append(dictionnaire)
      ifplid_dep_vus.add((ifplid, dep,arrive))
    else:
      dictionnaire_existant = next(d for d in dictionnaires_sans_doublons if (d["ifplid"] == ifplid and d["dep"] == dep))
      dictionnaire_a_conserver = comparer_dob(dictionnaire_existant, dictionnaire)
      dictionnaires_sans_doublons.remove(dictionnaire_existant)
      dictionnaires_sans_doublons.append(dictionnaire_a_conserver)
  return dictionnaires_sans_doublons

# Supprimer les doublons
vols_sans_doublons = supprimer_doublons(liste_tri)

# Afficher les résultats
print(f"Nombre de vols avant suppression: {len(liste_tri)}")
print(f"Nombre de vols après suppression: {len(vols_sans_doublons)}")

print(vols_sans_doublons[:20])

import pandas as pd
tableau = pd.DataFrame(vols_sans_doublons)

def recherche_mots(tableau, mots_recherches):

  """
  Fonction pour rechercher des mots dans un tableau.

  Paramètres :
  tableau (list): Le tableau de chaînes à rechercher.
  mots_recherches (list): Le tableau de mots à rechercher.

  Retourne :
  list: Une liste des éléments du tableau qui contiennent au moins un mot de recherche.
  """

  resultats = []

  for mot in mots_recherches:
    for element in tableau:
      if mot.lower() in element.lower():
        resultats.append(element)

  return resultats

mots_recherches = ["OTARO", "DOLIS", "KAMER", "REQIN", "SALMA", "CIRTA", "MOUET","CSO","ANB","BJA","ZEM"]

for i, plan in enumerate(vols_sans_doublons):
  if 'VLG2CZ' in plan['id']:
    test = any(mot in plan['81'] for mot in mots_recherches)
    test2 = recherche_mots(plan['81'], mots_recherches)
    print(plan['81'])
    print(test)
    print(test2)
    print(plan)

tableau = ['81', 'O0035PE', '2', '220004', 'O0035', '220004', 'EUCHZMFP', '(FPL-ACP2621-IS', '-B744/H-SDE2E3FGHIJ3J7M3RWXYZ/LB1D1', '-DGAA2345', '-N0495F350', 'LITE1D', 'LITEX', 'UA603', 'TAREN/N0494F370', 'UA603', 'BAKAB', 'UG859', 'BIS/N0489F390', 'UG859', 'CSO/N0485F380', 'UM2', 'PIGOS', 'UM985', 'EKSID', 'M985', 'NOSTA', 'DCT', 'NOPMU', 'DCT', 'CERVI/N0482F400', 'DCT', 'VADEM', 'DCT', 'GILIR', 'UN853', 'IXILU/N0429F240', 'UN853', 'GIVOR', 'UL47', 'GTQ/N0411F190', 'N852', 'LNO', '-EBLG0558', 'EBBR', '-CODE/4CC4BD', 'DAT/CPDLCX', '1FANS2PDC', 'DOF/230521', 'EET/DRRR0044', 'DAAA0155', 'LFFF0409', 'LIMM0446', 'LSAS0503', 'LFFF0511', 'EDGG0534', 'EBBU0535', 'IFP/MO']

mots_recherches = ["OTARO", "DOLIS", "KAMER", "REQIN", "SALMA", "CIRTA", "MOUET", "CSO", "ANB", "BJA", "ZEM"]

resultats = recherche_mots(tableau, mots_recherches)

print(f"Résultats : {resultats}")

liste_pln = []
creation = True
mots_recherches = ["OTARO", "DOLIS", "KAMER", "REQIN", "SALMA", "CIRTA", "MOUET", "CSO", "ANB", "BJA", "ZEM"]

num = 0
num81 = 0
iter = 0
plns = []
if creation:
  statut='F'
for plan in vols_sans_doublons:
  resultats=[]
  iter = iter+1
  #print(plan)
  flag_balise = False
  if '81' in plan:
    num81 += 1
    resultats = recherche_mots(plan['81'], mots_recherches)
    if resultats:
      flag_balise= True

  if plan['dep'][:2] == 'LF':
    plan['time'] = f"{plan['heure']:02d}{plan['minute']:02d}"
    plan['operator'] = 'Z  '
    plan['comment'] = f"{' ' * 21}"
    num+=1
    pln=f"{num:04d}"+statut+plan['time']+plan['dep']+plan['arrive']+plan['id']+'Z'+plan['type_avion']+plan['operator']+plan['immatriculation']+plan['comment']+plan['jour']+plan['ifplid']+plan['infono']+plan['origine']+plan['modes']
    print(pln)
    plns.append(pln)
  elif plan['dep'][0] == 'G':
    pass
  elif plan['dep'][:2] in eurocontrol:
    pass
  elif plan['balise'] == 'CSO' or plan['balise'] == 'ZEM' or plan['balise'] == 'ANB' or plan['balise'] == 'BJA' or flag_balise:
    num+=1
    plan['time'] = f"{plan['heure']:02d}{plan['minute']:02d}"
    plan['operator'] = 'Z  '
    plan['comment'] = f"{' ' * 21}"
    pln=f"{num:04d}"+"F"+plan['time']+plan['dep']+plan['arrive']+plan['id']+plan['type_avion']+plan['operator']+plan['immatriculation']+plan['comment']+plan['jour']+plan['ifplid']+plan['infono']+plan['origine']+plan['modes']
    plns.append(pln)

# Ouvrir le fichier en mode lecture
fichier = open("/content/drive/MyDrive/DSNA/Redevances/M-LF-20230601-090935-001-CESNAC.txt", "r")
# Lire toutes les lignes du fichier
lignes = fichier.readlines()
# Fermer le fichier
fichier.close()
# Créer un tableau vide
tableau_cesnac = []
tableau_said = []

# Parcourir la liste des lignes
for ligne in lignes:
    # Extraire les 26 premiers caractères de la ligne
    caracteres = ligne[9:26]
    # Ajouter les caractères au tableau
    tableau_cesnac.append(caracteres)

for ligne in plns:
    # Extraire les 26 premiers caractères de la ligne
    caracteres = ligne[9:26]
    # Ajouter les caractères au tableau
    tableau_said.append(caracteres)

print(tableau_said)

if tableau_cesnac[1] == tableau_said[0]:
  print('egalité')
else:
  print(tableau_cesnac[1],'!=',tableau_said[0])



len(tableau_cesnac[1])

len(tableau_said[0])

# Créer une liste vide pour stocker les différences
differences = []
# Créer une variable pour compter le nombre de différences
nombre_differences = 0

for valeur1, valeur2 in zip(tableau_cesnac[2], tableau_said[1]):
    # Comparer les valeurs à chaque indice
    if valeur1 != valeur2:
        # Il y a une différence
        # Ajouter la paire de valeurs à la liste des différences
        differences.append((valeur1, valeur2))
        # Incrémenter le compteur de différences
        nombre_differences += 1
# Afficher le nombre de différences
print(f"Il y a {nombre_differences} valeurs différentes entre les deux tableaux.")
# Afficher la liste des différences
print(f"Les valeurs différentes sont: {differences}")

nombre_differences = 0
# Parcourir le premier tableau
for i,valeur1 in enumerate(tableau_cesnac):
    # Vérifier si la valeur du premier tableau n'est pas dans le deuxième tableau
    nb = nombre_differences
    if valeur1 not in tableau_said:
        # Il y a une différence
        # Ajouter la valeur à la liste des différences
        print('cette valeur n\'estpas dans Le fichier généré ',valeur1,' index : ',i)

        # Incrémenter le compteur de différences
        nombre_differences += 1
    #if nb < nombre_differences:
    #  print(lignes[i])
print('nb duff = ',nombre_differences)

for i, plan in enumerate(tableaux_vol):
      if 'AUA900' in plan[0][0]['id']:
        print(plan)

for i, plan in enumerate(vols_sans_doublons):
  if 'AFR11PM' in plan['id']:
    print(plan)

for i, plan in enumerate(plns):
  if 'AUA900' in plan:
    print(plan)

# Ouvrir le fichier en mode lecture
fichier = open("/content/drive/MyDrive/DSNA/Redevances/M-LF-20230601-090935-001-CESNAC.txt", "r")
# Lire toutes les lignes du fichier
lignes = fichier.readlines()
# Fermer le fichier
fichier.close()
# Créer un tableau vide
tableau_cesnac = []
tableau_said = []

# Parcourir la liste des lignes
for ligne in lignes:
    # Extraire les 26 premiers caractères de la ligne
    caracteres = ligne[9:26]
    # Ajouter les caractères au tableau
    tableau_cesnac.append(caracteres)

for ligne in plns:
    # Extraire les 26 premiers caractères de la ligne
    caracteres = ligne[9:26]
    # Ajouter les caractères au tableau
    tableau_said.append(caracteres)

print(tableau_said)
print(tableau_cesnac)

len(tableau_said)

nombre_differences = 0
# Parcourir le premier tableau
for i,valeur1 in enumerate(tableau_said):
    # Vérifier si la valeur du premier tableau n'est pas dans le deuxième tableau
    if valeur1 not in tableau_cesnac:
        # Il y a une différence
        # Ajouter la valeur à la liste des différences
        print('cette valeur n\'estpas dans cesnac',valeur1,' index : ',i,'--- ligne complète',plns[i][:83])
        # Incrémenter le compteur de différences
        nombre_differences += 1
print('nb duff = ',nombre_differences)

import os
from datetime import datetime

# Définir le chemin du fichier
chemin_fichier = '/content/drive/MyDrive/DSNA/Redevances/'

# Obtenir la date et l'heure actuelles
maintenant = datetime.now()
date_heure_format = maintenant.strftime("%Y%m%d-%H%M%S-%f")[:-3]  # Supprimer les derniers 3 chiffres pour les millisecondes

# Nom du fichier
nom_fichier = f"M-LF-{date_heure_format}.TXT"

# Chemin complet du fichier
chemin_complet_fichier = os.path.join(chemin_fichier, nom_fichier)

# Écrire le contenu de df_facture['transmission'] dans le fichier
with open(chemin_complet_fichier, 'w') as f:
  for pln in plns:
    f.write(pln+ "\n")

print(f"Le fichier {nom_fichier} a été créé avec succès !")