from EX02.event import Event


def log_as_dictionary(log: str):
    dict = {}

    for line in log.splitlines():

        if len(line) == 0:
            continue

        parts = line.split(";")

        # print(parts)

        case_id = parts[1]
        task_name = parts[0]
        user_id = parts[2]
        time = parts[3]

        # init list if it is None
        if dict.get(case_id) is None:
            dict[case_id] = []

        event = Event(case_id=case_id, name=task_name, date=time, user_id=user_id)
        dict[case_id].append(event)

    return dict


def dependency_graph(log):
    dep_graph = {}

    # iterate cases
    for case in log:

        # iterate event list of case
        for i in range(len(log[case])-1):

            # create dic if not there
            if dep_graph.get(log[case][i].name) is None:
                dep_graph[log[case][i].name] = {log[case][i+1].name: 1}

            #
            else:

                if log[case][i+1].name not in dep_graph[log[case][i].name]:
                    inside_dic = dep_graph[log[case][i].name]
                    inside_dic[log[case][i+1].name] = 1
                else:
                    small_dic = dep_graph[log[case][i].name]
                    small_dic[log[case][i+1].name] += 1

    return dep_graph
