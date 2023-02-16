candidats = ['Jean Clanche','benoit jspquoi', 'tabar lis']

def get_candidats(candidats):
    if len(candidats) < 6 :
        for k in range(6 - len(candidats)):
            candidats.append('Candidat ' + str((6-len(candidats)+1)+2*k))
        return candidats
    elif len(candidats) > 6:
        return candidats[:6] 
    else:
        return candidats
