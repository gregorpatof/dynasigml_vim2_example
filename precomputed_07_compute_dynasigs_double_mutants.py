from dynasigml.dynasig_df import DynaSigDF
from dynasigml.dynasig_ml_model import load_dynasigml_model_from_file
import glob

if __name__ == "__main__":
    filenames_list = glob.glob("double_mutants/*.pdb")
    exp_data = [0 for x in filenames_list]
    exp_labels = ["dummy"]
    dsml = load_dynasigml_model_from_file("dsml_dynasig_only.pickle")
    best_beta_values = dsml.get_best_beta_values()
    dsdf = DynaSigDF(filenames_list, exp_data, exp_labels, "dsdf_double_mutants", beta_values=best_beta_values)
