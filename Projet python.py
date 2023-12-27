import pandas as pd
# Premiere base de donnees sur les developpeurs

# Spécifier l'URL du fichier CSV dans votre dépôt GitHub
github_csv_url = "https://raw.githubusercontent.com/Pierre-Clayton/Projet-Python-ENSAE/main/stackoverflow_full.csv"

# Charger le fichier CSV directement dans un DataFrame Pandas
df = pd.read_csv(github_csv_url, index_col="Unnamed: 0")

#%%
continent = pd.read_excel("C:/Users/cleme/Desktop/projetProg-main/" + "Countries_Languages.xls")

def countries_to_continent(country):
    name_countries = continent['Unnamed: 1']
    for i in range(len(name_countries)):
        if name_countries[i] == country:
            return continent.loc[i,'GUIDE TO COUNTRIES AND MOST WIDELY SPOKEN FIRST LANGUAGES']
    list_missing_values = ['United Kingdom of Great Britain and Northern Ireland',
     'Russian Federation',
     'United States of America',
     'Viet Nam',
     'Iran, Islamic Republic of...',
     'Hong Kong (S.A.R.)',
     'Belarus',
     'The former Yugoslav Republic of Macedonia',
     'Venezuela, Bolivarian Republic of...',
     'Syrian Arab Republic',
     'Taiwan',
     'South Korea',
     'Cameroon',
     'Republic of Moldova',
     "Lao People's Democratic Republic",
     'Democratic Republic of the Congo',
     'United Republic of Tanzania',
     'Kosovo',
     'Nomadic',
     'Congo, Republic of the...',
     'Republic of Korea',
     'Saint Kitts and Nevis',
     'Monaco',
     'Libyan Arab Jamahiriya',
     'Palestine',
     'Isle of Man',
     "Côte d'Ivoire",
     'Senegal',
     'Saint Lucia',
     'Saint Vincent and the Grenadines']
    fixed_missing_continent = ['Europe',
                               'Europe',
                               'North,Central America',
                               'Asia (West)',
                               'Asia (West)',
                               'Asia (East)',
                               'Eurpoe',
                               'Europe',
                               'South America',
                               'Asia (West)',
                               'Asia (East)',
                               'Asia (East)',
                               'Africa',
                               'Europe',
                               'Africa',
                               'Africa',
                               'Africa',
                               'Europe',
                               'Nomadic',
                               'Africa',
                               'Asia (East)',
                               'North,Central America',
                               'Europe',
                               'Asia (West)',
                               'Asia (West)',
                               'Europe',
                               'Africa',
                               'Africa',
                               'North,Central America',
                               'North,Central America']
    for i in range(len(list_missing_values)):
        if list_missing_values[i] == country:
            return fixed_missing_continent[i]
        
def countries_to_language(country):
    name_countries = continent["Unnamed: 1"]
    for i in range(len(name_countries)):
        if name_countries[i] == country:
            return continent.loc[i,'Unnamed: 5'].split(', ')
    list_missing_values = ['United Kingdom of Great Britain and Northern Ireland',
     'Russian Federation',
     'United States of America',
     'Viet Nam',
     'Iran, Islamic Republic of...',
     'Hong Kong (S.A.R.)',
     'Belarus',
     'The former Yugoslav Republic of Macedonia',
     'Venezuela, Bolivarian Republic of...',
     'Syrian Arab Republic',
     'Taiwan',
     'South Korea',
     'Cameroon',
     'Republic of Moldova',
     "Lao People's Democratic Republic",
     'Democratic Republic of the Congo',
     'United Republic of Tanzania',
     'Kosovo',
     'Nomadic',
     'Congo, Republic of the...',
     'Republic of Korea',
     'Saint Kitts and Nevis',
     'Monaco',
     'Libyan Arab Jamahiriya',
     'Palestine',
     'Isle of Man',
     "Côte d'Ivoire",
     'Senegal',
     'Saint Lucia',
     'Saint Vincent and the Grenadines']
    
    fixed_missing_language = ['English',
                              'Russian',
                              'English',
                              'Vietnamese',
                              'Persian,Farsi',
                              'Mandarin Chinese, Cantonese, English',
                              'Belarusian,Russian',
                              'Macedonian',
                              'Spanish',
                              'Arabic',
                              'Mandarin Chinese',
                              'Korean',
                              'French, English',
                              'Romanian (Moldovan)',
                              'Lao',
                              'French',
                              'Kiswahili, English',
                              'Albanian, Serbian',
                              'Unknown',
                              'French',
                              'Korean',
                              'English',
                              'French',
                              'Arabic',
                              'Arabic',
                              'Manx, English',
                              'French',
                              'French',
                              'English',
                              'English']
   
    for i in range(len(list_missing_values)):
        if list_missing_values[i] == country:
            return fixed_missing_language[i].split(',')
    

    

    

