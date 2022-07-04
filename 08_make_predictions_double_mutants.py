from dynasigml.dynasig_df import load_pickled_dynasig_df
from dynasigml.dynasig_ml_model import load_dynasigml_model_from_file
import numpy as np

if __name__ == "__main__":
    dsdf_double_mutants = load_pickled_dynasig_df("dsdf_double_mutants.pickle")
    dsml_model = load_dynasigml_model_from_file("dsml_dynasig_only.pickle")
    all_file_ids = dsdf_double_mutants.get_file_ids()

    data_lasso = dsdf_double_mutants.get_data_array(all_file_ids, beta=dsml_model.get_best_beta_lasso())
    data_lasso = data_lasso[:, 2:] # reject first two columns (beta value and dummy experimental measure)
    predictions_lasso = dsml_model.predict_lasso(data_lasso)

    data_mlp = dsdf_double_mutants.get_data_array(all_file_ids, beta=dsml_model.get_best_beta_mlp())
    data_mlp = data_mlp[:, 2:]
    predictions_mlp = dsml_model.predict_mlp(data_mlp)

    lasso_zscores = (predictions_lasso - np.mean(predictions_lasso)) / np.std(predictions_lasso)
    mlp_zscores = (predictions_mlp - np.mean(predictions_mlp)) / np.std(predictions_mlp)
    with open("predictions_double_mutants.df", "w") as f:
        f.write("file_id pred_lasso pred_mlp pred_lasso_zscore pred_mlp_zscore sum_zscores\n")
        for file_id, pred_lasso, pred_mlp, lasso_z, mlp_z in zip(all_file_ids, predictions_lasso, predictions_mlp,
                                                                 lasso_zscores, mlp_zscores):
            f.write("{} {} {} {} {} {}\n".format(file_id, pred_lasso, pred_mlp, lasso_z, mlp_z, lasso_z + mlp_z))
