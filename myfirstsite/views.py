#I have created this file-Sunanda
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # params={'name':'Pari','place':'Goa'}
    return render(request,'index.html')

     # return HttpResponse("<h1>hello Sunanda!!</h1><br/>This is Home Page<br/><a href='https://www.google.com'>Google Site</a>")

def about(request):
    return HttpResponse("This is About Us Page.<br/><a href='http://127.0.0.1:8000/index'>Back</a>")
def gallery(request):
    return HttpResponse("This is Gallery Page.<br/><a href='http://127.0.0.1:8000/index'>Back</a>")
def blog(request):
    return HttpResponse("This is Blog Page.<br/><a href='http://127.0.0.1:8000/index'>Back</a>")
def contact(request):
    return HttpResponse("This is Contact Us Page.<br/><a href='http://127.0.0.1:8000/index'>Back</a>")
def removepunc(request):
    #Get the text from textarea
    djtext=request.GET.get('tarea1','default')
    print(djtext)
    return HttpResponse("This is Remove Punctuation Us Page.<br/><a href='http://127.0.0.1:8000/index'>Back</a>")

def analyze(request):
    djtext = request.POST.get('tarea1', 'default')
    #Check1 checkboz values
    checkselect=request.POST.get('check1','off')
    checkfullcaps = request.POST.get('check2', 'off')
    checknewlinermv = request.POST.get('check3', 'off')
    checkspacermv = request.POST.get('check4', 'off')
    checkcharcount = request.POST.get('check5', 'off')
    checknumrmv = request.POST.get('check6', 'off')
    # Check if check1 is on
    if checkselect == "on":
        #Code for removing punctuations from the string
        punctuations='''!"#$%&'()*+,-./:;?@[\]^_`{|}~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations','analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html',params) #to show the next page analyze.html
    #check if check2 is on
    if checkfullcaps == "on":
        analyzed=""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if checknewlinermv == "on":
        analyzed = ""
        for char in djtext:
            if char !='\n' and char!='\r':
                analyzed = analyzed + char
        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if checkspacermv == "on":
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index]==" " and djtext[index+1] == " "):
                analyzed=analyzed+char

        params = {'purpose': 'Removed Extra Spaces', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if checkcharcount=="on":
        count=0
        analyzed=""
        for char in djtext:
            count=count+1
            analyzed=analyzed+char
        params = {'purpose': 'Character Count', 'analyzed_text': analyzed,'count':count}
        djtext = analyzed

    if checknumrmv == "on":
        analyzed=""
        for char in djtext:
            if not char.isdigit():
                analyzed=analyzed+char
        #analyzed=''.join([i for i in djtext if not i.isdigit()])
        params = {'purpose': 'Number Remover', 'analyzed_text': analyzed}
        djtext = analyzed

    if (checkselect != "on" and checkfullcaps != "on" and checknewlinermv != "on" and checkspacermv != "on" and checkcharcount!="on" and checknumrmv!="on"):
        return HttpResponse("Error : Please Select any of The Operations !! Try Again !!")
        # return render(request, 'analyze.html', params)

    # else:
    #     return HttpResponse("Error")
    return render(request, 'analyze.html', params)
    # return HttpResponse("This is Remove Punctuation Us Page.<br/><a href='http://127.0.0.1:8000/index'>Back</a>")

def ex1(request):
    s='''<body bgcolor="cyan"><h2>Navigation Bar<br/><h2>
        <a href="https://www.google.com">Google Site</a><br/>
        <a href="https://www.facebook.com">Facebook</a><br/>
        <a href="https://www.flipkart.com">Flipkart</a><br/></body>'''
    return HttpResponse(s)