import scraperwiki
import wikipedia_utils
import re
#wikipedia_utils = scraperwiki.utils.swimport("wikipedia_utils")

def clean(s):
    ''' remove references and comments '''
    s = re.sub("<ref>([^<>])*</ref>","",s)
    s = re.sub("<!--([^<>])*-->","",s)
    return s

title = "Cardis Cardell Willis"

def process(title): 
    #check if title is in list
    val = wikipedia_utils.GetWikipediaPage(title)
    res = wikipedia_utils.ParseTemplates(val["text"])
    infobox_comedian = dict(res["templates"]).get("Infobox comedian")
    influences = clean(infobox_comedian.get("influences"))
    influenced = clean(infobox_comedian.get("influenced"))
    store(title, influences, influenced)
    #add to list 
    #iterate through influenced / influences

def store(title, influences, influenced):
    return    

process(title)
#print influences
#print influenced
#print infobox_comedian    # prints just the comedian infobox



