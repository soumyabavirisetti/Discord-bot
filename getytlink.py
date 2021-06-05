import urllib.request
import re
def geturl(name):
    print(name)
    search_keyword = name
    #search_keyword = list(name.split(" "))
    query = "+".join(str(x) for x in search_keyword)
    html = urllib.request.urlopen("https://www.youtube.com/results?search_query=" + query)
    video_ids = re.findall(r"watch\?v=(\S{11})", html.read().decode())
    url = "https://www.youtube.com/watch?v=" + video_ids[0]
    return url
