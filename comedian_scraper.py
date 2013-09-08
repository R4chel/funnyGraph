import scraperwiki
import wikipedia_utils
#wikipedia_utils = scraperwiki.utils.swimport("wikipedia_utils")

title = "Aquamole Pot"

val = wikipedia_utils.GetWikipediaPage(title)
res = wikipedia_utils.ParseTemplates(val["text"])
print res               # prints everything we have found in the text
infobox_ukcave = dict(res["templates"]).get("Infobox ukcave")
print infobox_ukcave    # prints just the ukcave infobox
