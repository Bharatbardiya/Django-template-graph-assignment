from django.shortcuts import render, HttpResponse
from school.models import  PrimarySchool
from django.db.models import Count
# Create your views here.

def index(request):
    return render(request,'school/index.html')

def question_solution(request, questionNo):
    data = []
    if(questionNo == '11'):
        data = question11_data()
        return render(request, 'school/graphSolution11.html', {
            'question': questionNo[0],
            'part' : questionNo[1],
            "dataArray": data
        })
    elif(questionNo == '12'):
        data = question12_data()
        return render(request, 'school/graphSolution12.html', {
            'question': questionNo[0],
            'part' : questionNo[1],
            "dataArray": data
        })
    elif(questionNo == '13'):
        data = question13_data()
        return render(request, 'school/graphSolution13.html', {
            'question': questionNo[0],
            'part' : questionNo[1],
            "dataArray": data
        })
    
    
    # return HttpResponse(f"this is question no : {questionNo}")
    

def question11_data():
    data = PrimarySchool.objects.values('district_name').annotate(schools=Count('id'))
    dataArray = []
    for d in data:
        li = [d['district_name'], d['schools']]
        dataArray.append(li)
    return dataArray

def question12_data():
    
    school_cat_per_district = (
        PrimarySchool.objects.values('district_name', 'category')
    )
    data = {}
    for el in school_cat_per_district:
        
        if(el['district_name'] not in data):
            data[el['district_name']] = {}
        if(el['category'] not in data[el['district_name']]):
            data[el['district_name']][el['category']] = 0
        
        data[el['district_name']][el['category']] += 1
        
    # print(data)
    
    
    return data


def question13_data():
    school_medium_per_district = (
        PrimarySchool.objects.values('district_name', 'medium')
    )
    data = {}
    for el in school_medium_per_district:
        
        if(el['district_name'] not in data):
            data[el['district_name']] = {}
        if(el['medium'] not in data[el['district_name']]):
            data[el['district_name']][el['medium']] = 0
        
        data[el['district_name']][el['medium']] += 1
    return data



    

