## Running Cosmolike projects <a name="running_cosmolike_projects"></a> 

In this tutorial, we assume the user installed Cocoa via the *Conda installation* method, and the name of the Conda environment is `cocoa`. We also presume the user's terminal is in the folder where Cocoa was cloned.

:one: **Step 1 of 7**: activate the Conda Cocoa environment
    
        $ conda activate cocoa

:two: **Step 2 of 7**: go to the project folder (`./cocoa/Cocoa/projects`) and clone the Cosmolike LSST-Y1 project:
    
        $(cocoa) cd ./cocoa/Cocoa/projects
        $(cocoa) git clone --depth 1 git@github.com:SBU-COSMOLIKE/cocoa_lsst_les lsst_les


The option `--depth 1` prevents git from downloading the entire project history. By convention, the Cosmolike Organization hosts a Cobaya-Cosmolike project named XXX at `CosmoLike/cocoa_XXX`. However, our scripts and YAML files assume the removal of the `cocoa_` prefix when cloning the repository.

:three: **Step 3 of 7**: go to `cocoa_les` folder and uncompress the `data` folder

        $(cocoa) cd ./cocoa_les
        $(cocoa) tar xf data.xz

Git ignores the `data` folder (thanks to `.gitignore`) because the covariance files are too large not to be handled by Git-LFS. Git-LFS costs money, so we compress the folder using the `xz` [file format](https://tukaani.org/xz/format.html) (the Conda Cocoa environment contains the `xz` compression program).

:four: **Step 4 of 7**: go back to the Cocoa main folder, and activate the private Python environment
    
        $(cocoa) cd ../
        $(cocoa) source start_cocoa
 
:warning: (**warning**) :warning: Remember to run the start_cocoa script only after cloning the project repository. The script *start_cocoa* creates the necessary symbolic links and adds the *Cobaya-Cosmolike interface* of all projects to `LD_LIBRARY_PATH` and `PYTHONPATH` paths.

:five: **Step 5 of 7**: compile the project
 
        $(cocoa)(.local) source ./projects/lsst_les/scripts/compile_lsst_y1

:six: **Step 6 of 7**: select the number of OpenMP cores
    
        $(cocoa)(.local) export OMP_PROC_BIND=close; export OMP_NUM_THREADS=4
        
:seven:  **Step 7 of 7**: run a template YAML file

One model evaluation:

        $(cocoa)(.local) mpirun -n 1 --mca btl tcp,self --bind-to core:overload-allowed --rank-by core --map-by numa:pe=${OMP_NUM_THREADS} cobaya-run ./projects/lsst_les/EXAMPLE_EVALUATE1.yaml -f
 
MCMC:

        $(cocoa)(.local) mpirun -n 4 --mca btl tcp,self --bind-to core:overload-allowed --rank-by core --map-by numa:pe=${OMP_NUM_THREADS} cobaya-run ./projects/lsst_les/EXAMPLE_MCMC1.yaml -f

## Deleting Cosmolike projects <a name="running_cosmolike_projects"></a>

:warning: (**warning**) :warning: Never delete the `lsst_les` folder from the project folder without running `stop_cocoa` first; otherwise, Cocoa will have ill-defined soft links at `Cocoa/cobaya/cobaya/likelihoods/` , `Cocoa/external_modules/code/` and `Cocoa/external_modules/data/`
