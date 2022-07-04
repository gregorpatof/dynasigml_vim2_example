import sys
import os


def make_job(filename, header_lines, index):
    with open(filename, "w") as f:
        f.write(''.join(header_lines) + " {}\n".format(index))


def make_all_jobs(jobs_dir):
    with open('slurm_header.txt') as f:
        lines = f.readlines()
    newlines = []
    for line in lines:
        if line.strip().endswith('YOUR_ACCOUNT_HERE'):
            raise ValueError('You need to change the slurm_header.txt file and put your account name.')
        if line.startswith('LOAD_YOUR_MODULES_HERE_IF_NEEDED'):
            raise ValueError('You need to remove the LOAD_YOUR_MODULES_HERE_IF_NEEDED line in slurm_header.txt ' +
                             'and replace it with the commands to load your Python environment, if needed.')
        if line.startswith('cd /path/to/your/dynasigml_vim2_example/folder'):
            raise ValueError('You need to change the cd /path/to/your/dynasigml_vim2_example/folder line in ' +
                             'slurm_header.txt and replace it with the full path to the dynasigml_vim2_example folder.')
        if line.startswith('python run_one_dynasigdf.py'):
            line = 'python run_one_dynasigdf.py'
            newlines.append(line)
            break
        newlines.append(line)
    with open('{}/start_jobs.sh'.format(jobs_dir), 'w') as f:
        for i in range(20):
            jobname = 'job_{}.sh'.format(i)
            make_job('{}/{}'.format(jobs_dir, jobname), newlines, i)
            f.write('sbatch {}\n'.format(jobname))


if __name__ == "__main__":
    if not os.path.isdir("parallel_jobs"):
        os.mkdir("parallel_jobs")
    make_all_jobs("parallel_jobs")
