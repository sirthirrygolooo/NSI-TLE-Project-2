candidats = [
    {
    'candidat': 'Jean Clanche',
    'parti': 'Clancheurs',
    'vote': 436,
    'presence': 110,
    'image' : r"https://download.vikidia.org/vikidia/fr/images/thumb/4/47/T%C3%AAte_d'ornithorynque.jpg/166px-T%C3%AAte_d'ornithorynque.jpg"
    },
    {
    'candidat': 'SIUUUU REU',
    'parti': 'SHEEESH',
    'vote': 526,
    'presence': 341,
    'image' : r"http://apluche.com/image/peluches-d-eau/1960-ornithorynque__deponia_.jpg"
    },
    {
    'candidat': 'tabar lis',
    'parti': 'En Nage',
    'vote': 659,
    'presence': 76,
    'image' : r"http://jessleo.j.e.pic.centerblog.net/b45c8683.png"
    },
    {
    'candidat': 'Marine LeStylo',
    'parti': 'Rassemblement de la Nation ',
    'vote': 320,
    'presence': 50,
    'image' : r"https://derpicdn.net/img/view/2020/1/19/2251837__safe_artist-colon-stjonal_pinkie+pie_cursed+image_good+luck+sleeping+tonight_ice+age_kill+it+with+fire_looking+at+you_nightmare+fuel_sid_sid+the+sloth_.png"
    },
    {
        'candidat': "Jean Neymar",
        'parti': "La Marre",
        'vote': 546,
        'presence': 3,
        'image': r"https://www.soprono.com/_uploads/groupe/15/14092_189x189.jpg"
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
                'vote': 0,
                'presence': 0,
                'image' : r"http://getdrawings.com/free-icon-bw/anonymous-avatar-icon-19.png"
            })
        return candidats
    elif len(candidats) < 6 :
        for i in range(6-len(candidats)):
            candidats.append({
                'candidat': 'Candidat '+str((6-len(candidats))+2*i+1),
                'parti': 'Inconnu',
                'vote': 0,
                'presence': 0,
                'image' : r"http://getdrawings.com/free-icon-bw/anonymous-avatar-icon-19.png"
            })
        return candidats
    else :
        return candidats


def get_stats(candidats):
    stats = [{
        'Total': 0,
        'Blanc': 50,
        '!Blanc': 0,
        'Presentiel': 0,
        'Distanciel': 0,
    }]
    for candidat in candidats:
        stats[0]['!Blanc'] += candidat['vote']
        stats[0]['Presentiel'] += candidat['presence']
        stats[0]['Distanciel'] += candidat['vote'] - candidat['presence']

    stats[0]['Total'] = stats[0]['!Blanc'] + stats[0]['Blanc']
    return stats


    

    





    