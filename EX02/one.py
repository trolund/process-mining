from EX02.event import Event


def log_as_dictionary(log: str):
    log_dictionary = {}

    # iterate over all input lines
    for line in log.splitlines():

        # if is an empty line just skip it
        if len(line) == 0:
            continue

        # split the line by ';'
        parts = line.split(";")

        # give the parts readable names
        case_id = parts[1]
        task_name = parts[0]
        user_id = parts[2]
        time = parts[3]

        # init list if it is None
        if log_dictionary.get(case_id) is None:
            log_dictionary[case_id] = []

        # put data into a event object
        event = Event(case_id=case_id, name=task_name, date=time, user_id=user_id)

        # append that object to resulting dictionary
        log_dictionary[case_id].append(event)

    return log_dictionary


def dependency_graph(log):
    dep_graph = {}

    # iterate cases
    for case in log:

        # iterate event list of case
        for i in range(len(log[case])-1):

            # create dic if not there and first task with the occurrence 1
            if dep_graph.get(log[case][i].name) is None:
                dep_graph[log[case][i].name] = {log[case][i+1].name: 1}

            # now we know the dict is there! :)
            else:

                # get nested dict for the task
                nested_dic = dep_graph[log[case][i].name]

                # if the task name is not in the task's dict then add it with occurrence 1 else add +1 to it.
                if log[case][i+1].name not in nested_dic:
                    nested_dic[log[case][i+1].name] = 1
                else:
                    nested_dic[log[case][i+1].name] += 1

    return dep_graph
