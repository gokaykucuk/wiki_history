# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from xml.dom.pulldom import parse, START_ELEMENT
from xml.sax import make_parser
from xml.sax.handler import feature_external_ges


# %%
parser = make_parser()
parser.setFeature(feature_external_ges, True)
parsed_xml= parse('data.xml', parser=parser)

# %%
currentRevision = None
for event, node in parsed_xml:
    if (event == START_ELEMENT):
        if (node.tagName == "revision"):
            currentRevision = node
        if (node.tagName == "text"):
            print("NODE")
            print(currentRevision)
            print(node.nodeName)
            print(node.attributes)
            print(node.nodeValue)
            print("ENDNODE")

# %% [markdown]
# 

# %%


