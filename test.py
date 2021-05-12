score1 = {'interviewer': 'a',
            'parameter1': 9,
            'parameter2': 8,
            'parameter3': 10,
            'parameter4': 7}

score2 = {'interviewer':'b', 'parameter1': 8, 'parameter2':10, 'parameter3':9, 'parameter4':9}
score3 = {'interviewer':'c', 'parameter1':9, 'parameter2':10, 'parameter3':8, 'parameter4': 7}
score4={'interviewer':'d', 'parameter1':8, 'parameter2':8, 'parameter3':7, 'parameter4':10}

scores=[score1, score2, score3, score4]

avg_dict = { 'type' : 'average', 'avg1' : 0, 'avg2' : 0, 'avg3' : 0, 'avg4' : 0}

for score in scores:
    for avg_key, score_key in zip(avg_dict.keys(), score.keys()):
        if(type(avg_dict[avg_key]) == int):
            avg_dict[avg_key] += int(score[score_key])

for avg_key in avg_dict.keys():
    if(type(avg_dict[avg_key]) == int):
        avg_dict[avg_key]/=len(scores)
    

print(avg_dict)




