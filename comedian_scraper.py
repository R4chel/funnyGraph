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

val = wikipedia_utils.GetWikipediaPage(title)
res = wikipedia_utils.ParseTemplates(val["text"])
infobox_comedian = dict(res["templates"]).get("Infobox comedian")
influences = infobox_comedian.get("influences")
influenced = infobox_comedian.get("influenced")
print clean(influences)
print clean(influenced)

#print influences
#print influenced
#print infobox_comedian    # prints just the comedian infobox



