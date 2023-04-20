# Python Engineer role at SteelEye
# Download the xml from this link
# From the xml, please parse through to the first download link whose file_type is DLTINS and download the zip
# Extract the xml from the zip.
# Convert the contents of the xml into a CSV with the following header:
# FinInstrmGnlAttrbts.Id
# FinInstrmGnlAttrbts.FullNm
# FinInstrmGnlAttrbts.ClssfctnTp
# FinInstrmGnlAttrbts.CmmdtyDerivInd
# FinInstrmGnlAttrbts.NtnlCcy
# Issr

# In this file only extracting "FinInstrmGnlAttrbts.Id"
# do it by yourself for other fields this just help you to understand how to extract data from xml

# Sample XML in the file
# <FinInstrmGnlAttrbts><Id>DE000A2AAJ76</Id><FullNm>Niedersachsen, Land           Landessch.v.16(21) Ausg.858</FullNm><ShrtNm>NIEDERSACHSEN/0.1 LSA 20210120</ShrtNm><ClssfctnTp>DNFTFB</ClssfctnTp><NtnlCcy>EUR</NtnlCcy><CmmdtyDerivInd>false</CmmdtyDerivInd></FinInstrmGnlAttrbts><Issr>391200ITQQZ7JMHXK080</Issr>


import csv
import xml.etree.ElementTree as ET

# Create a list of all FinInstrmGnlAttrbts elements
with open('output.csv', 'w', newline='') as csvfile:

    writer = csv.writer(csvfile)
    writer.writerow(['FinInstrmGnlAttrbts.Id'])

    # Parse the XML file and find all FinInstrmGnlAttrbts elements
    tree = ET.parse('DLTINS_20210117_01of01.xml')
    root = tree.getroot()
    namespaces = {'a': 'urn:iso:std:iso:20022:tech:xsd:auth.036.001.02'}
    elems = root.findall('.//a:FinInstrmGnlAttrbts', namespaces)

    # Loop over the FinInstrmGnlAttrbts elements and write the values to the CSV file
    count = 0
    for elem in elems:
        id_elem = elem.find('a:Id', namespaces)

        # Get the value of the Id element
        if id_elem is not None and id_elem.text:
            id = id_elem.text.strip()

        # Write the values to the CSV file
        writer.writerow([id])
        count += 1

    print("Wrote " + str(count) + " rows to output.csv")
    print("https://github.com/sauravhathi")