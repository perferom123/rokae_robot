
import rospy
from turtlesim.msg import Pose
from geometry_msgs.msg import Wrench
from geometry_msgs.msg import WrenchStamped




def poseCallback(msg):
    rospy.loginfo("force : x:%0.6f, y:%0.6f, z:%0.6f " , msg.wrench.force.x, msg.wrench.force.y, msg.wrench.force.z)
    print("force : x:%0.6f, y:%0.6f, z:%0.6f " , msg.wrench.force.x, msg.wrench.force.y,  msg.wrench.force.z)
 
def pose_subscriber():
	# ROS节点初始化
    rospy.init_node('pose_subscriber', anonymous=True)
 
	# 创建一个Subscriber，订阅名为/turtle1/pose的topic，注册回调函数poseCallback
    rospy.Subscriber("/wrench", WrenchStamped, poseCallback)
 
	# 循环等待回调函数
    rospy.spin()
 
if __name__ == '__main__':
    pose_subscriber()























# #!/usr/bin/env python
# import rospy

# from  geometry_msgs   import  *
# from std_msgs.msg import String

# from geometry_msgs.msg import Wrench

# from geometry_msgs.msg import WrenchStamped

# import geometry_msgs.msg



  
  
  
# def callback(data):
#     rospy.loginfo(rospy.get_caller_id() + "I heard %s", data.data)
#     fake_wrench =WrenchStamped
    
    
    
# def listener():

      
#     # msg_wrench = geometry_msgs.msg.Wrench()
#     # print('x_force={0}'.format(msg_wrench.force.x))
#     # print('y_force={0}'.format(msg_wrench.force.y))
#     # print('z_force={0}'.format(msg_wrench.force.z))

#     # msg_wrenchStamped = geometry_msgs.msg.WrenchStamped()
    
#     # force = geometry_msgs.msg.Vector3()
#     # torque = geometry_msgs.msg.Vector3()
    
    
#     # In ROS, nodes are uniquely named. If two nodes with the same
#     # name are launched, the previous one is kicked off. The
#     # anonymous=True flag means that rospy will choose a unique
#     # name for our 'listener' node so that multiple listeners can
#     # run simultaneously.
#     rospy.init_node('listener', anonymous=True)

#     rospy.Subscriber('geometry_msgs/WrenchStamped', geometry_msgs.msg.WrenchStamped() , callback)

#     # spin() simply keeps python from exiting until this node is stopped
#     rospy.spin()

# if __name__ == '__main__':
#     listener()
