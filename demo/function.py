#from django.http import HttpResponse
from django.shortcuts import render #传达网页给用户

def home(request):
    return render(request, 'home.html')#接受用户的请求，返回网页


def count(request):
    user_text = request.GET['text']
    total_count = len(request.GET['text'])

    word_dict = {}

    for word in user_text:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    sorted_dict = sorted(word_dict.items(),key = lambda w:w[1] ,reverse=True)
    return render(request, 'count.html',
                  {'count':total_count,
                   'text':user_text,
                   'dict':word_dict,
                   'sorted':sorted_dict})#render将字典传递给网页