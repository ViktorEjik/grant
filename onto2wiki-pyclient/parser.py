import re
import pprint

def parser(path):
    parent_children = dict()
    children_parents = dict()
    classes = dict()
    with open(path, 'r') as f:
        while line := f.readline():

            if line.startswith(':'):
                pars = re.search(r':(\S+) rdf:type (\S+) ;', line)
                if pars.group(2) != 'owl:Class': raise Exception('Unknown syntaxes')
                page = {'title': pars.group(1)}
                while new_line := f.readline().strip():
                    pars_parent = re.search(r'rdfs:subClassOf :(\S+)', new_line[:-2])
                    if pars_parent:
                        page.update({'parent': pars_parent.group(1)})
                        if pars_parent.group(1) not in parent_children:
                            parent_children[pars_parent.group(1)] = [pars.group(1),]
                        else:
                            parent_children[pars_parent.group(1)].append(pars.group(1))
                        children_parents[pars.group(1)] = pars_parent.group(1)

                    pars_label = re.search(r'rdfs:label "(.+)"@(\S+)', new_line[:-2])
                    if pars_label:
                        page.update({f'label@{pars_label.group(2)}': pars_label.group(1)})
                        page.update({'title': '_'.join(pars_label.group(1).split())})
                    if new_line[-1] == '.': break
                classes[pars.group(1)] = page
    for parent, children in parent_children.items():
        classes[parent].update({'children': []})
        for child in children:
            classes[child]['parent'] = '_'.join(classes[parent]['title'].split())
            classes[parent]['children'].append('_'.join(classes[child]['title'].split()))
    # ans = []
    # print(parent_children['astronomy'])
    # for parent, children in parent_children.items():
    #     ans.append(classes[parent])
    #     for child in children:
    #         ans.append(classes[child])
    return classes, children_parents
