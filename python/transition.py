from easing import *


class Transition:

    ease_params = ['position3D', 'position2D', 'scale1D', 'scale3D']
    ease_class = ['lin', 'sin', 'quad', 'cub', 'quar',
                 'quin', 'exp', 'circ', 'elas', 'back']
    easing_types = ['easeI', 'easeO', 'easeIO']

    __ids2Ease = {('lin', 'easeI'):   LinearEase.ease_in_out,
                  ('lin', 'easeO'):   LinearEase.ease_in_out,
                  ('lin', 'easeIO'):  LinearEase.ease_in_out,
                  ('sin', 'easeI'):   SinEase.ease_in,
                  ('sin', 'easeO'):   SinEase.ease_out,
                  ('sin', 'easeIO'):  SinEase.ease_in_out,
                  ('quad', 'easeI'):  QuadEase.ease_in,
                  ('quad', 'easeO'):  QuadEase.ease_out,
                  ('quad', 'easeIO'): QuadEase.ease_in_out,
                  ('cub', 'easeI'):   CubicEase.ease_in,
                  ('cub', 'easeO'):   CubicEase.ease_out,
                  ('cub', 'easeIO'):  CubicEase.ease_in_out,
                  ('quar', 'easeI'):  QuarticEase.ease_in,
                  ('quar', 'easeO'):  QuarticEase.ease_out,
                  ('quar', 'easeIO'): QuarticEase.ease_in_out,
                  ('quin', 'easeI'):  QuinticEase.ease_in,
                  ('quin', 'easeO'):  QuinticEase.ease_out,
                  ('quin', 'easeIO'): QuinticEase.ease_in_out,
                  ('exp', 'easeI'):   ExpEase.ease_in,
                  ('exp', 'easeO'):   ExpEase.ease_out,
                  ('exp', 'easeIO'):  ExpEase.ease_in_out,
                  ('circ', 'easeI'):  CircularEase.ease_in,
                  ('circ', 'easeO'):  CircularEase.ease_out,
                  ('circ', 'easeIO'): CircularEase.ease_in_out,
                  ('elas', 'easeI'):  ElasticEase.ease_in,
                  ('elas', 'easeO'):  ElasticEase.ease_out,
                  ('elas', 'easeIO'): ElasticEase.ease_in_out,
                  ('back', 'easeI'):  BackEase.ease_in,
                  ('back', 'easeO'):  BackEase.ease_out,
                  ('back', 'easeIO'): BackEase.ease_in_out
                  }

    def __init__(self, nodepath, t_param, ease_types, duration,
                 values, cb_done=None):
        if t_param in Transition.ease_params:
            self._nodepath = nodepath
            self._values = values
            self._curr_time = 0
            self._duration = duration
            self._updating = False
            self._easing_cbs = [self.__ids2Ease[(ease_type)] for ease_type in ease_types]
            self._panda_func = self._meth_factory(nodepath, t_param)
            self._cb_done = cb_done
            self._values
        else:
            raise Exception('Ease parameter not valid. Use one from: ' + str(Transition.ease_params))

    def update(self, task):
        raise NotImplementedError()

    @property
    def is_updating(self):
        return self._updating

    def _meth_factory(self, nodepath, t_param):
        if 'position' in t_param:
            t_obj = self._nodepath.setPos
        elif 'scale' in t_param:
            t_obj = self._nodepath.setScale
        else:
            return None
        return t_obj

    def _right_transition(self, dimension, t_param):
        if dimension == '1D'  and not dimension in t_param:
            raise Exception('Wrong transition type, use Transition1D.')
        elif dimension == '2D' and not dimension in t_param:
            raise Exception('Wrong transition type, use Transition2D.')
        elif dimension == '3D'  and not dimension in t_param:
            raise Exception('Wrong transition type, use Transition3D.')

    def _right_class(self, t_class):
        if t_class not in Transition.ease_class:
            raise Exception('Ease class not valid. Use one from: ' + str(Transition.ease_class))

    def _right_type(self, t_type):
        if t_type not in Transition.easing_types:
            raise Exception('Ease type not valid. Use one from: ' + str(Transition.easing_types))

    def _param_validation(self, dimension, values, ease_types, t_param):
        self._right_transition(dimension, t_param)

        # if len(values[0]) != len(ease_types):
        #     raise Exception('Value dimension different from easing types count.')
        
        # if dimension == '1D' and len(ease_types) != 1:
        #     raise Exception('Transition1D needs only one easing type. You gave ' + str(len(ease_types)))
        # elif dimension == '2D' and len(ease_types) != 2:
        #     raise Exception('Transition2D needs two easing types. You gave ' + str(len(ease_types)))
        # elif dimension == '3D' and len(ease_types) != 3:
        #     raise Exception('Transition1D needs three easing types. You gave ' + str(len(ease_types)))

        for ease_type in ease_types:
            self._right_class(ease_type[0])
            self._right_type(ease_type[1])


