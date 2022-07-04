from dynasigml.dynasig_df import DynaSigDF
import sys
import glob
import json

if __name__ == "__main__":
    if len(sys.argv) != 2:
        raise ValueError("I need one argument: the job index")
    job_index = int(sys.argv[1])
    assert 0 <= job_index <= 19
    n_total_jobs = 20
    filenames_list = sorted(glob.glob("mutants_modeller/*.pdb"))
    step = int(len(filenames_list)/float(n_total_jobs) + 1)
    start = job_index * step
    stop = (job_index+1) * step
    sub_filenames_list = filenames_list[start:stop]
    with open("vim2_data_dict.json") as f:
        data_dict = json.load(f)
    with open("vim2_exp_labels.json") as f:
        exp_labels = json.load(f)
    data_list = []
    for filename in sub_filenames_list:
        variant_id = filename.split('/')[-1].split('.')[0].split('_')[-1]
        data_list.append(data_dict[variant_id])
    dsdf_name = "separate_dsdfs/partial_dsdf_vim2_{}".format(job_index)
    beta_values = [np.e ** (x / 2) for x in range(-6, 7)]
    dsdf = DynaSigDF(sub_filenames_list, data_list, exp_labels, dsdf_name, beta_values=beta_values)
