def isSixatEdge(liste):
    if liste[0]== 6 or liste[len(liste)-1] == 6:
        return True
    else:
        return False

def average(liste):
    snitt = sum(liste) / len(liste)
    return snitt


def median(liste):
    ny = sorted(liste)
    midt =ny[int(len(liste)/2 -0.5)]
    return midt

