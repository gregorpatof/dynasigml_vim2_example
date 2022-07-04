from dynasigml.dynasig_ml_model import DynaSigML_Model, load_dynasigml_model_from_file

if __name__ == "__main__":
    dsml_model = load_dynasigml_model_from_file("dsml_model.pickle")
    dsml_model.map_coefficients("mutants_modeller/4bz3_WT.pdb", "coefficients.pdb")
