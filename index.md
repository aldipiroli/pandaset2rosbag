# PandaSet 2 Rosbag
Convert  [PandaSet dataset](https://scale.com/open-datasets/pandaset) to Rosbags with Python. Please refer to [pandaset-devkit](https://github.com/scaleapi/pandaset-devkit) for the official devkit.

![Figure](https://github.com/aldipiroli/PandaSet_2_Rosbag/blob/master/img/img1.png)

## Dataset
### Download

To download the dataset, please visit the official [PandaSet](https://pandaset.org/ "Pandaset Official Website") webpage and sign up through the form.
You will then be forwarded to a page with download links to the raw data and annotations.

### Unpack

Unpack the archive into any directory on your hard disk. The path will be referenced in usage of `pandaset-devkit` later, and does not have to be in the same directory as your scripts.

### Structure

#### Files & Folders

```text
.
├── LICENSE.txt
├── annotations
│   ├── cuboids
│   │   ├── 00.pkl.gz
│   │   .
│   │   .
│   │   .
│   │   └── 79.pkl.gz
│   └── semseg  // Semantic Segmentation is available for specific scenes
│       ├── 00.pkl.gz
│       .
│       .
│       .
│       ├── 79.pkl.gz
│       └── classes.json
├── camera
│   ├── back_camera
│   │   ├── 00.jpg
│   │   .
│   │   .
│   │   .
│   │   ├── 79.jpg
│   │   ├── intrinsics.json
│   │   ├── poses.json
│   │   └── timestamps.json
│   ├── front_camera
│   │   └── ...
│   ├── front_left_camera
│   │   └── ...
│   ├── front_right_camera
│   │   └── ...
│   ├── left_camera
│   │   └── ...
│   └── right_camera
│       └── ...
├── lidar
│   ├── 00.pkl.gz
│   .
│   .
│   .
│   ├── 79.pkl.gz
│   ├── poses.json
│   └── timestamps.json
└── meta
    ├── gps.json
    └── timestamps.json
```

## Instructions

### Setup

1. Create a Python>=3.6 environment with `pip` installed.
2. Clone the repository `git clone https://github.com/scaleapi/pandaset-devkit`
3. `cd` into `pandaset-devkit/python`
4. Execute `pip3 install .`
5. Clone this repository `https://github.com/aldipiroli/PandaSet_2_Rosbag`

### Usage
In `PandaSet_2_Rosbag/pandaset2rosbag.py`:

1. Set the scene number e.g. `bag_ID = 001` 
2. Set the bag name and location `bag_name = /home/user/dataset/RosBags/ + str(bag_ID) + '.bag'`
3. Set the dataset location `dataset = DataSet('/home/user/dataset/Pandaset/dataset/')`
4. Launch the file `python3 pandaset2rosbag.py`
