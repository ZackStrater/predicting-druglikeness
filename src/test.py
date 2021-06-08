
import re

with open("../data/EPI_LogKOW_data.txt", "r", encoding='latin1') as f:
    data = f.read()
    num_ex = re.findall(r"(\d{6}-\d{2}-\d)(\s.+?\s)(-?\d{1,2}\.\d{2})", data)
    print(len(num_ex))


with open("../data/EPI_SMILES_CAS_data.txt", "r", encoding='latin1') as f:
    data = f.read()
    num_ex = re.findall(r"(\d{6}-\d{2}-\d)", data)
    print(len(num_ex))

# with open("../data/EPI_SMILES_CAS_data.txt", "r", encoding='latin1') as f:
#     data = f.read()
#     num_ex = re.findall(r"(\d{6}-\d{2}-\d)(\s.+?)(\s\S+?)", data)
#     print(len(num_ex))

with open("../data/EPI_SMILES_CAS_data.txt", "r", encoding='latin1') as f:
    data = f.read()
    data = re.sub(r'-{3,}', '', data)
    num_ex2 = re.findall(r"(\d{6}-\d{2}-\d)(?:.+?)(?:\s\S+?)(?:\s|\s\s|\s.\s|\s..\s|\s.|\s..)", data)
    print(len(num_ex2))

s1 = set(num_ex)
s2 = set(num_ex2)
s3 = s1.difference(s2)
print(len(s3))
print(s3)
