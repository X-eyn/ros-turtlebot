#!/usr/bin/python3
import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose

class CircularSpiralMotion:
    def __init__(self):
        rospy.init_node('robot_cleaner', anonymous=True)
        self.velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
        self.pose_subscriber = rospy.Subscriber('/turtle1/pose', Pose, self.pose_callback)
        self.rate = rospy.Rate(10)
        self.vel_msg = Twist()
        self.radius = 1.0

    def pose_callback(self, pose_msg):
        if round(pose_msg.y, 9) == 9:
            rospy.loginfo(f"Turtle has reached the set limit at x: {pose_msg.x}, y: {pose_msg.y}")
            self.vel_msg.linear.x = 0
            self.vel_msg.angular.z = 0
            self.velocity_publisher.publish(self.vel_msg)
            rospy.signal_shutdown("Spiral rotation done!!!")

    def move_circular_spiral(self):
        while not rospy.is_shutdown():
            self.vel_msg.linear.x = self.radius
            self.vel_msg.angular.z = 3.1416

            self.velocity_publisher.publish(self.vel_msg)
            self.rate.sleep()

            self.radius += 0.05

if __name__ == '__main__':
    try:
        circular_spiral = CircularSpiralMotion()
        circular_spiral.move_circular_spiral()
    except rospy.ROSInterruptException:
        pass
