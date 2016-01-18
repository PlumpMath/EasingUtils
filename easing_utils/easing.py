import math

"""Easing Utilities

This module contains all interpolation classes divided by function of
interpolation.
Each class represents a different way or MODE to interpolate
between two values.
Every MODE has three different TYPE of interpolation (except for the
LinearEase) with the same method signature.
The TYPEs are ease-in, ease-out and ease-in-out.

Paramters:
    curr_time: the current time of the interpolation
    start_val: start value
    end_val: end value
    duration: duration in seconds of the animation

Usage:
    In order to use it you have to have a current time variabile that
    you have to increment every step and then pass it to the selected function.

"""


class LinearEase():
    """Linear interpolation mode. No actual ease."""

    @staticmethod
    def ease_in_out(curr_time, start_val, end_val, duration):
        return (end_val-start_val)*(curr_time/duration) + start_val


class SinEase():
    """Sinusoidal interpolation mode. Preety slow."""

    @staticmethod
    def ease_in(curr_time, start_val, end_val, duration):
        change = end_val - start_val
        return -change * math.cos(curr_time/duration * (math.pi*.5))\
            + change + start_val

    @staticmethod
    def ease_out(curr_time, start_val, end_val, duration):
        change = end_val - start_val
        return change * math.sin(curr_time/duration * (math.pi*.5)) + start_val

    @staticmethod
    def ease_in_out(curr_time, start_val, end_val, duration):
        change = end_val - start_val
        return -change * .5 * (math.cos(math.pi*(curr_time/duration)) - 1.0)\
            + start_val


class QuadEase():
    """Quartic interpolation mode. Very used, standard speed."""

    @staticmethod
    def ease_in(curr_time, start_val, end_val, duration):
        change = end_val - start_val
        curr_time /= duration
        return change * curr_time**2 + start_val

    @staticmethod
    def ease_out(curr_time, start_val, end_val, duration):
        change = end_val - start_val
        curr_time /= duration
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
    """Cubic interpolation mode. Standard speed but a little bumpy."""

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
    """Quartic interpolation mode. Standard speed but a little bumpy."""

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
    """Quintic interpolation mode. Fast and bumpy."""

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
        return change * .5 * (curr_time**5 + 2.0) + start_val


class ExpEase():
    """Quintic interpolation mode. Very fast and very bumpy."""

    @staticmethod
    def ease_in(curr_time, start_val, end_val, duration):
        return (end_val - start_val) * \
            math.pow(2, 10.0 * (curr_time/duration - 1.0)) + start_val

    @staticmethod
    def ease_out(curr_time, start_val, end_val, duration):
        return (end_val - start_val) * \
            (-math.pow(2, -10.0 * curr_time/duration) + 1.0) + start_val

    @staticmethod
    def ease_in_out(curr_time, start_val, end_val, duration):
        change = end_val - start_val
        curr_time /= duration * .5
        if curr_time < 1.0:
            return change * .5 * math.pow(2, 10 * (curr_time - 1.0))\
                + start_val
        curr_time -= 1.0
        return change * .5 * (-math.pow(2, -10.0 * curr_time) + 2.0)\
            + start_val


class CircularEase():
    """Quintic interpolation mode. Very fast and maybe to much bumpy."""

    @staticmethod
    def ease_in(curr_time, start_val, end_val, duration):
        curr_time /= duration
        return -(end_val - start_val) * (math.sqrt(1 - curr_time**2) - 1)\
            + start_val

    @staticmethod
    def ease_out(curr_time, start_val, end_val, duration):
        curr_time /= duration
        curr_time -= 1.0
        return (end_val - start_val) * math.sqrt(1 - curr_time**2) + start_val

    @staticmethod
    def ease_in_out(curr_time, start_val, end_val, duration):
        change = end_val - start_val
        curr_time /= duration * .5
        if curr_time < 1:
            return -change * .5 * (math.sqrt(1 - curr_time**2) - 1.0)\
                + start_val
        curr_time -= 2.0
        return change * .5 * (math.sqrt(1 - curr_time**2) + 1.0)\
            + start_val


