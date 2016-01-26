#The MIT License (MIT)

#Copyright (c) 2015 Michele Mantovan

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

from transition import *


class EasingMgr:
    """EasingMgr
    This class rapresent the connection between the algorithminc
    calculations and the Panda3D engine.
    It has the list of all Transition created.

    Basic usage:
        easingMgr = EasingMgr()
        a_transition = easingMgr.add_transition(...)
        easingMgr.start_transition(a_transition)
    """

    def __init__(self):
        self.__transitions = []

    def add_transition(self, nodepath, t_param, ease_types,
                       duration, values, cb_done):
        """Creates and returns a transition. In order to start it,
        you have to save the transition externally."""
        transition = self.__transition_factory(t_param)(nodepath,
                                                        t_param,
                                                        ease_types,
                                                        duration,
                                                        values,
                                                        cb_done)
        self.__transitions.append(transition)
        return transition

    def __transition_factory(self, t_param):
        if '1D' in t_param:
            return Transition1D
        elif '2D' in t_param:
            return Transition2D
        elif '3D' in t_param:
            return Transition3D

    def start_transition(self, transition):
        if transition in self.__transitions:
            if not transition.is_updating:
                taskMgr.add(transition.update, str(transition))

    def remove_transition(self, transition):
        if transition in self.__transitions:
            self.__transitions.remove(transition)
