import os

from EX03.fileReader import read_from_file
from EX03.main import check_enabled
from EX03.petriNet import PetriNet


def getWorkFlow(log):
    workFlow = list()
    for events in log.values():
        trace = list()
        for c in range(len(events)):
            task = events[c]['concept:name']
            trace.append(task)
        if trace not in workFlow:
            workFlow.append(trace)
    return workFlow


def alpha(log):
    workFlow = getWorkFlow(log)
    uniqueItemsList = set()

    orderings = dict()

    for trace in workFlow:
        for activityNum in range(len(trace) - 1):
            if trace[activityNum] not in orderings.keys():
                orderings[trace[activityNum]] = list()
            if trace[activityNum + 1] not in orderings.keys():
                orderings[trace[activityNum + 1]] = list()
            if trace[activityNum + 1] not in orderings[trace[activityNum]]:
                orderings[trace[activityNum]].append(trace[activityNum + 1])

    print(orderings)

    for order in orderings:
        uniqueItemsList.add(order)
    
    petri = PetriNet()
    place = 1
    petri.add_place(place)
    # add all transitions
    for item in uniqueItemsList:
        petri.add_transition(item)
    
    # add edge from first place to first transition
    e = next(iter(uniqueItemsList))
    petri.add_edge(place, e)

    # add edge from : transition -> place -> transition[i]
    for transition in orderings:
        place += 1
        petri.add_place(place)
        petri.add_edge(transition, place)

        for nextItem in orderings[transition]:
            petri.add_edge(place, nextItem)

    return petri

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    mined_model = alpha(read_from_file(dir_path +"/data/extension-log.xes"))

    trace = ["record issue", "inspection", "intervention authorization", "work mandate", "work completion",
             "issue completion"]
    for a in trace:
        check_enabled(mined_model)
        mined_model.fire_transition(mined_model.transition_name_to_id(a))

