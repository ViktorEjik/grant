import parser
import pprint
from Onto2WikiClient import Onto2WikiClient

def find_root(children_parent, me):
    if me in children_parent:
        return find_root(children_parent, children_parent[me])
    else:
        return me

pages, children_parent = parser.parser('./smolontonew.ttl')
pprint.pprint(pages['Астрономия'])
roots = set()
for child in children_parent:
    roots.add(find_root(children_parent, child))
print(roots)

# client = Onto2WikiClient()
# text = ''
# for root in roots:
#     me = root
#     visited = ['']
#     i = 1
#     text = client.get_hierarchy_page(pages, me, visited, i)
# print(text)
client = Onto2WikiClient()
client.login()
# for page in pages.values():
#     client.add_new_page(page)
client.add_hierarchy_page("Иерархия", pages, roots)

