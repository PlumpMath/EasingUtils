from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import *
from direct.gui.OnscreenText import OnscreenText
from easing_utils.easing_mgr import EasingMgr
from easing_utils.easing import *
import sys


easeClass = ['lin', 'sin', 'quad', 'cub', 'quar',
             'quin', 'exp', 'circ', 'elas', 'back']
easeType = ['easeI', 'easeO', 'easeIO']
easeParam = ['position3D', 'position2D', 'scale1D', 'scale3D']
axis = ['1:', '2:', '3:']


class MyApp(ShowBase):
    """Test class for the all the uses cases for the EasingMgr class."""

    def __init__(self):
        ShowBase.__init__(self)

        base.disableMouse()
        base.setBackgroundColor(.2, .2, .2)

        camera.setPos(0, 0, 45)
        camera.setHpr(0, -90, 0)

        self.curr_ease = [(easeClass[8], easeType[1]),
                          (easeClass[8], easeType[1]),
                          (easeClass[8], easeType[1])]
        self.curr_param = easeParam[2]

        self._labs = []

        self.param_lab = OnscreenText(text=self.curr_param,
                                      pos=(-1.3, .9),
                                      scale=0.07,
                                      fg=(0.8, 0.8, 0.8, 1),
                                      align=TextNode.ALeft,
                                      mayChange=1)

        self.controls = OnscreenText(text='Controls: \n' +
          '   [p] Change paramter. \n' +
          '   [q, a, z] Change ease mode (x, y, z).\n' + 
          '   [w, s, x] Change ease type (x,y, z).\n' +
          '   [spacebar] Start the transition.\n' +
          '   [esc] Quit.',
                                     pos=(-1.3, -.7),
                                     scale=0.055,
                                     fg=(0.8, 0.8, 0.8, 1),
                                     align=TextNode.ALeft)

        for i in range(3):
            row = []
            row.append(OnscreenText(text=axis[i],
                                    pos=(-.9, .9 - (i*.1)),
                                    scale=0.07,
                                    fg=(0.8, 0.8, 0.8, 1),
                                    align=TextNode.ALeft,
                                    mayChange=1))
            row.append(OnscreenText(text=self.curr_ease[i][0],
                                    pos=(-.8, .9 - (i*.1)),
                                    scale=0.07,
                                    fg=(0.8, 0.8, 0.8, 1),
                                    align=TextNode.ALeft,
                                    mayChange=1))

            row.append(OnscreenText(text=self.curr_ease[i][1],
                                    pos=(-.6, .9 - (i*.1)),
                                    scale=0.07,
                                    fg=(0.8, 0.8, 0.8, 1),
                                    align=TextNode.ALeft,
                                    mayChange=1))
            self._labs.append(row)

        self._node = None

        self._ease_values = {'position3D': [(-8.0, -3.0, 10.0),
                                            (15.0, 3.0, -20.0)],
                             'position2D': [(-.7, -.3), (.7, .3)],
                             'scale1D': [[.08], [.20]],
                             'scale3D': [(1.0, 1.0, 1.0), (4.0, 4.0, 4.0)]}

        self.end_time = 1.0

        self.accept('escape', sys.exit, [0])
        self.input_setup(True)

        self.__easingMgr = EasingMgr()
        self.__curr_tr = None

        self.__change_param(0)

    def input_setup(self, activate):
        if activate:
            self.accept('q-up', self.__change_class, extraArgs=[0, 1])
            self.accept('a-up', self.__change_class, extraArgs=[1, 1])
            self.accept('z-up', self.__change_class, extraArgs=[2, 1])
            self.accept('w-up', self.__change_type, extraArgs=[0, 1])
            self.accept('s-up', self.__change_type, extraArgs=[1, 1])
            self.accept('x-up', self.__change_type, extraArgs=[2, 1])

            self.accept('p-up', self.__change_param, extraArgs=[1])
            self.accept('space-up', self.start_ease)
            self.accept('escape', sys.exit, [0])
        else:
            self.ignoreAll()

    def start_ease(self):
        self.input_setup(False)
        self.__easingMgr.start_transition(self.__curr_tr)

    def check_finished(self):
        if not self.__curr_tr.is_updating:
            self.input_setup(True)

    def __change_class(self, row, incr):
        self.curr_ease[row] = (easeClass[
            (easeClass.index(self.curr_ease[row][0]) + incr) % len(easeClass)],
            self.curr_ease[row][1])
        self._labs[row][1].setText(self.curr_ease[row][0])
        self.change_transition()

    def __change_type(self, row, incr):
        self.curr_ease[row] = (self.curr_ease[row][0], easeType[
            (easeType.index(self.curr_ease[row][1]) + incr) % len(easeType)])
        self._labs[row][2].setText(self.curr_ease[row][1])
        self.change_transition()

    def __change_param(self, incr):
        self.curr_param = easeParam[
            (easeParam.index(self.curr_param) + incr) % len(easeParam)]
        self.param_lab.setText(self.curr_param)
        self.release_nodes()
        if self.curr_param in ['position2D', 'scale1D']:
            self.load_text()
        if self.curr_param in ['position3D', 'scale3D']:
            self.load_sphere()
        if '1D' in self.curr_param:
            for i, row in enumerate(self._labs):
                if i < 1:
                    for lab in row:
                        lab.show()
                else:
                    for lab in row:
                        lab.hide()

        if '2D' in self.curr_param:
            for i, row in enumerate(self._labs):
                if i < 2:
                    for lab in row:
                        lab.show()
                else:
                    for lab in row:
                        lab.hide()
        if '3D' in self.curr_param:
            for i, row in enumerate(self._labs):
                for lab in row:
                    lab.show()
        self.change_transition()

    def change_transition(self):
        if self.__curr_tr:
            self.__easingMgr.remove_transition(self.__curr_tr)

        values = self._ease_values[self.curr_param]
        self.__curr_tr = self.__easingMgr.add_transition(self._node,
                                                         self.curr_param,
                                                         self.curr_ease,
                                                         self.end_time,
                                                         values,
                                                         self.check_finished)

    def load_text(self):
        self._node = OnscreenText(text='Fantastic text',
                                  pos=(self._ease_values['position2D'][0]),
                                  scale=self._ease_values['scale1D'][0][0])

    def load_sphere(self):
        self._node = loader.loadModel("planet_sphere")
        self._node.reparentTo(render)
        self._node.setScale(self._ease_values['scale3D'][0][0],
                            self._ease_values['scale3D'][0][1],
                            self._ease_values['scale3D'][0][2])
        self._node.setPos(self._ease_values['position3D'][0][0],
                          self._ease_values['position3D'][0][1],
                          self._ease_values['position3D'][0][2])
        self._node_tex = loader.loadTexture("earth.jpg")
        self._node.setTexture(self._node_tex, 1)

    def release_nodes(self):
        if self._node:
            self._node.removeNode()
            self._node = None

app = MyApp()
app.run()
