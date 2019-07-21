import xml.etree.ElementTree as ET
import re

xml_data = """<?xml version="1.0" encoding="UTF-8"?>\n<shelfDocument>\n  <!-- This file contains definitions of shelves, toolbars, and tools.\n I
t should not be hand-edited when it is being used by the application.\n Note, that two definitions of the same element are not allow
ed in\n a single file. -->\n\n  <tool name="$HDA_DEFAULT_TOOL" label="$HDA_LABEL" icon="$HDA_ICON">\n    <toolMenuContext name="view
er">\n      <contextNetType>SOP</contextNetType>\n    </toolMenuContext>\n    <toolMenuContext name="network">\n      <contextOpType
>$HDA_TABLE_AND_NAME</contextOpType>\n    </toolMenuContext>\n    <toolSubmenu>zTung/Cat01</toolSubmenu>\n    <toolSubmenu>zTung/Cat
02</toolSubmenu>\n    <toolSubmenu>zTung/Cat03</toolSubmenu>\n    <script scriptType="python"><![CDATA[import soptoolutils\n\nsoptoo
lutils.genericTool(kwargs, \'$HDA_NAME\')]]></script>\n  </tool>\n</shelfDocument>\n"""

pattern = '?<=\</toolMenuContext\>'

tree = ET.ElementTree(ET.fromstring(xml_data))
root = tree.getroot()
tool = root.getchildren()[0]
print(tool.getchildren())
# Remove current toolSubmenu
for e in tool.findall('toolSubmenu'):
    tool.remove(e)

toolsubmenu = ET.Element('toolSubmenu')
toolsubmenu.text = 'zTung/ThisIsNew'
tool.insert(-1, toolsubmenu)

toolsub2 = ET.Element('toolSubmenu')
toolsub2.text = 'zTung/ThisIsNew2'
tool.insert(-1, toolsub2)

print(tool.getchildren())
