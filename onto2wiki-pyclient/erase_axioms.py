import re

s = ''
with open("/home/viktor/dev/grant/tyrtelonto.ttl") as f:
    s = f.read()

match = re.search(r"\[ rdf:type owl:Axiom ;\n[^]]+ ] .", s)
while match:
    s = s.replace(match.group(0), '')
    match = re.search(r"\[ rdf:type owl:Axiom ;\n[^]]+ ] .", s)

with open('/home/viktor/dev/grant/tyrtelontonew.ttl', 'a', encoding='utf-8') as f:
     f.write(s)


print(s)