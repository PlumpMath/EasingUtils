

class Transition:
    __ids2Ease = {('lin', 'easeI'): LinearEase.ease_in_out,
                  ('lin', 'easeO'): LinearEase.ease_in_out,
                  ('lin', 'easeIO'): LinearEase.ease_in_out,
                  ('sin', 'easeI'): SinEase.ease_in,
                  ('sin', 'easeO'): SinEase.ease_out,
                  ('sin', 'easeIO'): SinEase.ease_in_out,
                  ('quad', 'easeI'): QuadEase.ease_in,
                  ('quad', 'easeO'): QuadEase.ease_out,
                  ('quad', 'easeIO'): QuadEase.ease_in_out,
                  ('cub', 'easeI'): CubicEase.ease_in,
                  ('cub', 'easeO'): CubicEase.ease_out,
                  ('cub', 'easeIO'): CubicEase.ease_in_out,
                  ('quar', 'easeI'): QuarticEase.ease_in,
                  ('quar', 'easeO'): QuarticEase.ease_out,
                  ('quar', 'easeIO'): QuarticEase.ease_in_out,
                  ('quin', 'easeI'): QuinticEase.ease_in,
                  ('quin', 'easeO'): QuinticEase.ease_out,
                  ('quin', 'easeIO'): QuinticEase.ease_in_out,
                  ('exp', 'easeI'): ExpEase.ease_in,
                  ('exp', 'easeO'): ExpEase.ease_out,
                  ('exp', 'easeIO'): ExpEase.ease_in_out,
                  ('circ', 'easeI'): CircularEase.ease_in,
                  ('circ', 'easeO'): CircularEase.ease_out,
                  ('circ', 'easeIO'): CircularEase.ease_in_out,
                  ('elas', 'easeI'): ElasticEase.ease_in,
                  ('elas', 'easeO'): ElasticEase.ease_out,
                  ('elas', 'easeIO'): ElasticEase.ease_in_out,
                  ('back', 'easeI'): BackEase.ease_in,
                  ('back', 'easeO'): BackEase.ease_out,
                  ('back', 'easeIO'): BackEase.ease_in_out
                  }

    def __init__(self, nodepath, t_class, t_types, duration):
        self.nodepath = nodepath
        self.t_class = t_class
        self.t_types = t_types
        self.duration = duration
        self._curr_time = 0
        self._updating = False
        self._easing_cbs = [self.__ids2Ease[t_type] for t_type in t_types]

    def update():
        if self._curr_time < self.duration:
            self._updating = True
            dt = globalClock.getDt()
            vals = ()
            for i in range(2):
                for j in range(len(self._values[0])):
                    val = self._easing_cbs[i](self.curr_time,
                                              self.values[i][j],
                                              self.values[i][j],
                                              self.end_time)
                    vals = vals + (val)
                self.curr_time += dt
                if len(val) == 1:
                    self.nodepath.panda_param(vals[0])
                else:
                    self.nodepath.panda_param(vals)
                return task.cont
            self.curr_time = 0.0
            self.end_time = 1.0
            self.nodepath.panda_param(self.values[1])
            self.values = self.values[::-1]
            return task.done

    def is_updating(self):
        return self.__updating

    @staticmethod
    def factory(nodepath, t_param, t_class, t_types, duration):
        if t_param == 'position3D' and len(t_types) == 3:
            t_obj = Pos3DTran
        elif t_param == 'position2D' and len(t_types) == 2:
            t_obj = Pos2DTran
        elif t_param == 'scale' and len(t_types) == 1:
            t_obj = ScaleTran
        elif t_param == 'scale3D' and len(t_types) == 3:
            t_obj = Scale3DTran
        else:
            return None
        return t_obj(nodepath, t_class, t_types, duration)
