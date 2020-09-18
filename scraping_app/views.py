from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

#a view should return HttpResponse
#def scrape_view(request):
#    return HttpResponse("<h1>Hello World<h1>")








def scrape_function(query):
    try:
        from googlesearch import search
    except:
        print("Use <pip install google> to install the module.")

    # This is the entity that needs to be searched for
    #query="CodersForNow"

    '''
    lang >> Stands for language
    tld >> top level domain like .in or .com
    num >> number of results to be printed at a time
    start >> index for first result to retrieve
    stop >> index for last result to retreve, if passed as None, the loop will never end
    pause >> time lap between every request
    '''

    list_of_results=[]
    for i in search(query, tld="com", num=10, start=0, stop=10, pause=2):
        list_of_results.append(i)
        #print(i)
    return list_of_results

def scrape_view(request):
    if request.method=='POST':
        qry_entered=request.POST.get('query')
        
        return render(request,'scraping_app/scrape.html',{'dict':qry_entered,'search_results_key':scrape_function(qry_entered)})    
    else:
        return render(request,'scraping_app/scrape.html')

