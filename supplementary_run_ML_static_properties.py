from dynasigml.dynasig_ml_model import DynaSigML_Model
import json

if __name__ == "__main__":
    with open("test_ids_8020.json") as f:
        test_ids = json.load(f)
    with open("vim2_exp_labels.json") as f:
        exp_labels = json.load(f)
    dsml_model = DynaSigML_Model("combined_dsdf.pickle", test_ids=test_ids, predictor_columns=exp_labels[1:])
    dsml_model.train_test_lasso()
    dsml_model.train_test_mlp()
    dsml_model.make_graphs('graphs_folder_static_only')
    dsml_model.save_to_file("dsml_static_only")

    dsml_model = DynaSigML_Model("combined_dsdf.pickle", test_ids=test_ids, predictor_columns=["rosetta_ddg", "asa"])
    dsml_model.train_test_lasso()
    dsml_model.train_test_mlp()
    dsml_model.make_graphs('graphs_folder_ddg_asa')
    dsml_model.save_to_file("dsml_ddg_asa")



