#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Point
from geometry_msgs.msg import Vector3
#from std_msgs.msg import UInt16


def callback(data):
    gimbal_msg = Vector3()
    #msg = UInt16()

    obj_loc_x = data.x
    obj_loc_y = data.y

    x = p_x.update(obj_loc_x)
    
    pwm_x = 0 if x < 0 else 180 if x > 180 else x

    gimbal_msg.x = pwm_x

    #msg.data = pwm_x

    pub.publish(gimbal_msg)

    #pub.publish(msg)

def main():
    global p_x
    global pwm_x
    global pub
 
    
    #maybe PID isn't necessary for servo control
    p_x = PID(10.0,5.0,1.0)
    p_x.setPoint(0.0)

    rospy.init_node('gimbal_control')
    
    pub = rospy.Publisher("gimbal_control", Vector3, queue_size=5)
    #pub = rospy.Publisher("gimbal_control", UInt16, queue_size=1)
    
    rospy.Subscriber("blob/point_blob", Point, callback)
    
    rospy.spin()


#######	Example	#########
#
#p=PID(3.0,0.4,1.2)
#p.setPoint(5.0)
#while True:
#     pid = p.update(measurement_value)
#
#
class PID:
	"""
	Discrete PID control
	"""

	def __init__(self, P=2.0, I=0.0, D=0.0, Derivator=0, Integrator=0, Integrator_max=30, Integrator_min=-30):

		self.Kp=P
		self.Ki=I
		self.Kd=D
		self.Derivator=Derivator
		self.Integrator=Integrator
		self.Integrator_max=Integrator_max
		self.Integrator_min=Integrator_min

		self.set_point=0.0
		self.error=0.0

	def update(self,current_value):
		"""
		Calculate PID output value for given reference input and feedback
		"""

		self.error = self.set_point - current_value

		self.P_value = self.Kp * self.error
		self.D_value = self.Kd * ( self.error - self.Derivator)
		self.Derivator = self.error

		self.Integrator = self.Integrator + self.error

		if self.Integrator > self.Integrator_max:
			self.Integrator = self.Integrator_max
		elif self.Integrator < self.Integrator_min:
			self.Integrator = self.Integrator_min

		self.I_value = self.Integrator * self.Ki

		PID = self.P_value + self.I_value + self.D_value

		return PID

	def setPoint(self,set_point):
		"""
		Initilize the setpoint of PID
		"""
		self.set_point = set_point
		self.Integrator=0
		self.Derivator=0

	def setIntegrator(self, Integrator):
		self.Integrator = Integrator

	def setDerivator(self, Derivator):
		self.Derivator = Derivator

	def setKp(self,P):
		self.Kp=P

	def setKi(self,I):
		self.Ki=I

	def setKd(self,D):
		self.Kd=D

	def getPoint(self):
		return self.set_point

	def getError(self):
		return self.error

	def getIntegrator(self):
		return self.Integrator

	def getDerivator(self):
		return self.Derivator


if __name__ == '__main__':
    main()


