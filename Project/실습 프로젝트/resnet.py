%matplotlib inline
from __future__ import print_fuction, division

import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim import lr_scheduler
import numpy as np
import torchvision
from torchvision import datasets, models, transforms
import matplotlib.pyplot as plt
import time
import os
import copy
plt.ion()

fro, google.colab import drive
drive.mount('/content/drive')

data_transforms = {
    'train':transforms.Compose([
       transforms.RandomResizesCrop(224),
       transforms.RandomHorizontalFlip( ),
       transforms.ToTensor((),
       transforms.Normalize([0.485, 0.465, 0.406], [0.229, 0.224, 0.225]))
    ]),
    'val':transforms.Compose([
      transform.Resize(256),
      transforms.CenterCrop(224),
      transforms.ToTensor( ),
      transforms.Normalize([0.485, 0.465, 0.406], [0.229, 0.224, 0.225]))
    ]),
}

data_dir = '/content/drive/My Drive/hymenoptera_data'
image_datasets = {x: datasests.ImageFolder(os.path.join(data_dir, x), data_transforms[x]) for x in ['train', 'val']}
dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size=4, shuffle=True, num_workers=4) for x in ['train', 'val']}
class_names = image_datasets['train'].classes
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")