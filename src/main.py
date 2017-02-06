import link_bfs
links_on_page = {}
num = int(input("Enter the number of links or clicks you want to make?"))

for i in range(num):
    source = input("Enter your wikipedia url: ")
    print(link_bfs.wikipedia_bfs(source, "http://en.wikipedia.org/wiki/Adolf_Hitler", links_on_page))
