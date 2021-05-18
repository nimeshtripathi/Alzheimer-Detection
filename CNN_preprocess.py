#adni dataset: permission required
#adni dataset link: http://adni.loni.usc.edu/
from data import ADNI_dataset
import torch
import argparse


#parser
x_p = argparse.ArgumentParser()
fn = x_p.add_argument("fn", type=str, default="")
iter_epoch = x_p.add_argument("iter_epoch", type=int, default=8)

#split_ratio
ratio_ds = x_p.add_argument("r_ds", type=float, nargs="+")
arg = x_p.parse_args()

#sz refers to the batch-size
sz = x_p.add_argument("sz", type=int, default=6)

def run_iter_epoch(data_train, data_val, data_test=0.0, crossval_fold=10):
    model, tuned_value = get_model_tuned_value(arg.fn, d)
    train_data = ADNI_dataset(arg.fn, arg.path, ratio_ds=arg.ratio_ds)
    val_data = ADNI_dataset(arg.fn, arg.path, ratio_ds=arg.ratio_ds)
    for itr in range(arg.iter_itr):
        loss_tr = train(model, train_loader)
        acc_tr = train(model,tuned_value)
        loss_val = eval(model)
        val_tr = eval(x_val1)
    
        if loss_val < loss_opt:
            save_model(model, loss_opt==1)
            loss_opt = loss_val