df['Continent'] = df['Country'].apply(countries_to_continent)
df['Language']  = df['Country'].apply(countries_to_language)

#%%
 # Finding the number of None values in the column Continent
none_count_cont = df['Continent'].isnull().sum()

 # Extracting the indices of None values
none_indices_cont = df.index[df['Continent'].isnull()].tolist()

 #Extracting the indices of missing values
values_at_indices_cont = df['Country'].iloc[none_indices_cont]

 #List of all missing values
data_without_duplicates_cont = values_at_indices_cont.drop_duplicates()
#%%

 # Finding the number of None values in the column Language
none_count_lang = df['Language'].isnull().sum()

 # Extracting the indices of None values
none_indices_lang = df.index[df['Language'].isnull()].tolist()

 #Extracting the indices of missing values
values_at_indices_lang = df['Language'].iloc[none_indices_lang]

 #List of all missing values
data_without_duplicates_lang = values_at_indices_lang.drop_duplicates()

#%%

hdi = pd.read_excel("C:/Users/cleme/Desktop/projetProg-main/" + "HDI.xlsx")

list_missing_countries = ['United Kingdom of Great Britain and Northern Ireland',
         'Turkey',
         'United States of America',
         'Iran, Islamic Republic of...',
         'Hong Kong (S.A.R.)',
         'Bolivia',
         'Czech Republic',
         'The former Yugoslav Republic of Macedonia',
         'Venezuela, Bolivarian Republic of...',
         'Taiwan',
         'South Korea',
         'Republic of Moldova',
         'Democratic Republic of the Congo',
         'United Republic of Tanzania',
         'Kosovo',
         'Nomadic',
         'Congo, Republic of the...',
         'Republic of Korea',
         'Swaziland',
         'Libyan Arab Jamahiriya',
         'Palestine',
         'Isle of Man',
         'Cape Verde']

fixed_missing_values = [[0.929,80.7422,17.30971909,13.4061203,45224.76564],
                        [0.838,76.0324,18.3382206,8.63313961,31032.80106],
                        [0.921,77.1982,16.28097916,13.68342972,64765.21509],
                        [0.774,73.8749,14.61524963,10.63645314,13000.7117],
                        [0.952,85.4734,17.27816963,12.22620964,62606.8454],
                        [0.692,63.6304,14.94697094,9.827750206,8111.190194],
                        [0.889,77.7283,16.21968079,12.86931038,38745.21386],
                        [0.77,73.8415,13.62443234,10.22815037,15917.75283],
                        [0.691,70.5536,12.81608,11.10727736,4810.882621],
                        [0.768,78.2107,14.2361149,7.600118446,17504.39969],
                        [None,73.2845,10.78317,None,None],
                        [0.767,68.8459,14.43299961,11.82159042,14875.33189],
                        [0.571,63.5187,12.33081527,6.166,2889.283521],
                        [0.549,66.2007,9.221489906,6.37289871,2664.329096],
                        [None,None,None,None,None],
                        [None,None,None,None,None],
                        [0.571,63.5187,12.33081527,6.166,2889.283521],
                        [None,73.2845,10.78317,None,None],
                        [0.597,57.0657,13.74434586,5.596,7678.591873],
                        [0.718,71.9112,12.85428,7.599985,15335.712],
                        [0.715,73.4727,13.35801029,9.938480377,6582.899416],
                        [None,None,None,None,None],
                        [None,None,None,None,None]]
def countries_to_hdi(country):
    name_countries = hdi["Table 1. Human Development Index and its components "]
    for i in range(len(name_countries)):
        if name_countries[i] == country:
            return hdi.loc[i,'Unnamed: 2']
    for i in range(len(list_missing_countries)):
        if list_missing_countries[i] == country:
            return fixed_missing_values[i][0]

def countries_to_le(country):
    #le = life expectency at birth
    name_countries = hdi["Table 1. Human Development Index and its components "]
    for i in range(len(name_countries)):
        if name_countries[i] == country:
            return hdi.loc[i,'Unnamed: 4']
    for i in range(len(list_missing_countries)):
        if list_missing_countries[i] == country:
            return fixed_missing_values[i][1]
    

def countries_to_eys(country):
    #eys = expected years of schooling
    name_countries = hdi["Table 1. Human Development Index and its components "]
    for i in range(len(name_countries)):
        if name_countries[i] == country:
            return hdi.loc[i,'Unnamed: 6']
    for i in range(len(list_missing_countries)):
        if list_missing_countries[i] == country:
            return fixed_missing_values[i][2]

def countries_to_gnipc(country):
    #gnipc = Gross National Income Per Capita
    name_countries = hdi["Table 1. Human Development Index and its components "]
    for i in range(len(name_countries)):
        if name_countries[i] == country:
            return hdi.loc[i,'Unnamed: 10']
    for i in range(len(list_missing_countries)):
        if list_missing_countries[i] == country:
            return fixed_missing_values[i][4]
        
