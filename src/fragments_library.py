
# TODO need to introduce a system to check anonymous heterocycles and polycyclic systems

# TODO maybe add system where atom has a fragemnt attribute (so you can tell if a nitrogen is conjugated for example)

# TODO add phantom bonds to pyridine etc so as not to include pyridinium

# TODO may need to distinguish between susbistuted amine heterocycles (i.e. methyl piperidine and piperidine)


biomolecules = {
    "pyranose": ["OCC1OCC(O)C(O)C1O"],
    "pentose": ["OC1C(O)C(CO)OC1CO"]
    }

peptide_amino_acids = {
    "Methionine": ["NC(C({N})=O)CCSCW"],
    "Tyrosine": ["NC(C({N})=O)CC1=CC=C(O)C=C1"],
    "Phenylalanine": ["NC(C({N})=O)CC1=CC=CC=C1", "NC(C=O)Cc1ccccc1"],
    "Tryptophan": ["NC(CC1=CNC2=CC=CC=C12)C({N})=O", "NC(C({N})=O)CC1=CNC2=C1C=CC=C2", "NC(Cc1cnc2ccccc12)C({N})=O"],
    "Asparagine": ["NC(C({N})=O)CC(N)=O"],
    "Glutamine": ["NC(C({N})=O)CCC(N)=O"],
    "Cysteine": ["NC(C({N})=O)CS"],
    "Lysine": ["NC(C({N})=O)CCCCN"],
    "Aspartic Acid": ["NC(C({N})=O)CC(O)=O"],
    "Glutamic Acid": ["NC(C({N})=O)CCC(O)=O"],
    "Histidine": ["NC(C({N})=O)CC1=CNC=N1", "NC(CC1=CN=CN1)C({N})=O", "NC(C({N})=O)Cc1cncc1"],
    "Arginine": ["NC(C({N})=O)CCCNC(N)=N", "NC(CCCN=C(N)N)C({N})=O", "NC(C({N})=O)CCC/N=C(N)/N", r"NC(C({N})=O)CCC\N=C(N)\N", r"O=C({N})C(CCC/N=C(N)\N)N", r"O=C({N})C(CCC\N=C(N)/N)N"],
    "Tert-Leucine": ["NC(C({N})=O)C(C)(C)C"],
    "Cyclopropyl-Glycine": ["NC(C({N})=O)C1CC1"],
    "Pyroglutamic acid": ["C({N})(C(CC1)NC1=O)=O"],
    "Proline": ["C({N})(C1NCCC1)=O"],
    "Isoleucine": ["NC(C(CC)C)C({N})=O"],
    "Valine": ["NC(C({N})=O)C(C)C"],
    "Leucine": ["NC(C({N})=O)CC(C)C"],
    "Threonine": ["NC(C({N})=O)C(C)O"],
    "Serine": ["NC(C({N})=O)CO"],
    "Alanine": ["NC(C({N})=O)CW"],
    "substituted Glycine": ["NC(Y)C({N})=O", "NC(Z)C({N})=O"],
    "Glycine": ["NC(X)C({N})=O"],
    }

