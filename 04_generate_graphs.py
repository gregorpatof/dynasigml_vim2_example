from dynasigml.dynasig_ml_model import load_dynasigml_model_from_file

if __name__ == "__main__":
    dsml_model = load_dynasigml_model_from_file("dsml_model.pickle")
    dsml_model.make_graphs("graphs_folder")
