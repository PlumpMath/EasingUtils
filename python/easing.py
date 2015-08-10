import math

 
class LinearEase():

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration):
		return (end_val-start_val)*(curr_time/duration) + start_val


class SinEase():

	@staticmethod
	def ease_in(curr_time, start_val, end_val, duration):
		change = end_val - start_val
		return -change * math.cos(curr_time/duration * (math.pi*.5)) + change + start_val

	@staticmethod
	def ease_out(curr_time, start_val, end_val, duration):
		change = end_val - start_val
		return change * math.sin(curr_time/duration * (math.pi*.5)) + start_val

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration):
		change = end_val - start_val
		return -change * .5 * (math.cos(math.pi*(curr_time/duration)) - 1.0) + start_val


class QuadEase():

	@staticmethod
	def ease_in(curr_time, start_val, end_val, duration):
		change = end_val - start_val
		curr_time /= duration;
		return change * curr_time**2 + start_val

	@staticmethod
	def ease_out(curr_time, start_val, end_val, duration):
		change = end_val - start_val
		curr_time /= duration;
		return -change * curr_time * (curr_time - 2.0) + start_val

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration):
		curr_time /= (duration * .5)
		change = end_val - start_val
		if curr_time < 1:
			return change * .5 * curr_time**2 + start_val
		curr_time -= 1.0
		return -change * .5 * (curr_time * (curr_time - 2.0) - 1.0) + start_val


class CubicEase():

	@staticmethod
	def ease_in(curr_time, start_val, end_val, duration):
		change = end_val - start_val
		curr_time /= duration
		return change * curr_time**3 + start_val

	@staticmethod
	def ease_out(curr_time, start_val, end_val, duration):
		change = end_val - start_val
		curr_time /= duration
		curr_time -= 1.0
		return change * (curr_time**3 + 1) + start_val

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration):
		change = end_val - start_val
		curr_time /= duration*.5
		if curr_time < 1.0:
			return change * .5 * curr_time**3 + start_val
		curr_time -= 2.0
		return change * .5 * (curr_time**3 + 2.0) + start_val


class QuarticEase():

	@staticmethod
	def ease_in(curr_time, start_val, end_val, duration):
		change = end_val - start_val
		curr_time /= duration
		return change * curr_time**4 + start_val

	@staticmethod
	def ease_out(curr_time, start_val, end_val, duration):
		change = end_val - start_val
		curr_time /= duration
		curr_time -= 1.0
		return -change * (curr_time**4 - 1.0) + start_val

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration):
		change = end_val - start_val
		curr_time /= duration * .5
		if curr_time < 1.0:
			return change * .5 * curr_time**4 + start_val
		curr_time -= 2.0
		return -change * .5 * (curr_time**4 - 2.0) + start_val


class QuinticEase():

	@staticmethod
	def ease_in(curr_time, start_val, end_val, duration):
		curr_time /= duration
		return (end_val - start_val) * curr_time**5 + start_val

	@staticmethod
	def ease_out(curr_time, start_val, end_val, duration):
		curr_time /= duration
		curr_time -= 1.0
		return (end_val - start_val) * (curr_time**5 + 1.0) + start_val

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration):
		change = end_val - start_val
		curr_time /= duration * .5
		if (curr_time < 1.0):
			return change * .5 * curr_time**5 + start_val
		curr_time -= 2.0
		return change* .5 * (curr_time**5 + 2.0) + start_val


class ExpEase():

	@staticmethod
	def ease_in(curr_time, start_val, end_val, duration):
		return (end_val - start_val) * math.pow(2, 
			10.0 * (curr_time/duration - 1.0) ) + start_val

	@staticmethod
	def ease_out(curr_time, start_val, end_val, duration):
		return (end_val - start_val) * ( -math.pow(2,
			-10.0 * curr_time/duration ) + 1.0 ) + start_val

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration):
		change = end_val - start_val
		curr_time /= duration * .5
		if curr_time < 1.0:
			return change * .5 *  math.pow(2, 10 * (curr_time - 1.0) ) + start_val
		curr_time -= 1.0
		return change * .5 * ( -math.pow(2, -10.0 * curr_time) + 2.0 ) + start_val


class CircularEase():

	@staticmethod
	def ease_in(curr_time, start_val, end_val, duration):
		curr_time /= duration
		return -(end_val - start_val) * (math.sqrt(1 - curr_time**2) - 1) + start_val

	@staticmethod
	def ease_out(curr_time, start_val, end_val, duration):
		curr_time /= duration
		curr_time -= 1.0;
		return (end_val - start_val) * math.sqrt(1 - curr_time**2) + start_val

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration):
		change = end_val - start_val
		curr_time /= duration * .5
		if curr_time < 1:
			return -change * .5 * (math.sqrt(1 - curr_time**2) - 1.0) + start_val
		curr_time -= 2.0
		return change * .5 * (math.sqrt(1 - curr_time**2) + 1.0) + start_val


class ElasticEase():

	@staticmethod
	def ease_in(curr_time, start_val, end_val, duration, k=.3):
		if curr_time == 0: 
			return start_val
		curr_time/=duration
		if curr_time == 1.0:
			return end_val
		p = duration* k
		change = end_val - start_val
		s = p/4.0
		curr_time-=1
		postFix = change * math.pow(2, 10 * curr_time)
		return -(postFix * math.sin((curr_time * duration - s) * (2 * math.pi)/p)) + start_val

	@staticmethod
	def ease_out(curr_time, start_val, end_val, duration, k=.3, b=2):
		change = end_val-start_val
	 	curr_time /= duration
	 	if curr_time == 1:
	 		return end_val
	 	p = duration * k
	 	s = p/4.0
	 	return change * math.pow(b, -10.0 * curr_time) * \
	 		math.sin((curr_time * duration - s)\
	 			* (2.0 * math.pi)/p) + change + start_val


	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration, k=.3):
		if curr_time==0: 
			return start_val
		curr_time /= duration/2.0
		if curr_time == 2.0:
			return end_val
		p = duration * k * 1.5
		change = (end_val - start_val)
		s = p/4.0
		if curr_time < 1:
			curr_time-=1
			postFix = change*math.pow(2, 10*(curr_time))
			return -.5*(postFix * math.sin((curr_time*duration-s)*(2.0 * math.pi)/p )) + start_val 
		curr_time-=1
		postFix = change * math.pow(2, -10*(curr_time))
		return postFix * math.sin((curr_time*duration-s)*(2.0 * math.pi)/p)*.5  + change + start_val



class BackEase():

	@staticmethod
	def ease_in(curr_time, start_val, end_val, duration, back_dist=1.7):
		postFix = curr_time/duration
		return (end_val - start_val)*postFix*curr_time*((back_dist+1)*curr_time - back_dist) + start_val

	@staticmethod
	def ease_out(curr_time, start_val, end_val, duration, back_dist=1.7):
		curr_time=curr_time/duration-1
		return (end_val - start_val)*(curr_time*curr_time*((back_dist+1)*curr_time + back_dist) + 1) + start_val;

	@staticmethod
	def ease_in_out(curr_time, start_val, end_val, duration, back_dist=1.7):
		back_dist*=1.525
		curr_time/=duration*.5
		if curr_time < 1:
			return (end_val - start_val)*.5*(curr_time*curr_time*((back_dist+1)*curr_time - back_dist)) + start_val
		curr_time -= 2.0
		return (end_val - start_val)*.5*(curr_time*curr_time*((back_dist+1.0)*curr_time + back_dist) + 2.0) + start_val + start_val