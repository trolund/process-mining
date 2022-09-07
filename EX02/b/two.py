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


def dependency_graph(log):
    dep_graph = {}

    # iterate cases
    for case in log:

        # iterate event list of case
        for i in range(len(log[case]) - 1):

            # create dic if not there and first task with the occurrence 1
            if dep_graph.get(log[case][i]["concept:name"]) is None:
                dep_graph[log[case][i]["concept:name"]] = {log[case][i + 1]["concept:name"]: 1}

            # now we know the dict is there! :)
            else:

                # get nested dict for the task
                nested_dic = dep_graph[log[case][i]["concept:name"]]

                # if the task name is not in the task's dict then add it with occurrence 1 else add +1 to it.
                if log[case][i + 1]["concept:name"] not in nested_dic:
                    nested_dic[log[case][i + 1]["concept:name"]] = 1
                else:
                    nested_dic[log[case][i + 1]["concept:name"]] += 1

    return dep_graph
