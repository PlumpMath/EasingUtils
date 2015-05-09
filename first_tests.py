
from direct.gui.OnscreenText import OnscreenText 
from direct.gui.DirectGui import *
from panda3d.core import *
import math
from direct.showbase.ShowBase import ShowBase
 

def lin_ease_none(curr_time, start_val, end_val, duration):
	return (end_val-start_val)*(curr_time/duration) + start_val

def sin_ease_in_out(curr_time, start_val, end_val, duration):
	return -(end_val-start_val) * .5 * (math.cos(math.pi*(curr_time/duration)) - 1.0) + start_val

def quad_ease_in_out(curr_time, start_val, end_val, duration):
	curr_time /= (duration * .5)
	if curr_time < 1:
		return (end_val-start_val) * .5 * curr_time * curr_time + start_val
	curr_time -= 1
	return -(end_val-start_val) * .5 * (curr_time * (curr_time - 2.0) - 1.0) + start_val

class MyApp(ShowBase):
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
		self.end_time = 5.5
		self.taskMgr.doMethodLater(2, self.spinCameraTask, "SpinCameraTask")

	def spinCameraTask(self, task):
		if self.curr_time < self.end_time:
			dt = globalClock.getDt()
			val = quad_ease_in_out(self.curr_time, 1.0, 0.0, self.end_time)
			print val
			self.curr_time += dt
			self.textObject.setPos(val, val)
			return task.cont

		return task.done

app = MyApp()
app.run()