class ElasticEase():
    """Elastic interpolation mode.
    The methods have arguments for the spring's elastic costant and speed.
    """
    @staticmethod
    def ease_in(curr_time, start_val, end_val, duration, k=.3, speed=4):
        if curr_time == 0:
            return start_val
        curr_time /= duration
        if curr_time == 1.0:
            return end_val
        p = duration * k
        change = end_val - start_val
        s = p/4.0
        curr_time -= 1
        postFix = change * math.pow(speed, 10 * curr_time)
        return -(postFix * math.sin(
            (curr_time * duration - s) * (2 * math.pi)/p)) + start_val

    @staticmethod
    def ease_out(curr_time, start_val, end_val, duration, k=.3, speed=4):
        change = end_val-start_val
        curr_time /= duration
        if curr_time == 1:
            return end_val
        p = duration * k
        s = p/4.0
        return change * math.pow(speed, -10.0 * curr_time)\
            * math.sin((curr_time * duration - s) * (2.0 * math.pi)/p)\
            + change + start_val

    @staticmethod
    def ease_in_out(curr_time, start_val, end_val, duration, k=.3, speed=4):
        if curr_time == 0:
            return start_val
        curr_time /= duration/2.0
        if curr_time == 2.0:
            return end_val
        p = duration * k * 1.5
        change = (end_val - start_val)
        s = p/4.0
        if curr_time < 1:
            curr_time -= 1
            postFix = change*math.pow(2, 10*(curr_time))
            return -.5 * \
                (postFix * math.sin((curr_time*duration-s)*(2.0 * math.pi)/p))\
                + start_val
        curr_time -= 1
        postFix = change * math.pow(speed, -10*(curr_time))
        return postFix * math.sin((curr_time*duration-s)*(2.0 * math.pi)/p)\
            * .5 + change + start_val


class BackEase():
    """Back interpolation mode.
    The methods have an argument for controlling the back distance.
    """

    @staticmethod
    def ease_in(curr_time, start_val, end_val, duration, back_dist=1.7):
        postFix = curr_time/duration
        return (end_val - start_val) * postFix*curr_time * \
            ((back_dist+1)*curr_time - back_dist) + start_val

    @staticmethod
    def ease_out(curr_time, start_val, end_val, duration, back_dist=1.7):
        curr_time = curr_time/duration-1
        return (end_val - start_val) * \
            (curr_time*curr_time*((back_dist+1)*curr_time + back_dist) + 1)\
            + start_val

    @staticmethod
    def ease_in_out(curr_time, start_val, end_val, duration, back_dist=1.7):
        back_dist *= 1.525
        curr_time /= duration*.5
        if curr_time < 1:
            return (end_val - start_val) * .5 * \
                (curr_time*curr_time*((back_dist+1.0)*curr_time - back_dist))\
                + start_val
        curr_time -= 2.0
        return (end_val - start_val) * .5 * \
            (curr_time*curr_time*((back_dist+1.0)*curr_time+back_dist) + 2.0)\
            + start_val

'''
 *
 * TERMS OF USE - EASING EQUATIONS
 *
 * Open source under the BSD License.
 *
 * Copyright © 2001 Robert Penner
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without modification,
 * are permitted provided that the following conditions are met:
 *
 * Redistributions of source code must retain the above copyright notice, this list of
 * conditions and the following disclaimer.
 * Redistributions in binary form must reproduce the above copyright notice, this list
 * of conditions and the following disclaimer in the documentation and/or other materials
 * provided with the distribution.
 *
 * Neither the name of the author nor the names of contributors may be used to endorse
 * or promote products derived from this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
 * EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
 * MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 *  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
 *  EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE
 *  GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED
 * AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
 *  NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
 * OF THE POSSIBILITY OF SUCH DAMAGE.
 *
'''
