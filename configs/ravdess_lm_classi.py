import torch
import torch.nn as nn
import os

from my_models import models
from utils.utils import Config

HOME = os.path.expanduser('~')

config = Config({
    # General configs
    'use_cuda': True,
    'log_run': True,

    # Dataset configs
    'data_path': HOME + '/Datasets/RAVDESS/Landmarks',
    'data_format': 'landmarks',
    'validation_split': .2,
    'sequence_length': 1,
    'step_size': 1,
    'image_size': 64,

    # Hyper parameters
    'num_epochs': 100,
    'learning_rate': 0.001,
    'batch_size': 32,

    # Logging
    'log_interval': 10000,
    'save_interval': 1,
    'save_path': 'saves/Classification_Landmarks'
})

config.update({
    # Model parameters
    'model': nn.Sequential(
        nn.Flatten(),
        nn.Linear(34 * config.window_size, 8),
    ),
    # 'model': models.LandmarksLSTM(config.window_size)
})

config.update({
    # Optimizer
    'optim': torch.optim.Adam(params=config.model.parameters(),
                              lr=config.learning_rate),
})
