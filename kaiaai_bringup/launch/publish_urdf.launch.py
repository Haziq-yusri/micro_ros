#!/usr/bin/env python3
#
# Copyright 2023 REMAKE.AI
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os, re
from ament_index_python.packages import get_package_share_path
from launch import LaunchDescription, LaunchContext
from launch.actions import DeclareLaunchArgument, OpaqueFunction
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import Command, LaunchConfiguration
from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

def make_node(context: LaunchContext, robot_model):
    robot_model_str = context.perform_substitution(robot_model)

    description_package_path = get_package_share_path(robot_model_str)
    urdf_path_name = os.path.join(
        description_package_path,
        'urdf',
        robot_model_str + '.urdf.xacro')

    robot_description = ParameterValue(Command(['xacro ', urdf_path_name]), value_type=str)

    print("URDF file : {}".format(urdf_path_name))

    return [
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            parameters=[{'robot_description': robot_description}]
        ),
    ]


def generate_launch_description():
    default_robot_model_name = os.getenv('KAIAAI_ROBOT', default='makerspet_snoopy')

    return LaunchDescription([
        DeclareLaunchArgument(
            name='gui',
            # default_value='false',
            default_value='true',
            choices=['true', 'false'],
            description='Enable joint state publisher GUI'
        ),
        DeclareLaunchArgument(
            name='robot_model',
            default_value=default_robot_model_name,
            description='Robot description package name, overrides KAIAAI_ROBOT'
        ),
        OpaqueFunction(function=make_node, args=[
            LaunchConfiguration('robot_model'),
        ]),
        Node(
            package='joint_state_publisher',
            executable='joint_state_publisher',
            condition=UnlessCondition(LaunchConfiguration('gui'))
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            condition=IfCondition(LaunchConfiguration('gui'))
        )
    ])