class Transition1D(Transition):

    def __init__(self, nodepath, t_param, ease_types=[('quad', 'easeIO')],
                 duration=1.0, values=[[0], [1]], cb_done=None):
        Transition.__init__(self, nodepath, t_param, ease_types,
                            duration, values, cb_done)
        self._param_validation('1D', values, ease_types, t_param)


    def update(self, task):
        if self._curr_time < self._duration:
            self._updating = True
            val = None
            val = self._easing_cbs[0](self._curr_time,
                                      self._values[0][0],
                                      self._values[1][0],
                                      self._duration)
            dt = globalClock.getDt()
            self._curr_time += dt
            self._panda_func(val)
            return task.cont

        self._curr_time = 0.0
        self._updating = False
        self._panda_func(self._values[1][0])
        self._values = self._values[::-1]
        if self._cb_done:
            self._cb_done()
        return task.done


class Transition2D(Transition):
    def __init__(self, nodepath, t_param, ease_types=[('quad', 'easeIO'),
                                                      ('quad', 'easeIO')],
                 duration=1.0, values=[(0, 0), (1, 1)], cb_done=None):
        Transition.__init__(self, nodepath, t_param, ease_types,
                            duration, values, cb_done)
        self._param_validation('2D', values, ease_types, t_param)

    def update(self, task):
        if self._curr_time < self._duration:
            self._updating = True
            vals = ()
            for i in range(len(self._easing_cbs)):
                val = self._easing_cbs[i](self._curr_time,
                                          self._values[0][i],
                                          self._values[1][i],
                                          self._duration)
                vals = tuple(list(vals) + [val])
            dt = globalClock.getDt()
            self._curr_time += dt
            self._panda_func(vals[0], vals[1])
            return task.cont
        self._curr_time = 0.0
        self._updating = False
        self._panda_func(self._values[1][0], self._values[1][1])
        self._values = self._values[::-1]
        if self._cb_done:
            self._cb_done()
        return task.done


class Transition3D(Transition):
    def __init__(self, nodepath, t_param, ease_types=[('quad', 'easeIO'),
                                                      ('quad', 'easeIO'),
                                                      ('quad', 'easeIO')],
                 duration=1.0, values=[(0, 0, 0), (1, 1, 1)], cb_done=None):
        Transition.__init__(self, nodepath, t_param, ease_types,
                            duration, values, cb_done)
        self._param_validation('3D', values, ease_types, t_param)

    def update(self, task):
        if self._curr_time < self._duration:
            self._updating = True
            vals = ()
            for i in range(len(self._easing_cbs)):
                val = self._easing_cbs[i](self._curr_time,
                                          self._values[0][i],
                                          self._values[1][i],
                                          self._duration)
                vals = tuple(list(vals) + [val])
            dt = globalClock.getDt()
            self._curr_time += dt
            self._panda_func(vals[0], vals[1], vals[2])
            return task.cont
        self._curr_time = 0.0
        self._updating = False
        self._panda_func(self._values[1][0],
                         self._values[1][1],
                         self._values[1][2])
        self._values = self._values[::-1]
        if self._cb_done:
            self._cb_done()
        return task.done
