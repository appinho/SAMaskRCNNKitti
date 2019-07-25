# Mask R-CNN for Object Detection and Segmentation on KITTI Dataset

## Bug fixes to run it in Google Colab

* Replaced keras.engine with keras.layers
* Replaced keras.topology with keras.savings
* Replaced scipy.misc.imresize with cv2.resize (swapped height and width because of OpenCV standard)
* Added option to not use padding for non-squared images
* Use cv2.NEAREST for resizing images to have stable outputs
