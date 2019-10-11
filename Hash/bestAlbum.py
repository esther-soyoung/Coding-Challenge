from collections import Counter
from collections import defaultdict

def solution(genres, plays):
    ret = []    
    g = Counter()
    for i in range(len(genres)):
        g += Counter({genres[i] : plays[i]})
    g = g.most_common()
    
    dic = defaultdict(list)
    for i in range(len(genres)):
        dic[genres[i]].append((i, plays[i]))
    
    for genre in dic.keys():
        dic[genre] = sorted(dic[genre], key = lambda x : (-x[1], x[0]),reverse = False)

    for a, b in g:
        ret.append(dic[a][0][0])
        if len(dic[a]) ==1:
            continue
        ret.append(dic[a][1][0])
        
    return ret
