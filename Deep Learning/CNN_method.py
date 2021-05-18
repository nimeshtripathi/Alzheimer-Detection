
def run_iter_epoch(data_train, data_val, data_test=0.0, crossval_fold=10):
    model, tuned_value = get_model_tuned_value(arg.fn, d)
    data_train = ADNI_dataset(arg.fn, arg.path, ratio_ds=arg.ratio_ds)
    data_val = ADNI_dataset(arg.fn, arg.path, ratio_ds=arg.ratio_ds)
    for itr in range(arg.iter_itr):
        loss_tr = train(model, train_loader)
        acc_tr = train(model, tuned_value)
        loss_val = eval(model)
        val_tr = eval(x_val1)

        if loss_val < loss_opt:
            save_model(model, loss_opt == 1)
            loss_opt = loss_val
