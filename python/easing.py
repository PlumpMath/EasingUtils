import math

 
class LinearEase():

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration):
		return (end_val-start_val)*(curr_time/duration) + start_val


class SinEase():

	@staticmethod
	def ease_in(curr_time, start_val, end_val, duration):
		return -(end_val - start_val) * math.cos(curr_time/duration * (math.pi/2.0)) + (end_val - start_val) + start_val

	@staticmethod
	def ease_out(curr_time, start_val, end_val, duration):
		 return (end_val - start_val) * math.sin(curr_time/duration * (math.pi/2.0)) + start_val

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration):
		return -(end_val-start_val) * .5 * (math.cos(math.pi*(curr_time/duration)) - 1.0) + start_val


class QuadEase():

	@staticmethod
	def ease_in(curr_time, start_val, end_val, duration):
		curr_time /= duration;
		return (end_val - start_val)* curr_time*curr_time + start_val

	@staticmethod
	def ease_out(curr_time, start_val, end_val, duration):
		curr_time /= duration;
		return -(end_val - start_val) * curr_time*(curr_time-2.0) + start_val

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration):
		curr_time /= (duration * .5)
		if curr_time < 1:
			return (end_val-start_val) * .5 * curr_time * curr_time + start_val
		curr_time -= 1.0
		return -(end_val-start_val) * .5 * (curr_time * (curr_time - 2.0) - 1.0) + start_val


class CubicEase():

	@staticmethod
	def ease_in(curr_time, start_val, end_val, duration):
		curr_time /= duration
		return (end_val - start_val)*curr_time*curr_time*curr_time + start_val

	@staticmethod
	def ease_out(curr_time, start_val, end_val, duration):
		curr_time /= duration
		curr_time -= 1.0
		return (end_val - start_val)*(curr_time*curr_time*curr_time + 1) + start_val

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration):
		curr_time /= (duration*.5)
		if curr_time < 1.0:
			return (end_val - start_val)*.5*curr_time*curr_time*curr_time + start_val
		curr_time -= 2.0
		return (end_val - start_val)*.5*(curr_time*curr_time*curr_time + 2.0) + start_val


class QuarticEase():

	@staticmethod
	def ease_in(curr_time, start_val, end_val, duration):
		curr_time /= duration
		return (end_val - start_val)*curr_time*curr_time*curr_time*curr_time + start_val

	@staticmethod
	def ease_out(curr_time, start_val, end_val, duration):
		curr_time /= duration
		curr_time -= 1.0
		return -(end_val - start_val) * (curr_time*curr_time*curr_time*curr_time - 1.0) + start_val

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration):
		curr_time /= duration*.5;
		if curr_time < 1.0:
			return (end_val - start_val)*.5*curr_time*curr_time*curr_time*curr_time + start_val
		curr_time -= 2.0
		return -(end_val - start_val)*.5 * (curr_time*curr_time*curr_time*curr_time - 2.0) + start_val


class QuinticEase():

	@staticmethod
	def ease_in(curr_time, start_val, end_val, duration):
		curr_time /= duration
		return (end_val - start_val)*curr_time*curr_time*curr_time*curr_time*curr_time + start_val

	@staticmethod
	def ease_out(curr_time, start_val, end_val, duration):
		curr_time /= duration
		curr_time -= 1.0
		return (end_val - start_val)*(curr_time*curr_time*curr_time*curr_time*curr_time + 1.0) + start_val

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration):
		curr_time /= duration*.5
		if (curr_time < 1.0):
			return (end_val - start_val)*.5*curr_time*curr_time*curr_time*curr_time*curr_time + start_val
		curr_time -= 2.0
		return (end_val - start_val)*.5*(curr_time*curr_time*curr_time*curr_time*curr_time + 2.0) + start_val


class ExpEase():

	@staticmethod
	def ease_in(curr_time, start_val, end_val, duration):
		return (end_val - start_val) * math.pow( 2, 10.0 * (curr_time/duration - 1.0) ) + start_val

	@staticmethod
	def ease_out(curr_time, start_val, end_val, duration):
		return (end_val - start_val) * ( -math.pow( 2, -10.0 * curr_time/duration ) + 1.0 ) + start_val

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration):
		curr_time /= duration*.5
		if (curr_time < 1.0):
			return (end_val - start_val)/2 *  math.pow( 2, 10 * (curr_time - 1.0) ) + start_val
		curr_time -= 1.0
		return (end_val - start_val)*.5 * ( -math.pow( 2, -10.0 * curr_time) + 2 ) + start_val


class CircularEase():

	@staticmethod
	def ease_in(curr_time, start_val, end_val, duration):
		pass

	@staticmethod
	def ease_out(curr_time, start_val, end_val, duration):
		pass

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration):
		pass


class ElasticEase():

	@staticmethod
	def ease_in(curr_time, start_val, end_val, duration):
		pass

	@staticmethod
	def ease_out(curr_time, start_val, end_val, duration):
		pass

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration):
		pass


class BackEase():

	@staticmethod
	def ease_in(curr_time, start_val, end_val, duration):
		pass

	@staticmethod
	def ease_out(curr_time, start_val, end_val, duration):
		pass

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration):
		pass