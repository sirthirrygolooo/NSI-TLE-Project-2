candidats = [
    {
    'candidat': 'Jean Clanche',
    'parti': 'PS',
    'vote': 0
    },
    {
    'candidat': 'benoit jspquoi',
    'parti': 'PS',
    'vote': 0
    },
    {
    'candidat': 'tabar lis',
    'parti': 'PS',
    'vote': 0
    }
]

def get_candidats(candidats):
    if len(candidats) > 6 :
        return candidats[:6]
    elif candidats == []:
        for i in range(6):
            candidats.append({
                'candidat': 'Candidat '+str(i+1),
                'parti': 'Inconnu',
                'vote': 0
            })
        return candidats
    elif len(candidats) < 6 :
        for i in range(6-len(candidats)):
            candidats.append({
                'candidat': 'Candidat '+str((6-len(candidats))+2*i+1),
                'parti': 'Inconnu',
                'vote': 0
            })
        return candidats
    else :
        return candidats


    

    





    