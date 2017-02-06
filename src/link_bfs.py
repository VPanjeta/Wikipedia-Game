from queue import Queue
import re
import get_links

link_exp = re.compile('(?:a href=("\/wiki\/[^:]*?"))')


def wikipedia_bfs(source_url, end_url, shortest_mapping):

    shortest_mapping[end_url] = None
    q = Queue()
    previous_page = {}
    dist = 0
    curr_path = []
    distance = float("inf")

    previous_page[source_url] = None
    q.put(source_url)

    # If source url is the destination
    if source_url == end_url:
        return [source_url, end_url]

    while not q.empty():

        current = q.get()
        dist += 1

        print("Current url " + current)

        # Compares if the new distance is better than previous distance
        if dist >= distance:
            return curr_path

        # neighbour is any page that the current page links to
        for neighbour in get_links.get_links(current, link_exp):

            # If the path is found to the destination
            if neighbour == end_url:
                previous_page[neighbour] = current
                path = path_traceback(previous_page, neighbour)
                add_path_to_mapping(path, shortest_mapping)
                return path

            # if a path to a neighbour is found and is better than previous one (i.e. a shortcut)
            elif neighbour in shortest_mapping:
                previous_page[neighbour] = current
                print("Found shortcut for " + neighbour + " to end")
                path = path_traceback(previous_page, neighbour)
                ending = path_traceback(shortest_mapping, neighbour)
                ending.reverse()
                ending.remove(neighbour)
                curr_path = path + ending
                distance = len(curr_path) - 1

            else:
                if neighbour not in previous_page:
                    previous_page[neighbour] = current
                    q.put(neighbour)

    return curr_path


def path_traceback(previous_page, end):
  
    # previous_page is the mapping of a page with it's previous page in bfs
    # end is the url to start tracing back from

    path = [end]
    current = end

    # Trace path back to the source
    while previous_page[current] is not None:
        path.insert(0, previous_page[current])
        current = previous_page[current]

    return path # a list with first entry as the source and last as the end


def add_path_to_mapping(path, shortest_mapping):
    #Add the path to global mappings 
    #path is the path to add
    #shortest_mapping is the mapping to add to
    for idx in range(len(path) - 1):
        shortest_mapping[path[idx]] = path[idx + 1]