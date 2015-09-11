from easing import *


class EasingMgr:

    def __init__():
        self.__transitions = []

    def add_transition(self, nodepath,
                       t_class, t_types,
                       duration, values):
        transition = Transition.factory(nodepath,
                                        t_class,
                                        t_types,
                                        duration)
        self.__transitions.append(transition)
        return transition

    def start_transition(transition):
        if transition in self.__transitions:
            if not transition.is_updating:
                taskMgr.add(transition.update, str(transition))

    def remove_transition(transition):
        if transition in self.__transitions:
            self.__transitions.pop(transition)
