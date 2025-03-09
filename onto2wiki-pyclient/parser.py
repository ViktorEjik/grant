import re
import pprint

def parser_ttl(path):
    parent_children = dict()
    classes = dict()
    with open(path, 'r') as f:
        while line := f.readline():
            pars = re.search(r'(\S+) rdf:type (\S+) ;', line)
            if pars:
                if pars.group(2) != 'owl:Class': raise Exception('Unknown syntaxes')
                # if pars.group(1).startswith(':'):
                #     page = {'title': pars.group(1)[1:]}
                #     while new_line := f.readline().strip():
                #         pars_parent = re.search(r'rdfs:subClassOf :(\S+)', new_line[:-2])
                #         if pars_parent:
                #             pars_parent = pars_parent.group(1).split('#')
                #             if len(pars_parent) == 2:
                #                 pars_parent = pars_parent[1][:-1]
                #             else:
                #                 pars_parent = pars_parent[0]
                #
                #             if pars_parent not in parent_children:
                #                 parent_children[pars_parent] = [pars.group(1)[1:],]
                #             else:
                #                 parent_children[pars_parent].append(pars.group(1)[1:])
                #         pars_label = re.search(r'rdfs:label "(.+)"@(\S+)', new_line[:-1])
                #         if pars_label:
                #             page.update({f'label@{pars_label.group(2)}': pars_label.group(1)})
                #         if new_line[-1] == '.': break
                #     classes[pars.group(1)[1:]] = page
                # else:
                pars = pars.group(1).split('#')[1][:-1]
                page = {'title': pars}
                while new_line := f.readline().strip():
                    pars_parent = re.search(r'rdfs:subClassOf (\S+)', new_line[:-1])
                    if pars_parent:
                        pars_parent = pars_parent.group(1).split('#')
                        # print(pars_parent)
                        if len(pars_parent) == 2:
                            pars_parent = pars_parent[1][:-1]
                        else:
                            pars_parent = pars_parent[0]

                        page.update({'parent': pars_parent})
                        if pars_parent not in parent_children:
                            parent_children[pars_parent] = [pars,]
                        else:
                            parent_children[pars_parent].append(pars)
                    pars_label = re.search(r'rdfs:label "(.+)"@(\S+)', new_line[:-1])
                    if pars_label:
                        page.update({f'label@{pars_label.group(2)}': pars_label.group(1)})
                    if new_line[-1] == '.': break
                classes[pars] = page
    for parent, children in parent_children.items():
        classes[parent].update({'children': children})
    return classes
