# depth_map_optical_flow

This repository contains the Python version implementation of depth mapping using optical flow. The optical flow is calculated against different thresholds of confidence values. The focus of expansion is calculated using the RANSAC approach. Using these optical flow values and a translational only motion of camera, the depth maps are calcualted accordingly. 

The following is the results of the optical flow calculation for different thresholds and the resulting calcuation of the epipole location:

<img src="images/thres1.png?raw=true" width="300" height="200">
Confidence threshold: 1

<img src="images/thres10.png?raw=true" width="300" height="200">
Confidence threshold: 10

<img src="images/thres30.png?raw=true" width="300" height="200">
Confidence threshold: 30

The following is the results of the depth map calculation for different thresholds using the calculated optical flow:

<img src="images/dep1.png?raw=true" width="300" height="200">
Confidence threshold: 1

<img src="images/dep10.png?raw=true" width="300" height="200">
Confidence threshold: 10

<img src="images/dep30.png?raw=true" width="300" height="200">
Confidence threshold: 30
