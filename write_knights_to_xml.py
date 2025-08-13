import lxml.etree as et

FILE_PATH = "DATA/knights.txt"

root_element = et.Element("knights")
with open(FILE_PATH) as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()  # remove \n
        name, title, color, quest, comment = line.split(':')
        knight_element = et.SubElement(root_element, "knight", title=title)
        name_element = et.SubElement(knight_element, "name")
        name_element.text = name
        et.SubElement(knight_element, "color").text = color
        et.SubElement(knight_element, "quest").text = quest
        et.SubElement(knight_element, "comment").text = comment

raw_xml_string = et.tostring(root_element, pretty_print=True, xml_declaration=True)
xml_string = raw_xml_string.decode()
print(xml_string)

xml_doc = et.ElementTree(root_element)
xml_doc.write("knights.xml", pretty_print=True, xml_declaration=True)
