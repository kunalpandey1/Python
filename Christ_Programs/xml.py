import xml.etree.ElementTree as ET

# Example XML data
xml_data = '''
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
'''

# Parse the XML data
root = ET.fromstring(xml_data)

# Accessing elements and attributes
for country in root.findall('country'):
    name = country.get('name')
    rank = country.find('rank').text
    year = country.find('year').text
    gdppc = country.find('gdppc').text
    print(f'Country: {name}, Rank: {rank}, Year: {year}, GDP per capita: {gdppc}')

    for neighbor in country.findall('neighbor'):
        neighbor_name = neighbor.get('name')
        neighbor_direction = neighbor.get('direction')
        print(f'Neighbor: {neighbor_name}, Direction: {neighbor_direction}')
