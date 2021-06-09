
import re
import pandas as pd

with open("../data/EPI_LogKOW_data.txt", "r", encoding='latin1') as f:
    data1 = f.read()
    log_kow_data = re.findall(r"(\d{6}-\d{2}-\d)(\s.+?\s)(-?\d{1,2}\.\d{2})", data1)

with open("../data/EPI_SMILES_CAS_data.txt", "r", encoding='latin1') as f:
    data2 = f.read()
    data2 = re.sub(r'-{3,}', '', data2)
    smiles_data = re.findall(r"(\d{6}-\d{2}-\d)(.+?\s)(\S+?)(\s|\s\s|\s.\s|\s..\s|\s.|\s..)(?=\d{6}-\d{2}-\d)", data2)

log_kow_dict = {'CAS': [mol[0] for mol in log_kow_data], 'LogP': [mol[2] for mol in log_kow_data]}
df_logp = pd.DataFrame(log_kow_dict)
print(df_logp)

smiles_dict = {'CAS': [mol[0] for mol in smiles_data], 'smiles_string': [mol[2] for mol in smiles_data]}
df_smiles = pd.DataFrame(smiles_dict)
print(df_smiles)

df_combined = pd.merge(df_logp, df_smiles, how='inner', on='CAS')
print(df_combined)

df_combined.to_csv('../data/cleaned_logp_smiles_data.csv', index=False)