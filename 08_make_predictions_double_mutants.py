from dynasigml.dynasig_df import load_pickled_dynasig_df
from dynasigml.dynasig_ml_model import load_dynasigml_model_from_file

if __name__ == "__main__":
    dsdf_double_mutants = load_pickled_dynasig_df("dsdf_double_mutants.pickle")
    dsml_model = load_dynasigml_model_from_file("dsml_dynasig_only")
    all_file_ids = dsdf_double_mutants.get_file_ids()

    data_lasso = dsdf_double_mutants.get_data_array(all_file_ids, beta=dsml_model.get_best_beta_lasso())
    data_lasso = data_lasso[:, 2:] # reject first two columns (beta value and dummy experimental measure)
    predictions_lasso = dsml_model.predict(data_lasso)

    data_mlp = dsdf_double_mutants.get_data_array(all_file_ids, beta=dsml_model.get_best_beta_mlp())
    data_mlp = data_mlp[:, 2:]
    predictions_mlp = dsml_model.predict(data_mlp)

    with open("predictions_double_mutants.df", "w") as f:
        f.write("file_id pred_lasso pred_mlp\n")
        for file_id, pred_lasso, pred_mlp in zip(all_file_ids, predictions_lasso, predictions_mlp):
            f.write("{} {} {}\n".format(file_id, pred_lasso, pred_mlp))
