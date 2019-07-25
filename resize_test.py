import cv2
import matplotlib.pyplot as plt
import numpy as np
import imageio
import matplotlib.image as mpimg
import scipy.misc as sp


filename = "000000_10.png"
height = 320
width = 1152
gt_image = imageio.imread("../data_semantics/training/instance/" + filename)
print(np.max(gt_image))
instance_gt = np.array(gt_image) % 256
semantic_gt = np.array(gt_image) // 256
#plt.imshow(semantic_gt)
#plt.show()
print(np.unique(instance_gt))
print(np.unique(semantic_gt))
instance_gt = cv2.resize(instance_gt, (width, height), interpolation=cv2.INTER_NEAREST)
semantic_gt = cv2.resize(semantic_gt, (width, height), interpolation=cv2.INTER_NEAREST)
print(np.unique(instance_gt))
print(np.unique(semantic_gt))
#plt.imshow(semantic_gt2)
#plt.show()
labels = [26, 24]
for l in labels:
    mask_sem = (semantic_gt == [l]).astype(np.int_) * 255
    mask_ins = instance_gt & mask_sem
    num_ins = np.max(mask_ins)
    print(l, num_ins, np.unique(mask_ins))
    
    for i in range(1, num_ins + 1):
        mask_obj = (mask_ins == [i]).astype(np.int_) * 255
        print(i, np.sum(mask_obj == [255]))
        plt.imshow(mask_obj)
        plt.show()