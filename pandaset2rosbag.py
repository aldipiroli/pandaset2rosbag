from pandaset import DataSet
import os
import rospy
import rosbag
from datetime import date, datetime, timedelta
from std_msgs.msg import Header
from sensor_msgs.msg import CameraInfo, Imu, PointField, NavSatFix
import sensor_msgs.point_cloud2 as pcl2
import numpy as np
import argparse
from pathlib import Path
import json
import pickle
import glob
import pandas as pd


def perdelta(start, end, delta):
    curr = start
    while curr < end:
        yield curr
        curr += delta


def main():
    # Select Scene:
    bag_ID = '024'

    # Create empty bag:
    bag_name = '/home/user/workspace/Datasets/Pandaset/RosBags/pandaset_' + \
        str(bag_ID) + '.bag'
    bag = rosbag.Bag(bag_name, 'w', compression=rosbag.Compression.NONE)

    # Set frames:
    velo_frame_id = 'pandar'
    velo_topic = '/mytopic/'

    # Load the sequences:
    dataset = DataSet('/home/user/workspace/Datasets/Pandaset/dataset/')
    sequences = dataset.sequences(with_semseg=True)
    sequences.sort()

    seqence = dataset[bag_ID]
    seqence.load_lidar().load_semseg()

    # Time hack, get every 100ms (since 10Hz sensor)
    time = []
    for res in perdelta(datetime.now(), datetime.now() + timedelta(minutes=1), timedelta(milliseconds=100)):
        time.append(res)
    print(len(time))

    # Load Annotations: if you only want some to see some of the classes
    # annotations = []
    # for seq in seqence.semseg:
    #     ann = seq.to_numpy()
    #     for index in range(0, len(ann)):
    #         if(ann[index] == 1 or ann[index] == 2 or ann[index] == 3):
    #             ann[index] = 1
    #         else:
    #             ann[index] = 0
    #     annotations.append(ann)

    # Load Annotations: if you want to see all the classes
    # annotations = []
    # for seq in seqence.semseg:
    #     ann = seq.to_numpy()
    #     annotations.append(ann)

    # Loas scans:
    i = 0
    seqence.lidar.set_sensor(0)
    for scan in seqence.lidar:
        data = scan[['x', 'y', 'z', 'i']].to_numpy(
            dtype=np.float32).reshape(-1, 4)

        #full_data = np.hstack((data, annotations[i]))

        header = Header()
        header.frame_id = velo_frame_id
        header.stamp = rospy.Time.from_sec(
            float(datetime.strftime(time[i], "%s.%f")))

        fields = [PointField('x', 0, PointField.FLOAT32, 1), PointField('y', 4, PointField.FLOAT32, 1), PointField(
            'z', 8, PointField.FLOAT32, 1), PointField('intensity', 12, PointField.FLOAT32, 1)]

        pcl_msg = pcl2.create_cloud(header, fields, data)
        bag.write(velo_topic + '/pointcloud', pcl_msg, t=pcl_msg.header.stamp)

        print(i)

        i += 1

    print("## OVERVIEW ##")
    print(bag)
    bag.close()


if __name__ == '__main__':
    main()
