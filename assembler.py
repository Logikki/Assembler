#ohjeet https://b1391bd6-da3d-477d-8c01-38cdf774495a.filesusr.com/ugd/44046b_b73759b866b249a0b3a715bf5a18f668.pdf

def decimalToBinary(n):
    return "{0:015b}".format(int(n))

#luetaan tiedosto ja tehdään komennoista lista
assemblyKomennot = [] #mallia ["123213","02101010"]
komennot = []
count = 0
with open ("./06/pong/PongL.asm", "r") as f: 
    for rivi in f.readlines():
        if "//" not in rivi and rivi.strip():
            komennot.append(rivi[:-1]) #poistetaan "\n"       


#dest=comp;jump
#Binary: 1 1 1 a c1 c2 c3 c4 c5 c6 d1 d2 d3 j1 j2 j3
# // Either the dest or jump fields may be empty.
# // If dest is empty, the ‘‘=’’ is omitted;
# // If jump is empty, the ‘‘;’’ is omitted.

def aKomento(komento):
    luku = int(komento[1:])
    lukuBittina =  str("0" + decimalToBinary(luku)) #muunnetaan luku 15 bittiseen 2 komplementtimuotoon
    return lukuBittina

def dest(komento):
    if komento == "M":
        return "001"
    elif komento == "D":
        return "010"
    elif komento == "MD":
        return "011"
    elif komento == "A":
        return "100"
    elif komento == "AM":
        return "101"
    elif komento == "AD":
        return "110"
    elif komento == "AMD":
        return "111"
    else:
        return "dest"

def jump(komento):
    if komento == "JGT":
        return "001"
    elif komento == "JEQ":
        return "010"
    elif komento == "JGE":
        return "011"
    elif komento =="JLT":
        return "100"
    elif komento =="JNE":
        return "101"
    elif komento == "JLE":
        return "110"
    elif komento == "JMP":
        return "111"
    else:
        return "jump"


def comp(komento):
    if komento == "0":
        return "0" + "101010"  
    elif komento == "1": 
        return "0" +"111111"
    elif komento == "-1": 
        return "0" +"111010"
    elif komento == "D": 
        return "0" +"001100"
    elif komento == "A":
        return "0" +"110000" 
    elif komento == "!D":
        return "0" +"001101"
    elif komento == "!A":
        return "0" +"110001"
    elif komento == "-D":
        return "0" +"00111"
    elif komento == "-A":
        return "0" +"110011"
    elif komento == "D+1":
        return "0" +"011111"
    elif komento == "A+1":
        return "0" +"110111"
    elif komento == "D-1":
        return "0" +"001110"
    elif komento == "A-1":
        return "0" +"110010"
    elif komento == "D+A":
        return "0" +"000010"
    elif komento == "D-A":
        return "0" +"010011"
    elif komento == "A-D":
        return "0" +"000111"
    elif komento == "D&A":
        return "0" +"000000"
    elif komento == "D|A":
        return "0" + "010101"
    elif komento == "M":
        return  "1110000"
    elif komento == "!M":
        return  "1110001"
    elif komento == "-M":
        return  "1110011"
    elif komento == "M+1":
        return  "1110111"
    elif komento == "M-1":
        return  "1110010"
    elif komento == "D+M":
        return  "1000010"
    elif komento == "D-M":
        return  "1010011"
    elif komento == "M-D":
        return  "1000111"
    elif komento == "D&M":
        return  "1000000"
    elif komento == "D|M":
        return "1010101"
    else:
        return "comp"

for komento in komennot:
    print(komento)
    jumpOsa = ""
    instrOsa = ""
    destOsa = ""
    compOsa = ""
    if "@" in komento: #jos a-komento
        assemblyKomennot.append(aKomento(komento) + "\n") #lisätään komento dictionaryyn
        continue
    else:
        #lisätään aluksi instr osa
        instrOsa = "111"

        #dest osa 
        if "=" not in komento:
            destOsa = "000"
        else:
            destOsa = dest(komento.split("=")[0]) #erotetaan dest osa ja muutetaan assemblykielelle. Lisätään dictionaryyn
            komento = komento.split("=")[1] #poistetaan dest osa kokonaan myöhempää tekemistä varten
        
        #jump osa
        if ";" not in komento: 
            jumpOsa = "000"
        else: 
            jumpOsa = jump(komento.split(";")[1])
            komento = komento.split(";")[0]

        #comp-osa
        compOsa = comp(komento)
        komentoAssemblyna = str(instrOsa) + str(compOsa) + str(destOsa) + str(jumpOsa)
        if len(komentoAssemblyna) != 16:
            print(komentoAssemblyna)

        assemblyKomennot.append(str(instrOsa) + str(compOsa) + str(destOsa) + str(jumpOsa) + "\n")

with open("testi.hack", "w") as f:
    for komento in assemblyKomennot:
        f.writelines(str(komento))