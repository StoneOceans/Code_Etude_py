from datetime import datetime
import pandas as pd
import numpy as np

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

with open('/home/ajar/Téléchargements/testdebibli/RDVC-20230522(1).pln', 'r') as fichier:
  for i, ligne in enumerate(fichier):
    words = ligne.strip().split()  # Remove leading/trailing whitespaces before splitting
    if not words:  # Check for empty line
      continue

    if words[0] == "02":
      # Extract date
      date_str = words[1]
      try:
        date_obj = datetime.strptime(date_str, "%d-%m-%Y")
      except ValueError:
        # Handle potential alternative formats here (optional)
        print(f"Error parsing date: {ligne}")
        continue
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
                  tableau_vol['IFPL'+etat] = words[3].strip().ljust(10)
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
