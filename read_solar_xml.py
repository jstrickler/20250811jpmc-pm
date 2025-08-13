import lxml.etree as et

FILE_PATH = 'DATA/solar.xml'

xml_doc = et.parse(FILE_PATH)

# xml_doc = et.parsestring(STRING)

print(xml_doc)
root_element = xml_doc.getroot()
print(root_element, "\n")

for planet_element in xml_doc.findall(".//planet"):
    print(planet_element.get("planetname"))
    for moon_element in planet_element.findall('moon'):
        print(f"    {moon_element.text}")

