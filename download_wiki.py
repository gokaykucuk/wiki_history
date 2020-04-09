import os

packs = list(map(lambda x: x+1, range(27)))

for current_pack in packs:
    os.system(f"wget -O  http://ftp.acc.umu.se/mirror/wikimedia.org/dumps/enwiki/20200401/enwiki-20200401-stub-meta-history{current_pack}.xml.gz")