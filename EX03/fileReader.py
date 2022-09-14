from datetime import datetime
import xml.etree.ElementTree as ET

def read_from_file(url):
    # open file
    opened = open(url)
    # read file
    contents = opened.read()
    # parse XML format
    root = ET.fromstring(contents)

    # dictionary to collect data
    log_dictionary = {}

    for i in range(5, len(root)):  # start at 5 to jump over extensions and interate over outside elements
        temp = []

        for j in range(1, len(root[i])):
            values = {}

            for child in root[i][j]:

                # map data to data types
                if child.attrib["key"] == "time:timestamp":
                    child.attrib["value"] = datetime.strptime(child.attrib["value"], '%Y-%m-%dT%H:%M:%S+01:00')
                if child.attrib["key"] == "cost":
                    child.attrib["value"] = int(child.attrib["value"])

                # put data in to dictionary
                values[child.attrib["key"]] = child.attrib["value"]

            temp.append(values)
        log_dictionary[root[i][0].attrib["value"]] = temp

    return log_dictionary
