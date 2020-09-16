#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from graphs import AlgoritmsWithGraphs


def callback(data):
    start, end = data.data.split()
    al = AlgoritmsWithGraphs()
    pub_1 = rospy.Publisher('graph_in', String, queue_size=10)
    rate = rospy.Rate(10)  # 10hz
    pub_1.publish(al.algoritm_deikstra(start, end))


def listener():
    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('graph', anonymous=True)

    rospy.Subscriber('graph_out', String, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    listener()