from compare import CodeJudge


class PetriNet():

    def __init__(self):


    def add_place(self, name):


    def add_transition(self, name, id):


    def add_edge(self, source, target):


    def get_tokens(self, place):


    def is_enabled(self, transition):


    def add_marking(self, place):


    def fire_transition(self, transition):
# code here

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.

def check_correcness:
    judge = CodeJudge()
    p = PetriNet()

    p.add_place(1)  # add place with id 1
    p.add_place(2)
    p.add_place(3)
    p.add_place(4)
    p.add_transition("A", -1)  # add transition "A" with id -1
    p.add_transition("B", -2)
    p.add_transition("C", -3)
    p.add_transition("D", -4)

    p.add_edge(1, -1)
    p.add_edge(-1, 2)
    p.add_edge(2, -2).add_edge(-2, 3)
    p.add_edge(2, -3).add_edge(-3, 3)
    p.add_edge(3, -4)
    p.add_edge(-4, 4)

    print(p.is_enabled(-1), p.is_enabled(-2), p.is_enabled(-3), p.is_enabled(-4))

    p.add_marking(1)  # add one token to place id 1
    print(p.is_enabled(-1), p.is_enabled(-2), p.is_enabled(-3), p.is_enabled(-4))

    p.fire_transition(-1)  # fire transition A
    print(p.is_enabled(-1), p.is_enabled(-2), p.is_enabled(-3), p.is_enabled(-4))

    p.fire_transition(-3)  # fire transition C
    print(p.is_enabled(-1), p.is_enabled(-2), p.is_enabled(-3), p.is_enabled(-4))

    p.fire_transition(-4)  # fire transition D
    print(p.is_enabled(-1), p.is_enabled(-2), p.is_enabled(-3), p.is_enabled(-4))

    p.add_marking(2)  # add one token to place id 2
    print(p.is_enabled(-1), p.is_enabled(-2), p.is_enabled(-3), p.is_enabled(-4))

    p.fire_transition(-2)  # fire transition B
    print(p.is_enabled(-1), p.is_enabled(-2), p.is_enabled(-3), p.is_enabled(-4))

    p.fire_transition(-4)  # fire transition D
    print(p.is_enabled(-1), p.is_enabled(-2), p.is_enabled(-3), p.is_enabled(-4))

    # by the end of the execution there should be 2 tokens on the final place
    print(p.get_tokens(4))

    expexted = """"False False False False
True False False False
False True True False
False False False True
False False False False
False True True False
False False False True
False False False False
2"""

    if judge.is_equals(expexted):
        print("correct!")
    else:
        print("FAILED!")
        print(judge.get_res(), expexted)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    check_correcness()


