from event import Event
from fileReader import read_from_file
from petriNet import PetriNet

from enum import Enum
import numpy as np


class Relation(Enum):
    DIRECT = 1
    LEFT = 2  # CAUSAL
    RIGHT = 3  # CAUSAL
    PARALLEL = 4
    UNRELATED = 5


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
    unique_name_list = set()
    start_events = set()
    end_events = set()

    # iterate cases
    for case in log:
        for i in range(len(log[case])):
            event = log[case][i]

            # find start events
            if i == 0:
                start_events.add(event["concept:name"])

            # find end events
            if i == len(log[case]) - 1:
                end_events.add(event["concept:name"])

            unique_name_list.add(event["concept:name"])

    return list(unique_name_list), list(start_events), list(end_events)


def depth_relation_lookup(df, x, y):
    # independent to it self
    if x == y:
        return Relation.UNRELATED

    # parallel to it self
    if safe_lookup(df, x, y) > 0 and safe_lookup(df, y, x) > 0:
        return Relation.PARALLEL

    # causal relation
    if safe_lookup(df, x, y) > 0:
        return Relation.LEFT

    if safe_lookup(df, y, x) > 0:
        return Relation.RIGHT

    return Relation.UNRELATED


def safe_lookup(df, x, y):
    try:
        return df[x][y]
    except:
        return 0


# def posible_sets(log, df, all_events):
#     s = set()
#     for x in all_events:
#         for y in all_events:
#             relation = depth_relation_lookup(df, x, y)
#             if is_causal(relation):
#                 s.add(({x}, {y}))

def is_causal(relation):
    return relation == Relation.LEFT or relation == Relation.RIGHT


def create_task_sequence_set(log):
    # Create set of event/task sequences
    ts_set = set()
    for task in log:
        for i in range(0, len(task) - 1):
            ts_set.add((task[i], task[i + 1]))
    return ts_set


def map(relation: Relation):
    if relation == Relation.RIGHT:
        return "-->"
    elif relation == Relation.LEFT:
        return "<--"
    elif relation == Relation.UNRELATED:
        return " # "
    elif relation == Relation.PARALLEL:
        return " $ "
    elif relation == Relation.DIRECT:
        return " > "
    else:
        return "   "

def footprint(df, all_events):
    for x in all_events:
        for y in all_events:
            print(map(depth_relation_lookup(df, x, y)), end =" ")
        print()







def sets(df, all_events):
    a = set()
    b = set()

    for x in all_events:
        for y in all_events:

            if depth_relation_lookup(df, x, y) is Relation.RIGHT:
                if not is_unrelated(df, b, y):
                    b.add(y)
                elif not is_unrelated(df, a, x):
                    a.add(x)

    return a, b

def is_unrelated(df, s, x):
    
    if len(s) == 0:
        return False
    
    for y in s:
        if depth_relation_lookup(df, x, y) == Relation.UNRELATED:
            return False
       
    return True 

def alpha(log):
    # pre-processing
    df = dependency_graph(log)

    (all_events, start_events, end_events) = unique_events(log)

    (a, b) = sets(df, all_events)
    
    print("-------------> ", depth_relation_lookup(df, "intervention authorization", "intervention authorization"))

    for x in a:
        print(x)
        
    print("----------------")

    for y in b:
        print(y)

    footprint(df, all_events)

   # print(start_events)
   # print(end_events)
   # print(all_events)

    # print(sets)


    # create petri net
    p = PetriNet()

    p.add_place("start")
    p.add_place("end")

    # create transitions
    i = -1
    for trans in all_events:
        p.add_transition(trans, i)
        i = i - 1

    return p


def check_enabled(pn: PetriNet):
    ts = ["record issue", "inspection", "intervention authorization", "action not required", "work mandate",
          "no concession", "work completion", "issue completion"]
    for t in ts:
        print(pn.is_enabled(pn.transition_name_to_id(t)))
    print("")


if __name__ == '__main__':
    mined_model: PetriNet = alpha(read_from_file("data/extension-log.xes"))

    #trace = ["record issue", "inspection", "intervention authorization", "work mandate", "work completion",
    #         "issue completion"]
    #for a in trace:
    #    check_enabled(mined_model)
    #    mined_model.fire_transition(mined_model.transition_name_to_id(a))
