import re
from cas_name_logp_data import Kow_data
from Smiles_CAS_name import Smiles_data
import pandas as pd
from find_fragments import fragmentize
from fragments_library import biomolecules, peptide_amino_acids, heterocycles, arenes, functional_groups, hydrocarbons
import os
path = "."


# list of tuples with (CAS, Chemical Name, LogP value)
CAS_LogP = re.findall(r"(\d{6}-\d{2}-\d)(.*?)([-\d ]\d\.\d{2}\s)(.*?)(?=\d{6}-\d{2}-\d)", Kow_data)

# dict with CAS as keys and properly formatted LogP as values (also gets rid of duplicates)
CAS_LogP_dict = {t[0]: t[2].strip() for t in CAS_LogP}
print(len(CAS_LogP_dict))

# list of tuples with (CAS, Chemical Name, smiles string)
CAS_smiles = re.findall(r"(\d{6}-\d{2}-\d)(.+?)(\s\S+?)(\s.?.?\s)(?=\d{6}-\d{2}-\d)", Smiles_data)

# dict with CAS as keys and properly formatted smiles string as values
CAS_smiles_dict = {t[0]: t[2].strip() for t in CAS_smiles}
print(len(CAS_smiles_dict))

# add the CAS_LogP data to the combined list, excluding any CAS numbers that
# don't show up in the CAS_smiles data.  the values are put inside a list
combined_dict = {k: [v] for k, v in CAS_LogP_dict.items() if k in CAS_smiles_dict}
combined_dict.pop("000118-03-6", None)
print(len(combined_dict))
a = input("")


# append the smiles strings to the value (which is a list containing the logP)
# of each CAS key
for k, v in CAS_smiles_dict.items():
    if k in combined_dict:
        combined_dict[k].append(v)

excluded_dict = {k: v for k, v in combined_dict.items() if "[" in v[1]}
# print(len(excluded_dict))
# for k, v in excluded_dict.items():
#     print(k, v)

combined_dict = {k: v for k, v in combined_dict.items() if "[" not in v[1]}

print(len(combined_dict))
for k, v in combined_dict.items():
    print(k, v)

CAS_data = [key for key in combined_dict]
LogP_data = [float(v[0]) for k, v in combined_dict.items()]  # convert values to numerical values
smiles_data = [v[1] for k, v in combined_dict.items()]


df1 = pd.DataFrame({"CAS": CAS_data, "LogP": LogP_data, "smiles": smiles_data})
fragments_data = []
for mol in smiles_data:
    fragments_data.append(fragmentize(mol, biomolecules, peptide_amino_acids, heterocycles, arenes, functional_groups, hydrocarbons, numeric=True))
fragments_headers = []
for d in [biomolecules, peptide_amino_acids, heterocycles, arenes, functional_groups, hydrocarbons]:
    for key in d:
        fragments_headers.append(key)

df2 = pd.DataFrame(fragments_data, columns=fragments_headers)
df3 = pd.concat([df1, df2], axis=1)

LogP_fragments_data = os.path.join(path, "LogP_fragments_data.csv")
df3.to_csv(LogP_fragments_data, index=False)

