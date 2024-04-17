#Hi Guys, this isn´t working as it should right now but I´m working on it. If your´re going to run this, please remember to add your file paths to this. I´ve replaced mine with "C:\\PATH\\TO\\YOUR\\FILE\\merged.xml"

import xml.etree.ElementTree as ET
from datetime import datetime

ET.register_namespace('', "http://www.transxchange.org.uk/")

def merge_elements(parent, element):
    existing = parent.find(element.tag)
    if existing is not None:
        for child in element:
            merge_elements(existing, child)
    else:
        parent.append(element)

def merge_transxchange(files):
    current_datetime = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
    output_file = "C:\\PATH\\TO\\YOUR\\FILE\\merged.xml"
    root = ET.Element('TransXChange', {
        'xmlns:xsi': "http://www.w3.org/2001/XMLSchema-instance",
        'CreationDateTime': current_datetime,
        'FileName': output_file,
        'Modification': "new",
        'ModificationDateTime': current_datetime,
        'RegistrationDocument': "false",
        'RevisionNumber': "1",
        'SchemaVersion': "2.4",
        'xsi:schemaLocation': "http://www.transxchange.org.uk/ http://www.transxchange.org.uk/schema/2.4/TransXChange_general.xsd"
    })

    for file in files:
        tree = ET.parse(file)
        for element in tree.getroot():
            merge_elements(root, element)

    tree = ET.ElementTree(root)
    with open(output_file, 'wb') as f:
        f.write(b'<?xml version="1.0" encoding="UTF-8"?>\n')
        tree.write(f, encoding='utf-8')

files_to_merge = ["C:\\PATH\\TO\\YOUR\\FILE\\input_1.xml", "C:\\PATH\\TO\\YOUR\\FILE\\input_2.xml", "C:\\PATH\\TO\\YOUR\\FILE\\input_3.xml"]  #In theory, you can add as many files as you want to :)

merge_transxchange(files_to_merge)
