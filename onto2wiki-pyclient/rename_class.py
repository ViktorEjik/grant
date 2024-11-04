import re
import pprint
file = ''
old_new = dict()
with open('./smolonto.ttl', 'r') as f:
    while line := f.readline():
        file += line
        if line == ':instruments-for-solar-research rdf:type owl:Class ;\n':
            pass
        if line.startswith(':'):
            pars = re.search(r':(\S+) rdf:type (\S+) ;', line)
            if pars.group(2) != 'owl:Class': raise Exception('Unknown syntaxes')

            while new_line := f.readline():
                file += new_line
                pars_label = re.search(r'rdfs:label "(.+)"@(\S+)', new_line[:-3])
                if pars_label:
                    old_new[pars.group(1)] = '_'.join(pars_label.group(1).split())
                if new_line[-2] == '.': break
file_str = ''
pprint.pprint(old_new)
file = file.split('\n')
i = 0
while i < len(file):
    line: str = file[i] + '\n'

    if line.startswith(':'):
        pars = re.search(r':(\S+) rdf:type (\S+) ;', line)
        if pars.group(1) in old_new:
            file_str += line.replace(pars.group(1), old_new[pars.group(1)])
        new_line = file[i + 1] + '\n'
        pars_parent = re.search(r'rdfs:subClassOf :(\S+)', new_line[:-2])
        if pars_parent:
            if pars_parent.group(1) in old_new:
                new_line = new_line.replace(pars_parent.group(1), old_new[pars_parent.group(1)])
                file_str += ' ' * (len(old_new[pars.group(1)])+2) + new_line.lstrip()
                i += 1
        new_line = file[i + 1] + '\n'
        pars_label = re.search(r'rdfs:label "(.+)"@(\S+)', new_line[:-1])
        # print(new_line)
        if pars_label:
            file_str += ' ' * (len(old_new[pars.group(1)])+2) + new_line.lstrip()
            i += 1
    elif line.startswith('### '):
        pars = re.search(r'### .*#(\S+)', line)
        if pars:
            if pars.group(1) in old_new:
                file_str += line.replace(pars.group(1), old_new[pars.group(1)])
        else: file_str += line
    else: file_str += line
    i += 1
print(file_str)

with open('./smolontonew.ttl', 'a') as f:
    f.write(file_str)
