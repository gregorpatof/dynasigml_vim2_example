from dynasigml.dynasig_df import combine_pickled_dynasig_dfs
import glob

if __name__ == "__main__":
    separate_dsdfs = glob.glob("separate_dsdfs/*.pickle")
    combine_pickled_dynasig_dfs(separate_dsdfs, "combined_dsdf")
    