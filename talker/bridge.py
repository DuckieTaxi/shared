import roslib
import rospy
from std_msgs.msg import String


def car_handler(data):
    global graph_pub
    rospy.loginfo("from car: ", data.data)
    graph_pub.publish(data)


def graph_handler(data):
    global car_pub
    rospy.loginfo("from graph: ", data.data)
    car_pub.publish(data)


def run():
    global graph_pub, car_pub
    rospy.init_node('comms')
    graph_pub = rospy.Publisher('graph_out', String)
    rospy.Subscriber('graph_in', String, graph_handler)
    car_pub = rospy.Publisher('car_out', String)
    rospy.Subscriber('car_in', String, car_handler)
    rospy.spin()


if __name__=='__main__':
    run()