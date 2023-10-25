import json



# Ouvrir le fichier JSON en lecture
mon_fichier = open("aitweets.json", "r")
data = mon_fichier.read()

#pour le topK utlisateur
def regroupe_id(l_dict):
    dict2={}
    for dictio in l_dict:
        if dictio['id'] in dict2:
            s=dictio['id']
            dict2[s]=dict2[s]+1
        else:
            s=dictio["id"]
            dict2[s]=1
    return dict2

def topk(l_dict,k):
    dictio=regroupe_id(l_dict)
    p=[]
    maxi=0
    for j in range(k):
        for i in dictio:
            if dictio[i]>maxi:
                maxi=dictio[i]
        p.append(i)
        del dictio[i]
    return p


# Parser les données JSON en une liste de dictionnaires Python
l_dict = json.loads(data)
dict2={}

# Parcourir la liste et accéder à la clé "id" de chaque objet JSON
for objet_json in l_dict:
    print(objet_json["id"])
    print(objet_json["TweetText"])
    dict2[objet_json["id"]] = objet_json["TweetText"]


print(dict2)
print(len(l_dict))
print(topk(l_dict,5))

import pandas as pd

df = pd.read_json("aitweets.json")
print(df)