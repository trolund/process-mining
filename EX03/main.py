from EX03.event import Event
from EX03.fileReader import read_from_file


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


def unique_events(log):
    # initialize result list
    unique_list = []
    unique_name_list = []

    # iterate cases
    for case in log:
        for i in range(len(log[case]) - 1):
            event = log[case][i + 1]
            # print(event["concept:name"])
            # check if exists in unique_list or not, if not added it
            if event["concept:name"] not in unique_name_list:
                unique_name_list.append(event["concept:name"])
                unique_list.append(event)

    # print(unique_name_list)
    return unique_list




def alpha(log):
    all_events = unique_events(log)


if __name__ == '__main__':
    mined_model = alpha(read_from_file("data/extension-log.xes"))
