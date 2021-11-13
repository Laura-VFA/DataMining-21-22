import pandas as pd
import glob

dfs = []
for file in glob.glob(f'./**/*.xls', recursive=True):
    print(file)
    try:
        iterDf = pd.DataFrame(pd.read_excel(file, skiprows=4))
    except ValueError as e:
        print(f'Error on {file}')
    iterDf['Fecha'] = file[-14:-4]
    dfs.append(iterDf)

concatDf = pd.concat(dfs)
concatDf.to_csv('../../Datasets/Aemet.csv')
