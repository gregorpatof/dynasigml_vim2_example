from dynasigml.dynasig_ml_model import DynaSigML_Model
import json

if __name__ == "__main__":
    with open("test_ids_8020.json") as f:
        test_ids = json.load(f)
    dsml_model = DynaSigML_Model("combined_dsdf.pickle", test_ids=test_ids)
    dsml_model.train_test_lasso()
    dsml_model.train_test_mlp()
    dsml_model.performance_report()
    dsml_model.save_to_file('dsml_model')
