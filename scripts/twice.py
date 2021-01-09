#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float32

n = 0

def  cb(message):
    global n
    n = message.data*2

    if n > 100:
        n =  message.data*3

    if n > 300:
        n = message.data/5


rospy.init_node('twice')
sub = rospy.Subscriber('count_up', Float32, cb)
pub = rospy.Publisher('twice', Float32, queue_size=1)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    pub.publish(n)
    rate.sleep()

