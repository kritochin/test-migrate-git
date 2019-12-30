from django.shortcuts import render
from newsapi import NewsApiClient
import json
#Initializing API KEY 
newsapi = NewsApiClient(api_key='64f09c3d3cec421abc22451aabd11c5a')
all_articles = newsapi.get_everything(q='bitcoin',sources='google,the-verge,cnbc,bloomberg',language='en',sort_by='relevancy')

# loading all_articles as json 
new = json.dumps(all_articles)
# This will allow us to create creat dictionary from the json which will make easier for us to use the data 
data = json.loads(new)
def index(request):
    return render(request,'index.html',{'data':data})