# Mask R-CNN for Object Detection and Segmentation on KITTI Dataset

## Bug fixes to run it in Google Colab

* Replaced keras.engine with keras.layers
* Replaced keras.topology with keras.savings
* Replaced scipy.misc.imresize with cv2.resize (swapped height and width because of OpenCV standard)
* Added option to not use padding for non-squared images
* Use cv2.INTER_NEAREST and cv2.INTER_LINEAR for resizing images to have stable outputs

## Procedure

### 1 Dataset

### 2 Visualizer

### 3 Naive Solution

### 4 Research state-of-the-art

### 5 Set up Transfer Learning

### 6 Data augmentation and Training

## Results