heterocycles = {
    "quaternary ammonium": ["NZ", "N({C})({C})({C})({C})"],
    "hantzsch ester": ["CC(NC(C)=C1C(OX)=O)=C(C1)C(OX)=O"],
    "phthalimide": ["O=C1NC(C2=CC=CC=C21)=O", "O=C1NC(C2=C1C=CC=C2)=O"],
    "1,4-dioxane": ["C1COCCO1"],
    "morpholine": ["C1COCCN1"],
    "cytosine": ["O=C1NC=CC(N)=N1"],
    "Tetrahydrothiophene": ["C1CCCS1"],
    "uracil": ["O=C(NC=C1)NC1=O"],
    "indoline": ["N1C2=CC=CC=C2CC1", "C1(CCN2)=C2C=CC=C1", "N1c2ccccc2CC1"],
    "pyrrolizidine": ["C1CCN2C1CCC2"],
    "indole": ["N1C2=CC=CC=C2C=C1", "C1(C=CN2)=C2C=CC=C1", "n1c2ccccc2cc1"],
    "indazole": ["C12=CC=CC=C1C=NN2", "C12=C(C=CC=C2)NN=C1", "c1(cccc2)c2cnn1"],
    "benzimidazole": ["C12=CC=CC=C1N=CN2", "C12=C(C=CC=C2)NC=N1", "c1(cccc2)c2ncn1"],
    "benzotriazole": ["C12=CC=CC=C1N=NN2", "C12=C(C=CC=C2)NN=N1", "c1(cccc2)c2nnn1"],
    "adenine": ["NC1=C2C(N=CN2)=NC=N1", "NC1=NC=NC2=C1NC=N2", "NC1=C2C(NC=N2)=NC=N1", "NC1=NC=NC2=C1N=CN2", "Nc1ncnc2ncnc12"],
    "purine": ["C1=NC=C2C(N=CN2)=N1", "C1(N=CN2)=C2C=NC=N1", "C12=CN=CN=C1NC=N2", "C12=C(C=NC=N2)N=CN1", "c1ncc2c(ncn2)n1"],
    "benzofuran": ["C1=C2C(C=CO2)=CC=C1", "C1(C=CO2)=C2C=CC=C1", "c1c2c(cco2)ccc1"],
    "benzothiophene": ["C1=CC2=CC=CC=C2S1", "C1(C=CS2)=C2C=CC=C1", "c1cc2ccccc2s1"],
    "benzoisoxazole": ["C1=C(ON=C2)C2=CC=C1", "C12=C(C=NO2)C=CC=C1", "c1c(onc2)c2ccc1"],
    "benzoisothiazole": ["C1=NSC2=CC=CC=C21", "C1(C=NS2)=C2C=CC=C1", "c1nsc2ccccc21"],
    "benzoxazole": ["C1=NC2=CC=CC=C2O1", "C1(N=CO2)=C2C=CC=C1", "c1nc2ccccc2o1"],
    "benzothiazole": ["C1=NC2=CC=CC=C2S1", "C1(N=CS2)=C2C=CC=C1", "c1nc2ccccc2s1"],
    "isoxazole": ["C1=NOC=C1", "c1nocc1"],
    "quinoline": ["C1=C2C(C=CC=N2)=CC=C1", "C1(C=CC=N2)=C2C=CC=C1", "C12=CC=CN=C1C=CC=C2", "c1c2c(cccn2)ccc1"],
    "isoquinoline": ["C1=CC=C(C=CN=C2)C2=C1", "C1(C=CN=C2)=C2C=CC=C1", "C12=CN=CC=C1C=CC=C2", "c1ccc(ccnc2)c2c1"],
    "quinoxaline": ["C1=NC2=CC=CC=C2N=C1", "C1(N=CC=N2)=C2C=CC=C1", "C12=NC=CN=C1C=CC=C2", "c1nc2ccccc2nc1"],
    "quinazoline": ["C1=NC2=CC=CC=C2C=N1", "C1(C=NC=N2)=C2C=CC=C1", "C12=NC=NC=C1C=CC=C2", "c1nc2ccccc2cn1"],
    "cinnoline": ["C1=CC2=CC=CC=C2N=N1", "C1(C=CN=N2)=C2C=CC=C1", "C12=NN=CC=C1C=CC=C2", "c1cc2ccccc2nn1"],
    "pteridine": ["C1=NC2=NC=CN=C2C=N1", "C1(C=NC=N2)=C2N=CC=N1", "C12=NC=NC=C1N=CC=N2", "c1nc2nccnc2cn1"],
    "chromenone": ["O=C1C=COC2=CC=CC=C21", "O=C(C=CO1)C2=C1C=CC=C2", "O=C1c2ccccc2OC=C1" ],
    "chromene": ["C1=COC2=CC=CC=C2C1", "C1(CC=CO2)=C2C=CC=C1", "c1(CC=CO2)c2cccc1"],
    "coumarin": ["O=C1C=CC2=CC=CC=C2O1", "O=C(O1)C=CC2=C1C=CC=C2", "O=C(C=C1)Oc2c1cccc2"],
    "quinolinone": ["O=C1C=CC2=CC=CC=C2N1", "O=C(N1)C=CC2=C1C=CC=C2", "O=C(N1)C=Cc2c1cccc2"],
    "isoquinolinone": ["O=C1NC=CC2=CC=CC=C21", "O=C1NC=CC2=C1C=CC=C2", "O=C1NC=Cc2c1cccc2"],
    "pyrazole": ["N1C=CC=N1", "n1cccn1"],
    "imidazole": ["C1=NC=CN1", "c1nccn1"],
    "pyridazine": ["C1=NN=CC=C1", "C1=CC=CN=N1", "c1nnccc1"],
    "pyrimidine": ["C1=NC=CC=N1", "c1ncccn1"],
    "pyrazine": ["C1=CN=CC=N1", "c1cnccn1"],
    "1,2,4-triazole": ["C1=NNC=N1", "C1=NN=CN1", "c1nncn1"],
    "1,2,3-triazole": ["N1N=NC=C1", "n1nncc1"],
    "1,2,4-triazine": ["C1=NN=CC=N1", "N1=NC=NC=C1", "c1nnccn1"],
    "1,2,3-triazine": ["C1=NN=NC=C1", "N1=NN=CC=C1", "c1nnncc1"],
    "1,3,5-triazine": ["C1=NC=NC=N1", "c1ncncn1"],
    "furan": ["C1=CC=CO1", "c1ccco1"],
    "chromane": ["C12=CC=CC=C1OCCC2", "C1(CCCO2)=C2C=CC=C1", "c12ccccc1OCCC2"],
    "thiophene": ["C1=CC=CS1", "c1cccs1"],
    "oxazole": ["C1=NC=CO1", "c1ncco1"],
    "thiazole": ["C1=CN=CS1", "c1cncs1"],
    "pyridine": ["C1=CC=CC=N1", "c1ccccn1"],
    "caprolactam": ["O=C1NCCCCC1"],
    "piperazine": ["N1CCNCC1"],
    "hydantoin": ["O=C1NCC(N1)=O"],
    "tetrazole": ["C1=NN=NN1", "C1=NNN=N1", "c1nnnn1"],
    "2-oxazolidone": ["O=C1NCCO1"],
    "guanine": ["O=C1C2C(NC=N2)N=C(N)N1", "O=C1C2C(N=C(N1)N)N=CN2", "O=C1C2C(NC(N)=N1)NC=N2", "O=C1C2C(NC(N)=N1)N=CN2"],
    "pyrolidinone": ["O=C1NCCC1"],
    "gamme-butyrrolactone": ["O=C1OCCC1"],
    "beta-lactone": ["O=C1CCO1"],
    "beta-lactam": ["O=C1CCN1"],
    "4-piperidinone": ["O=C1CCNCC1"],
    "2-piperidinone": ["O=C1NCCCC1"],
    "pyrrole": ["N1C=CC=C1", "n1cccc1"],
    "pyrrolidine": ["N1CCCC1"],
    "pyrazolidine": ["N1NCCC1"],
    "piperidine": ["C1CCNCC1"],
    }

