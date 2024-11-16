import parser
import pprint
from Onto2WikiClient import Onto2WikiClient, find_roots

pages = parser.parser_ttl('./fuc_new.ttl')
pprint.pprint(pages)

for page in pages:
    if 'parent' not in page:
        pprint.pprint(page)

roots = find_roots(pages)
print('roots = ', find_roots(pages), len(roots))

# client = Onto2WikiClient()
# text = ''
# for root in roots:
#     me = root
#     visited = ['']
#     i = 1
#     text = client.get_hierarchy_page(pages, me, visited, i)
# print(text)
client = Onto2WikiClient()
client('./fuc_new.ttl', 'Заглавная_страница')
# for page in pages.values():
#     client.dell_page(page)
# client.delete_hierarchy_page('. Иерархия тем', pages, roots)
# # for page in pages.values():
# #     client.add_new_page(page)
# client.add_hierarchy_page(list(roots)[0]+" иерархия тем", pages, roots)

