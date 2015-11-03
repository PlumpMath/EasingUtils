# EasingUtils
Interpolation utility, written in Python for Panda3D.


###Content
* Python package easing_utils with all the modules of the utility.
* test application of the utility with some assets.


###Basic usage:
All the transition are handled in a standard way by the EasingMgr class. Feel free to use the Transition classes on your own.
```python
# Manager creation
easingMgr = EasingMgr()

# Transition creation, stored externally.
a_transition = easingMgr.add_transition(...)

# Transition start.
easingMgr.start_transition(a_transition)
```


###Future improvements
* Better usability for the Transition classes along with the EasingMgr class.
