from django.shortcuts import render, HttpResponse
from matches.models import Match
from django.db.models import Count
# Create your views here.

def index(request):
    
    return render(request,'matches/index.html')

def question_solution(request, questionNo):
    data = []
    
    if(questionNo == '21'):
        data = question21_data()
    elif(questionNo == '22'):
        data = question22_data()
        # print("question 22")
        return render(request, 'matches/graphSolution22.html', {
            'question': questionNo[0],
            'part' : questionNo[1],
            "dataArray": data,
        })

    
    dataArray = []
    for el in data:
        li = []
        for key,val in el.items():
            li.append(val)
        dataArray.append(li)
    # print(dataArray)
    # for el in data:
    #     print(el['season'] , " : ",  el['match_count'])
    
    return render(request, 'matches/graphSolution21.html', {
        'question': questionNo[0],
        'part' : questionNo[1],
        "dataArray" : dataArray
    })


def question21_data():
    data = Match.objects.values('season').annotate(match_count=Count('id'))
    # print(data)
    return data

def question22_data():
    
    winning_matches_per_team_per_season = (
        Match.objects.values('season', 'winner')
    )
    data = {}
    for el in winning_matches_per_team_per_season:
        
        if(el['season'] not in data):
            data[el['season']] = {}
        if(el['winner'] not in data[el['season']]):
            data[el['season']][el['winner']] = 0
        
        data[el['season']][el['winner']] += 1
        
    # print(data)
    
    # Printing the results
    # for entry in data:
    #     print(f"Season: {entry['season']}, Team: {entry['winner']}, Winning Matches Count: {entry['winning_match_count']}")
    return data


    

