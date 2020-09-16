#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String
from barcode import *


def talker():
    pub = rospy.Publisher('car_in', String, queue_size=1)
    rospy.init_node('car', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        image = GetImage()
        result = BarcodeDetector(image)
        if result is not None:
            rospy.loginfo(result)
            pub.publish(result)
        rate.sleep()


if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass
