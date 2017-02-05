import urllib.request
main = 'http://en.wikipedia.org/wiki/Main_Page'  #Main page url
def get_links(source_url, regex):

    page = urllib.request.urlopen(source_url)
    page_html = str(page.read())

    links = set()

    for link in regex.findall(page_html):
        links.add("http://en.wikipedia.org" + link.split("\"")[1])
    #Remove entries to the main page
    links.discard(main)               

    return links    #returns a set of all links from a page except the link to the main page


