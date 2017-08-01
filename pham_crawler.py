from urllib import request
import re

resp = request.urlopen("http://blairbash.org/search?query=tag%3Apham&start=0")
data = str(resp.read())
data = data.split('<blockquote class="quote-body">')

for i in range(1,len(data)):
    quote = data[i]
    quote = quote[17:quote.index("</p>")].split("<br/>")

    dList = list()
    for line in quote:
        if ": " in line:
            dList.append(line)

    print(dList)
