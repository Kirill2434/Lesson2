
school_info =     [
    {'school_class': '11a', 'scores': [3,4,4,5,2]},
    {'school_class': '11b', 'scores': [2,5,5,3,3]},
    {'school_class': '11v', 'scores': [4,2,2,3,2]}
]  


def school_scores_avg(scores):

    for numb in scores:
        mark = numb['school_class']
        mark_school = sum(numb['scores'])/len(numb['scores'])
        
        print(mark, mark_school)
        
school_scores_avg(scores=school_info)

sum_school_marks = len(school_info)
total=sum(school_info[0]['scores']) + sum(school_info[1]['scores']) + sum(school_info[2]['scores'])
print(sum_school_marks/total)
