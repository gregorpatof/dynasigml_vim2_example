from dynasigml.dynasig_ml_model import DynaSigML_Model

if __name__ == "__main__":
    dsml_model = DynaSigML_Model("combined_dsdf.pickle", predictor_columns=["dynasig"])
    dsml_model.train_test_lasso()
    dsml_model.train_test_mlp()
    dsml_model.save_to_file("dsml_dynasig_only")