#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-
import sys, random, copy
import rospy, tf, rospkg
from gazebo_msgs.srv import SpawnModel
from gazebo_msgs.msg import ModelStates
from geometry_msgs.msg import *
from std_msgs.msg import *

import moveit_commander
import moveit_msgs.msg
from moveit_commander.conversions import pose_to_list



if __name__ == "__main__":


    rospy.init_node("sort_robot_program")
    
    moveit_commander.roscpp_initialize(sys.argv)
    robot = moveit_commander.RobotCommander()

    group_name1 = "manipulator"
    group1 = moveit_commander.MoveGroupCommander(group_name1)
    group1.set_planner_id("RRTConnectkConfigDefault")

    display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',moveit_msgs.msg.DisplayTrajectory,queue_size=20)
    scene = moveit_commander.PlanningSceneInterface()
    rospy.sleep(2)
    group1.set_named_target("up")    #NO use home  for pose. will load collision
    plan1 = group1.plan()
    group1.execute(plan1,wait=True)

    rospy.sleep(2)


    