arenes = {
    "anthracene": ["C12=CC=CC=C1C=C3C(C=CC=C3)=C2", "C1(C=C(C=CC=C2)C2=C3)=C3C=CC=C1", "c12ccccc1cc3c(cccc3)c2"],
    "phenanthrene": ["C12=CC=CC=C1C3=CC=CC=C3C=C2", "C12=CC=CC=C1C(C=CC=C3)=C3C=C2", "c12ccccc1c3ccccc3cc2"],
    "fluorene": ["C12=CC=CC=C1CC3=CC=CC=C23", "C1(C(C=CC=C2)=C2C3)=C3C=CC=C1", "C12=CC=CC=C1CC3=C2C=CC=C3", "c12c(c3c(C2)cccc3)cccc1"],
    "naphthalene": ["C12=CC=CC=C1C=CC=C2", "C1(C=CC=C2)=C2C=CC=C1", "c1ccc2c(cccc2)c1"],
    "benzene": ["C1=CC=CC=C1", "c1ccccc1"],
    }

functional_groups = {
    "azide": ["NN#N", "N=N=N", "N=N#N"],
    "tetrahydropyran": ["C1CCCCO1"],
    "tetrahydrofuran": ["C1CCCO1"],
    "cyclohexanone": ["O=C1CCCCC1"],
    "cyclohexenone": ["O=C1C=CCCC1"],
    "isocyanate": ["N=C=O"],
    "isothiocyanate": ["N=C=S"],
    "nitrosamine": ["NN=O"],
    "nitroso": ["N=O"],
    "nitro(aryl)": ["ON({c})(=O)", "ON({C1CCCCC1})(=O)", "N({c})(=O)(=O)", "N({C1CCCCC1})(=O)(=O)"],
    "nitro": ["ON(=O)", "N(=O)(=O)"],
    "1,3-dioxolane": ["C1OCCO1"],
    "Urea": ["O=C(N)N"],
    "Thiourea": ["S=C(N)N"],
    "carbamate": ["O=C(N)O"],
    "carbamyl": ["O=C({N})O"],
    "Cyano": ["C#N"],
    "trifluoromethyl": ["C(F)(F)F"],
    "difluoromethyl": ["C(F)F"],
    "hydrazide(acyl)": ["NNC=O"],
    "hydrazide(sulfonoyl)": ["NNS(=O)(=O)"],
    "oxime": ["C=NOW"],
    "oxime(substituted)": ["C=NOX"],
    "hydrazone": ["C=NN"],
    "hydrazine": ["NN"],
    "sulfonamide(aryl)": ["O=S({C1=CC=CC=C1})(N)=O", "O=S({c1ccccc1})(N)=O"],
    "sulfonamide": ["O=S(N)=O"],
    "carboxylic acid(aryl)": ["O=C({c})OW"],
    "carboxylic acid": ["O=C({C})OW"],
    "acetoxy": ["WCC(OX)=O"],
    "methyl ester": ["O=C({C})OCW", "O=C({c})OCW"],
    "ethyl ester": ["O=C({C})OC(X)CW", "O=C({c})OC(X)CW"],
    "ester": ["O=C({C})OX", "O=C({c})OX"],
    "thioamide": ["NC(=S)Y"],
    "formamide": ["NC(=O)X"],
    "primary amide": ["WNC(=O)Y"],
    "secondary amide": ["XNC(=O)Y"],
    "tertiary amide": ["YNC(=O)Y"],
    "acyl(amide)": ["O=C({N}){C}", "O=C({N}){c}"],
    "amide nitrogen": ["{O=C}(N){C}", "{O=C}(N){c}"],
    "sulfonic acid": ["O=S(O)=O"],
    "sulfone": ["O=S=O"],
    "sulfoxide": ["O=SY"],
    "thiol(aryl)": ["WS{C1=CC=CC=C1}", "WS{c1ccccc1}"],
    "thiol": ["SW"],
    "disulfide": ["SS"],
    "thioether": ["SX"],
    "guanidine": ["N=C(N)N"],
    "amidine": ["N=CN"],
    "imine": ["N=C"],
    "epoxide": ["C1OC1"],
    "enone": ["C=CC=O"],
    "enol": ["C=COW"],
    "aldehyde": ["O=C(X){C}", "O=C(X){c}"],
    "ketone(aryl)": ["O=C({c}){C}", "O=C({c}){c}", "O=C{C1=CC=CC=C1}"],
    "ketone": ["O=C({C}){C}"],
    "methoxy": ["WCOX"],
    "ether(aryl)": ["XO{C1=CC=CC=C1}", "XO{c1ccccc1}"],
    "ether": ["OX"],
    "hydroxy(aryl)": ["WO{C1=CC=CC=C1}", "WO{c1ccccc1}", "WO({c})"],
    "hydroxyl": ["WO({C})"],
    "oxo": ["O"],
    "diazo": ["N=N"],
    "dimethylamine": ["WCNCW"],
    "diethylamine": ["WC(CY)N(CY)CW"],
    "amine(aryl)": ["N{C1=CC=CC=C1}", "N{c1ccccc1}"],
    "primary amine": ["NW"],
    "secondary amine": ["NX"],
    "tertiary amine": ["NY"],
    "flouride(ammonium)": ["F{N(C)(C)(C)(C)}"],
    "chloride(ammonium)": ["Cl{N(C)(C)(C)(C)}"],
    "bromide(ammonium)": ["Br{N(C)(C)(C)(C)}"],
    "iodide(ammonium": ["I{N(C)(C)(C)(C)}"],
    "fluoro(aryl)": ["F{C1=CC=CC=C1}", "F{c1ccccc1}"],
    "chloro(aryl)": ["Cl{C1=CC=CC=C1}", "Cl{c1ccccc1}"],
    "bromo(aryl)": ["Br{C1=CC=CC=C1}", "Br{c1ccccc1}"],
    "iodo(aryl)": ["I{C1=CC=CC=C1}", "I{c1ccccc1}"],
    "fluoro": ["F"],
    "chloro": ["Cl"],
    "bromo": ["Br"],
    "iodo": ["I"],
    }

