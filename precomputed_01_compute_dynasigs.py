from dynasigml.dynasig_df import DynaSigDF
import glob
import json

if __name__ == "__main__":
    filenames_list = glob.glob("mutants_modeller/*.pdb")
    with open("vim2_data_dict.json") as f:
        data_dict = json.load(f)
    with open("vim2_exp_labels.json") as f:
        exp_labels = json.load(f)
    data_list = []
    for filename in filenames_list:
        variant_id = filename.split('/')[-1].split('.')[0].split('_')[-1]
        data_list.append(data_dict[variant_id])
    dsdf = DynaSigDF(filenames_list, data_list, exp_labels, "full_dsdf_vim2")