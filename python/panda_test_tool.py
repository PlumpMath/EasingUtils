from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import *
from easing import *

easeClass = ['lin', 'sin', 'quad', 'cub', 'quar', 'quin', 'exp', 'circ', 'elas']
easeType = ['easeI', 'easeO', 'easeIO']

class MyApp(ShowBase):

	ids2Ease = {('lin', 'easeI'): LinearEase.ease_in_out,
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
			   }

	def __init__(self):
		ShowBase.__init__(self)
		self.curr_ease = ['lin', 'easeI']
		self.class_lab = OnscreenText(text=self.curr_ease[0],
								  pos=(-1.2, .9), 
								  scale=0.07,
								  fg=(1, 0.8, 0.8, 1),
								  align=TextNode.ALeft,
								  mayChange=1)

		self.type_lab = OnscreenText(text=self.curr_ease[1],
								  pos=(-1.0, .9), 
								  scale=0.07,
								  fg=(1, 0.8, 0.8, 1),
								  align=TextNode.ALeft,
								  mayChange=1)

		self.positions = [(-.7, 0, 0), (.7, 0, 0)]

		self.myFrame = DirectFrame(frameColor=(0, 0, 1, 1),
                      		  	   frameSize=(-.3, .3, -.3, .3),
                      		       pos=self.positions[0])

		self.curr_time = 0.0
		self.end_time = 1.0
		self.accept('q-up', self.__change_class, extraArgs=[1])
		self.accept('a-up', self.__change_class, extraArgs=[-1])
		self.accept('w-up', self.__change_type, extraArgs=[1])
		self.accept('s-up', self.__change_type, extraArgs=[-1])

		self.accept('space-up', self.start_ease)

	def start_ease(self):
		self.ignore('space-up')
		taskMgr.add(self.ease_task, 'ease_task')

	def ease_task(self, task):
		if self.curr_time < self.end_time:
			dt = globalClock.getDt()
			val = self.ids2Ease[(self.curr_ease[0],
								 self.curr_ease[1])](self.curr_time,
													 self.positions[0][0],
													 self.positions[1][0],
													 self.end_time)
			self.curr_time += dt
			self.myFrame.setPos(val, 0, 0)
			return task.cont
		self.curr_time = 0.0
		self.end_time = 1.0
		self.myFrame.setPos(self.positions[1])
		self.positions = self.positions[::-1]
		self.accept('space-up', self.start_ease)
		return task.done

	def __change_class(self, incr):
		self.curr_ease[0] = easeClass[(easeClass.index(self.curr_ease[0]) + incr) % len(easeClass)]
		self.class_lab.setText(self.curr_ease[0]);

	def __change_type(self, incr):
		self.curr_ease[1] = easeType[(easeType.index(self.curr_ease[1]) + incr) % len(easeType)]
		self.type_lab.setText(self.curr_ease[1]);


app = MyApp()
app.run()