df['HDI'] = df['Country'].apply(countries_to_hdi)
df['Life expectency at birth'] = df['Country'].apply(countries_to_le)
df['Expected years of schooling'] = df['Country'].apply(countries_to_eys)
df['Gross National Income Per Capita'] = df['Country'].apply(countries_to_gnipc)
#%%

 # Finding the number of None values in the column HDI
none_count_hdi = df['HDI'].isnull().sum()

 # Extracting the indices of None values
none_indices_hdi = df.index[df['HDI'].isnull()].tolist()

 #Extracting the indices of missing values
values_at_indices_hdi = df['Country'].iloc[none_indices_hdi]

 #List of all missing values
data_without_duplicates_hdi = values_at_indices_hdi.drop_duplicates()
#%%
 # Finding the number of None values in the column Life expectency at birt
none_count_le = df['Life expectency at birth'].isnull().sum()

 # Extracting the indices of None values
none_indices_le = df.index[df['Life expectency at birth'].isnull()].tolist()

 #Extracting the indices of missing values
values_at_indices_le = df['Country'].iloc[none_indices_le]

 #List of all missing values
data_without_duplicates_le = values_at_indices_le.drop_duplicates()
#%%
 # Finding the number of None values in the column Expected years of schooling
none_count_eys = df['Expected years of schooling'].isnull().sum()

 # Extracting the indices of None values
none_indices_eys = df.index[df['Expected years of schooling'].isnull()].tolist()

 #Extracting the indices of missing values
values_at_indices_eys = df['Country'].iloc[none_indices_eys]

 #List of all missing values
data_without_duplicates_eys = values_at_indices_eys.drop_duplicates()
#%%
 # Finding the number of None values in the column Gross National Income Per Capita
none_count_gnipc = df['Gross National Income Per Capita'].isnull().sum()

 # Extracting the indices of None values
none_indices_gnipc = df.index[df['Gross National Income Per Capita'].isnull()].tolist()

 #Extracting the indices of missing values
values_at_indices_gnipc = df['Country'].iloc[none_indices_gnipc]

 #List of all missing values
data_without_duplicates_gnipc = values_at_indices_gnipc.drop_duplicates()

#%%
iso = pd.read_excel("C:/Users/cleme/Desktop/projetProg-main/" + "Liste-Excel-des-pays-du-monde.xlsx")

def countries_to_iso(country):
    name_countries = iso['Unnamed: 4']
    for i in range(len(name_countries)):
        if name_countries[i] == country:
            return iso.loc[i,'Unnamed: 1']
    list_missing_values = ['United Kingdom of Great Britain and Northern Ireland',
     'Russian Federation',
     'United States of America',
     'Netherlands',
     'Iran, Islamic Republic of...',
     'Hong Kong (S.A.R.)',
     'United Arab Emirates',
     'Bolivia',
     'Czech Republic',
     'The former Yugoslav Republic of Macedonia',
     'Venezuela, Bolivarian Republic of...',
     'Dominican Republic',
     'Syrian Arab Republic',
     'Taiwan',
     'South Korea',
     'Republic of Moldova',
     "Lao People's Democratic Republic",
     'Democratic Republic of the Congo',
     'Philippines',
     'United Republic of Tanzania',
     'Kosovo',
     'Nomadic',
     'Congo, Republic of the...',
     'Republic of Korea',
     'Swaziland',
     'Libyan Arab Jamahiriya',
     'Sudan',
     'Palestine',
     'Cape Verde',
     'Niger',
     'Gambia']
    fixed_missing_values = ["GBR",
                    "RUS",
                    "USA",
                    "NLD",
                    "IRN",
                    "HKG",
                    "ARE",
                    "BOL",
                    "CZE",
                    "MKD",
                    "VEN",
                    "DOM",
                    "SYR",
                    "TWN",
                    "KOR",
                    "MDA",
                    "LAO",
                    "COG",
                    "PHL",
                    "TZA",
                    "XXK",
                    None,
                    "COG",
                    "KOR",
                    "SWZ",
                    "LBY",
                    "SDN",
                    "PSE",
                    "CPV",
                    "NER",
                    "GMB"]
    for i in range(len(list_missing_values)):
        if list_missing_values[i] == country:
            return fixed_missing_values[i]
        
df['ISO'] = df['Country'].apply(countries_to_iso)

#%%
 # Finding the number of None values in the column ISO
none_count_iso = df['ISO'].isnull().sum()

 # Extracting the indices of None values
none_indices_iso = df.index[df['ISO'].isnull()].tolist()

 #Extracting the indices of missing values
values_at_indices_iso = df['Country'].iloc[none_indices_iso]

 #List of all missing values
data_without_duplicates_iso = values_at_indices_iso.drop_duplicates()