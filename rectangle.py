#!/usr/bin/python3
import rospy
from geometry_msgs.msg import Twist

def move_rectangle(height, width):
    rospy.init_node('robot_cleaner', anonymous=True)
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    vel_msg = Twist()

    
    print("Moving the turtle in a rectangular path")
    speed = float(input("Input your speed:"))

    for _ in range(2):  
        # Move forward (height)
        vel_msg.linear.x = abs(speed)
        vel_msg.linear.y = 0
        vel_msg.linear.z = 0
        vel_msg.angular.x = 0
        vel_msg.angular.y = 0
        vel_msg.angular.z = 0

        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        while current_distance < height:
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_distance = speed * (t1 - t0) #s=d/t

        # Stop the robot
        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)

        rospy.sleep(1.0)

        # Turn 90 degrees to the left (counterclockwise)
        vel_msg.angular.z = abs(speed)
        t0 = rospy.Time.now().to_sec()
        current_angle = 0

        while current_angle < 1.5708:  # 1.5708 radians= 90 degrees
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_angle = speed * (t1 - t0)

        # Stop the robot
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)

        rospy.sleep(1.0)

        # Move forward (width)
        vel_msg.linear.x = abs(speed)
        t0 = rospy.Time.now().to_sec()
        current_distance = 0

        while current_distance < width:
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_distance = speed * (t1 - t0)

        # Stop the robot
        vel_msg.linear.x = 0
        velocity_publisher.publish(vel_msg)

        rospy.sleep(1.0)

        # Turn 90 degrees to the left (counterclockwise)
        vel_msg.angular.z = abs(speed)
        t0 = rospy.Time.now().to_sec()
        current_angle = 0

        while current_angle < 1.5708:  # 1.5708 radians= 90 degrees
            velocity_publisher.publish(vel_msg)
            t1 = rospy.Time.now().to_sec()
            current_angle = speed * (t1 - t0)

        # Stop the robot
        vel_msg.angular.z = 0
        velocity_publisher.publish(vel_msg)

        rospy.sleep(1.0)
        #bot has returned to og



    while current_distance < height:
        velocity_publisher.publish(vel_msg)
        t1 = rospy.Time.now().to_sec()
        current_distance = speed * (t1 - t0)

    # Stop the robot
    vel_msg.linear.x = 0
    velocity_publisher.publish(vel_msg)

    rospy.spin()

if __name__ == '__main__':
    try:
        
        height = float(input("Enter the height of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))

        
        move_rectangle(height, width)
    except rospy.ROSInterruptException:
        pass