hydrocarbons = {
    "1,3-cyclohexadiene": ["C1C=CC=CC1"],
    "1,4-cyclohexadiene": ["C1=CCC=CC1"],
    "cyclohexene": ["C1CCC=CC1"],
    "1,3-cyclopentadiene": ["C1C=CC=C1"],
    "cyclopentene": ["C1CCC=C1"],
    "arene ring fragment": ["{C1}=CC=CC={C1}", "{C}=1C=CC=C{C1}", "{C1}C=CC=C{C1}"],  # TODO come back to this one
    "cis alkene": [r"{R}/C(X)=C(X)\{R}", r"{R}\C(X)=C(X)/{R}"],
    "trans alkene": [r"{R}\C(X)=C(X)\{R}", r"{R}/C(X)=C(X)/{R}"],
    "terminal alkene": ["C=CW"],
    "trisubstitued alkene": ["C(Y)=C(X)"],
    "tetrasubstitued alkene": ["C(Y)=C(Y)"],
    "alkene": ["C=C"],
    "terminal alkyne": ["C#CW"],
    "alkyne": ["C#C"],
    "cyclopropane": ["C1CC1"],
    "isopropyl": ["YC(CW)(CW)"],
    "tert-butyl": ["ZC(CW)(CW)(CW)"],
    "addamantyl": ["C1(CC2C3)CC(C2)CC3C1"],
    "cyclooctane": ["C1CCCCCCC1"],
    "cyclohpetane": ["C1CCCCCC1"],
    "cyclohexane": ["C1CCCCC1"],
    "cyclopentane": ["C1CCCC1"],
    "cyclobutane": ["C1CCC1"],
    "octyl": ["CCCCCCCC"],
    "septyl": ["CCCCCCC"],
    "hexyl": ["CCCCCC"],
    "pentyl": ["CCCCC"],
    "butyl": ["CCCC"],
    "propyl": ["CCC"],
    "ethyl": ["CC"],
    "methyl": ["CW"],
    "methylene": ["CX"],
    "tertiary carbon": ["CY"],
    "quaternary carbon": ["CZ"],
    }








