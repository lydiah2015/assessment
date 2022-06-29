from django.shortcuts import render
import requests

# Create your views here.

def index(request):



    url = 'https://newsapi.org/v2/everything?q=apple&from=2022-06-28&to=2022-06-28&sortBy=popularity&apiKey=44b10db924834a118afd2a0118363190'

    apple = requests.get(url).json()

    a = apple  ['articles']
    desc =[]
    title =[]
    img =[]

    for i in range(len(a)):
        f = a[i]
        title.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(title, desc, img)

    context = {'mylist': mylist}

    return render(request, 'index.html', context)