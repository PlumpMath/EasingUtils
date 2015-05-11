from direct.showbase.ShowBase import ShowBase
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import *
from easing import *

class MyApp(ShowBase):

	id2Ease = {'lin': LinearEase}

	def __init__(self):
		print 'creo'
		ShowBase.__init__(self)
		bk_text = 'Linear'
		self.textObject = OnscreenText(text=bk_text,
								  pos=(1, 1), 
								  scale=0.07,
								  fg=(1, 0.8, 0.8,1),
								  align=TextNode.ACenter,
								  mayChange=1)
		self.curr_time = 0.0
		self.end_time = 1.0
		self.curr_ease = 'lin'
		self.accept('space-up', self.__change_ease)
		self.accept('enter-up', self.start_ease)

	def start_ease(self):
		taskMgr.add(self.ease_task, 'ease_task')

	def ease_task(self, task):
		if self.curr_time < self.end_time:
			dt = globalClock.getDt()
			val = self.id2Ease[self.curr_ease].ease_in_out(self.curr_time, 1.0, 0.0, self.end_time)
			print val
			self.curr_time += dt
			self.textObject.setPos(val, val)
			return task.cont

		return task.done

	def __change_ease(self):
		pass


app = MyApp()
app.run()