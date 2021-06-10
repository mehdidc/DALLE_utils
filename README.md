# DALLE_clip_score

Utility functions that can be used for <https://github.com/lucidrains/DALLE-pytorch>  experiments.

## How to install ?

`python setup.py install`

## How to use ?


### Splitting a dataset into train/test

Example:

`dalle_utils  split  CUB_200_2011 --train-ratio=0.9 --seed=42 CUB_200_2011`

will create a train and test folder in CUB_200_2011 with 90% training  and 10% test, randomly splitted.
