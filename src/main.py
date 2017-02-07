import link_bfs
import wikipedia
mapping = {}
num = int(input("Enter the number of links or clicks you want to make?"))

for i in range(num):
    source = input("Enter your wikipedia article/page title: ")
    source=wikipedia.page(source)
    print(link_bfs.wikipedia_bfs(source.url, "http://en.wikipedia.org/wiki/Adolf_Hitler", mapping))
