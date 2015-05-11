import math

 
class LinearEase():

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration):
		return (end_val-start_val)*(curr_time/duration) + start_val


class SinEase():

	@staticmethod
	def ease_in(curr_time, start_val, end_val, duration):
		pass

	@staticmethod
	def ease_out(curr_time, start_val, end_val, duration):
		pass

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration):
		return -(end_val-start_val) * .5 * (math.cos(math.pi*(curr_time/duration)) - 1.0) + start_val


class QuadEase():

	@staticmethod
	def ease_in(curr_time, start_val, end_val, duration):
		pass

	@staticmethod
	def ease_out(curr_time, start_val, end_val, duration):
		pass

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration):
		curr_time /= (duration * .5)
		if curr_time < 1:
			return (end_val-start_val) * .5 * curr_time * curr_time + start_val
		curr_time -= 1
		return -(end_val-start_val) * .5 * (curr_time * (curr_time - 2.0) - 1.0) + start_val


class CubicEase():

	@staticmethod
	def ease_in(curr_time, start_val, end_val, duration):
		pass

	@staticmethod
	def ease_out(curr_time, start_val, end_val, duration):
		pass

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration):
		pass


class QuarticEase():

	@staticmethod
	def ease_in(curr_time, start_val, end_val, duration):
		pass

	@staticmethod
	def ease_out(curr_time, start_val, end_val, duration):
		pass

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration):
		pass


class QuinticEase():

	@staticmethod
	def ease_in(curr_time, start_val, end_val, duration):
		pass

	@staticmethod
	def ease_out(curr_time, start_val, end_val, duration):
		pass

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration):
		pass


class ExpEase():

	@staticmethod
	def ease_in(curr_time, start_val, end_val, duration):
		pass

	@staticmethod
	def ease_out(curr_time, start_val, end_val, duration):
		pass

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration):
		pass


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