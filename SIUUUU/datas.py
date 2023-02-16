candidats = [
    {
    'candidat': 'Jean Clanche',
    'parti': 'Clancheurs',
    'vote': 0
    },
    {
    'candidat': 'SIUUUU REU',
    'parti': 'SHEEESH',
    'vote': 0,
    'image' : ''
    },
    {
    'candidat': 'tabar lis',
    'parti': 'En Nage',
    'vote': 0,
    'image' : ''
    },
    {
    'candidat': 'Marine LeStylo',
    'parti': 'Rassemblement de la Nation ',
    'vote': 0,
    'image' : ''
    },
]

def get_candidats(candidats):
    if len(candidats) > 6 :
        return candidats[:6]
    elif candidats == []:
        for i in range(6):
            candidats.append({
                'candidat': 'Candidat '+str(i+1),
                'parti': 'Inconnu',
                'vote': 0,
                'image' : ''
            })
        return candidats
    elif len(candidats) < 6 :
        for i in range(6-len(candidats)):
            candidats.append({
                'candidat': 'Candidat '+str((6-len(candidats))+2*i+1),
                'parti': 'Inconnu',
                'vote': 0,
                'image' : ''
            })
        return candidats
    else :
        return candidats


    

    





    