# Table of contents
1. [Running Cosmolike projects](#running_cosmolike_projects)
2. [Deleting Cosmolike projects](#delete_projects)
3. [Updating the data folder](#updating_data)
4. [Optimistic/Pessimistic choice of parameters](#opt_neg)   
5. [Mask choices](#mask_choices) 

## Running Cosmolike projects <a name="running_cosmolike_projects"></a> 

In this tutorial, we assume the user installed Cocoa via the *Conda installation* method, and the name of the Conda environment is `cocoa`. We also presume the user's terminal is in the folder where Cocoa was cloned.

:one: **Step 1 of 7**: activate the Conda Cocoa environment
    
        $ conda activate cocoa

:two: **Step 2 of 7**: go to the `projects` folder and clone the Cosmolike LSST-Y1 project:
    
        $(cocoa) cd ./cocoa/Cocoa/projects
        $(cocoa) git clone --depth 1 git@github.com:SBU-COSMOLIKE/cocoa_lsst_les lsst_les


The option `--depth 1` prevents git from downloading the entire project history. By convention, the Cosmolike Organization hosts a Cobaya-Cosmolike project named XXX at `CosmoLike/cocoa_XXX`. However, our scripts and YAML files assume the removal of the `cocoa_` prefix when cloning the repository.

:three: **Step 3 of 7**: go to `cocoa_les` folder and uncompress the `data` folder

        $(cocoa) cd ./cocoa_les
        $(cocoa) tar xf data.xz

Git ignores the `data` folder (thanks to `.gitignore`) because the covariance files are too large not to be handled by Git-LFS. Git-LFS costs money, so we compress the folder using the `xz` [file format](https://tukaani.org/xz/format.html).

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

## Deleting Cosmolike projects <a name="delete_projects"></a>

:warning: (**warning**) :warning: Never delete the `lsst_les` folder from the project folder without running `stop_cocoa` first; otherwise, Cocoa will have ill-defined soft links at `Cocoa/cobaya/cobaya/likelihoods/` , `Cocoa/external_modules/code/` and `Cocoa/external_modules/data/`

## Updating the data folder <a name="updating_data"></a>

In this tutorial, we assume the user installed Cocoa via the *Conda installation* method, and the name of the Conda environment is `cocoa`. We also presume the user's terminal is in the folder where Cocoa was cloned.

:one: **Step 1 of 3**: activate the Conda Cocoa environment
    
        $ conda activate cocoa
        
The Conda Cocoa environment contains the `xz` compression program. 

:two: **Step 2 of 3**: go to the `lsst_les` folder and clone the Cosmolike LSST-Y1 project:
    
        $(cocoa) cd ./cocoa/Cocoa/projects/lsst_les

:three: **Step 3 of 3**: delete the `data.xz` file, and then type

        $(cocoa) tar -cf - data/ | xz -k -9e --threads=4 -c - > data.xz

Compression may take a few minutes. Afterward, proceed with the usual `git commit` and `git push` commands.

## Optimistic/Pessimistic choice of parameters <a name="opt_neg"></a>

This is our suggestion for optimistic/pessimistic choices of IA, photo-z, and shear bias.

<img width="627" alt="Screenshot 2023-08-03 at 3 57 17 PM" src="https://github.com/SBU-COSMOLIKE/cocoa_lsst_les/assets/3210728/909f2f51-1e92-42cf-98c4-f18d6de3584e">

## Mask choices <a name="mask_choices"></a>

The Python file `calculate_mask.py` on `/data` allows the user to create mask files. We do provide the following mask files for Y1/Y3/Y6/Y10 data
        if (mask_choice == 1):
          # LSST_YX_M1.mask  (lmax = 3000) on CS -----------------------------------------
          # lmax \times \theta_min corresponds to the first zero of the Bessel 𝐽0/4
          ξp_CUTOFF = 2.756  # cutoff scale in arcminutes
          ξm_CUTOFF = 8.696  # cutoff scale in arcminutes
          gc_CUTOFF = 21     # Galaxy clustering cutoff in Mpc/h
        elif (mask_choice == 2):
          # LSST_YX_M2.mask  (lmax = 1500) on CS -----------------------------------------
          # lmax \times \theta_min corresponds to the first zero of the Bessel 𝐽0/4
          ξp_CUTOFF = 5.512  # cutoff scale in arcminutes
          ξm_CUTOFF = 17.392  # cutoff scale in arcminutes
          gc_CUTOFF = 21     # Galaxy clustering cutoff in Mpc/h
        elif (mask_choice == 3):
          # LSST_YX_M3.mask  (lmax = 750) on CS -----------------------------------------
          # lmax \times \theta_min corresponds to the first zero of the Bessel 𝐽0/4
          ξp_CUTOFF = 11.024 # cutoff scale in arcminutes
          ξm_CUTOFF = 34.784 # cutoff scale in arcminutes
          gc_CUTOFF = 21     # Galaxy clustering cutoff in Mpc/h
