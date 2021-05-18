# adni dataset: permission required
# adni dataset link: http://adni.loni.usc.edu/
from data import ADNI_dataset
import torch
import argparse

# parser
x_p = argparse.ArgumentParser()
fn = x_p.add_argument("fn", type=str, default="")
iter_epoch = x_p.add_argument("iter_epoch", type=int, default=8)

# split_ratio
ratio_ds = x_p.add_argument("r_ds", type=float, nargs="+")
arg = x_p.parse_args()

# sz refers to the batch-size
sz = x_p.add_argument("sz", type=int, default=6)
