import collections

def get_winner(ballots):
    res = collections.Counter(ballots).most_common()
    x ={a : b  for (a,b) in res}
    z = [j for j in x.keys()]
    y = [i for i in x.values()]
    if y[0] > (len(ballots)//2):
        return z[0]
    else:
        return None
