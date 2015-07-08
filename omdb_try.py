import urllib2
import json
import webbrowser
from StringIO import StringIO



def my_search():

    response = urllib2.urlopen("http://www.omdbapi.com/?apikey=e729bdf0&t=x-men&y=&plot=short&r=json")
    result = response.read()
    data = json.loads(result)
##    for key, value in data.items():
##        print key+": "+value
    print data[0].key
    

my_search()


