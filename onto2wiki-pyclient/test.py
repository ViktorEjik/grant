import parser
import pprint
from Onto2WikiClient import Onto2WikiClient, find_roots

pages = parser.parser_ttl('./psixolog.ttl')
pprint.pprint(pages)

roots = find_roots(pages)
print('roots = ', find_roots(pages))

# client = Onto2WikiClient()
# text = ''
# for root in roots:
#     me = root
#     visited = ['']
#     i = 1
#     text = client.get_hierarchy_page(pages, me, visited, i)
# print(text)
# client = Onto2WikiClient()
# client(pages, 'Заглавная_страница')
# # for page in pages.values():
# #     client.add_new_page(page)
# client.add_hierarchy_page(list(roots)[0]+" иерархия тем", pages, roots)

