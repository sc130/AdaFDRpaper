# AdaFDR

Git repo to reproduce the results of the paper "AdaFDR: a Fast, Powerful and Covariate-Adaptive Approach to Multiple Hypothesis Testing", 2018.

The python package can be found at the git repo [adafdr](https://github.com/martinjzhang/adafdr). It can be 
installed using 

```
pip install adafdr
```

The data are either incorporated as part of the *adafdr* package or can be found at [AdaFDRpaper_data](https://osf.io/hjwnf/).
- Download the data: `wget https://osf.io/hjwnf/download`
  
  (`download` maybe be changed to the actual name of the compressed file)  
- Extract the file: `tar -zxvf download`

# Experiments
The software version `adafdr 0.1.7` is used for all experiments.
## GTEx demo
Due to the large size of GTEx data, we provide a GTEx demo that is ~100 times smaller but yet carries all important features. 
- Location: `./vignettes/gtex_demo.ipynb`
- Description: the gtex_demo data is incorporated as part of the *adafdr* package and can be loaded directly. It 
  contains 50k associations from the Adipose_Subcutaneous tissue with four covariates. Note that this is after 
  the filtering that only  associations with p-values <0.01 or >0.99 are included.
  Hence the actual number of associations is ~2.5million (50k*50), presenting a good proxy for the full GTEx data. 

## small GTEx data
The two small_GTEx data (Fig. 3a) are incorporated as part of the *adafdr* package and hence can be loaded directly.
Note that this data is not filtered. Hence they contain only 300k associations each, which are smaller than the 
gtex_demo above.
- small_GTEx_Adipose_Subcutaneous: `./vignettes/small_GTEx_Adipose_Subcutaneous.ipynb`
- small_GTEx_Adipose_Visceral_Omentum: `./vignettes/small_GTEx_Adipose_Visceral_Omentum.ipynb`

## RNA-seq experiments
The three RNA-seq datasets are incorporated as part of the *adafdr* package and hence can be loaded directly. 
Jupyter notebook files are provided to reproduce the results of *adafdr*, along with baseline methods *BH* and *SBH*.
- airway: `./vignettes/airway.ipynb`
- bottomly: `./vignettes/bottomly.ipynb`
- passila: `./vignettes/passila.ipynb`

<!--### R methods -->

## Simulations
### Simulation data (Fig. 4, Supp. Fig. 8)
- Simulated data with one covariate: `./vignettes/simulation_1d_bump_slope.ipynb`
- Simulated data with weakly-dependent p-values: `./vignettes/simulation_data_wd.ipynb`
- Simulated data with strongly-dependent p-values: `./vignettes/simulation_data_sd.ipynb`
- Simulated data used in AdaPT: `./vignettes/simulation_data_adapt.ipynb`
- Simulated data used in IHW: `./vignettes/simulation_data_ihw.ipynb`
- Simulated data with two covariates: `./vignettes/simulation_2d_bump_slope`
- Simulated data with ten covariates: Not included since it takes a long time to run in a jupyter notebook. It is recommended 
  to run it using `.sh` commands

### Simulation data in SummarizedBench (Supp. Figs. 9-10)
- Yeast RNA-Seq *in silico* experiment: `./vignettes/simulation_data_yeast.ipynb`
- Polyester RNA-Seq *in silico* experiment: `./vignettes/simulation_data_polyester.ipynb`
- Polyester RNA-Seq *in silico* experiment with uninformative covariate: `./vignettes/simulation_data_polyester_ui.ipynb`
- Simulation varying the number of tests: Not included.
- Simulation varying the non-null proportion: Not included.

<!--## GTEx data
### Python methods 
Only the GTEx data for the two adipose tissues are provided, which can be downloaded from `...`
### R methods
## Comparison with MuTHER data -->


# Data
We make most of the data available in the data folder [AdaFDRpaper_data](https://osf.io/hjwnf/) including
  
- small GTEx data (Fig. 3a): `/data3/martin/AdaFDRpaper_data/gtex_adipose_chr21_300k`
  - The first 300k hypotheses from chromosome 21.
  - Format: col1: p-value; col2: gene-SNP name; col3: log10(expression+0.5); col4: AAF (mean imputed);
    col5: distance from TSS; col6: chromatin states.
    
- RNA-seq data: `AdaFDRpaper/RNA_seq` 
  - Format: .csv file. col1: p-value; col2: ground truth (dummy, all 0); col3: gene expression

- Simulation data:  
  - Simulated data with one covariate: `./simu_1d_bump_slope`
  - Simulated data with weakly-dependent p-values: `./simu_data_wd`
  - Simulated data with strongly-dependent p-values: `./simu_data_sd`
  - Simulated data used in AdaPT: `./simu_data_adapt`
  - Simulated data used in IHW: `./simu_data_ihw`
  - Simulated data with two covariates: `./simu_2d_bump_slope`
  - Simulated data with ten covariates: `./simu_10d_bump_slope`
   - Format: each data is a folder containing 10 random repetitions. For each data file, the format is: col1: p-value;
    col2: ground truth (1 being alternative); col3-...: covariates

- Simulation data in SummarizedBench: The first three each has 10 repetitions, with the naming `data_y` where 
  `y` is the random repitition number. The last two each has 20 repititions, 
  with the naming `data_x_y`, where `x` is the varying parameter and `y` is the random repitition number.
  The format inside each data is the same as above (Simulation data)
  - Yeast RNA-Seq *in silico* experiment: `./data_yeast` 
  - Polyester RNA-Seq *in silico* experiment: `./data_polyester` 
  - Polyester RNA-Seq *in silico* experiment with uninformative covariate: `./data_polyester_ui` 
  - Simulation varying the number of tests: `./data_ntest` 
  - Simulation varying the non-null proportion: `./data_prop_alt` 
  
The GTEx data for the tissue *Adipose_Subcutaneous* is provided as [GTEx_Adipose_Subcutaneous](https://osf.io/c5yk6/) (Fig. 2b, 2c, 2d). It is stored separately due to its large size. 
- Downloading
  - Download the data: `wget https://osf.io/c5yk6/download`
    
    (`download` maybe be changed to the actual name of the compressed file)
  - Extract the file: `tar -zxvf download` 
- Contents
  - Adipose_Subcutaneous tissue with four covariates: 
  `GTEx_Adipose_Subcutaneous/Adipose_Subcutaneous.allpairs.txt.processed.filtered`
  - Adipose_Subcutaneous tissue with four covariates plus the -log10 p-value from the other adipose tissue: 
  `GTEx_Adipose_Subcutaneous/Adipose_Subcutaneous.allpairs.txt.processed.filtered.augmented.txt`
  - Adipose_Subcutaneous tissue with four covariates plus the -log10 p-value from the brain tissue: 
  `GTEx_Adipose_Subcutaneous/Adipose_Subcutaneous.allpairs.txt.processed.filtered.augmented_not_related.txt`
  - Format: col1: gene-SNP name; col2: gene expression; col3: AAF; col4: distance from TSS; 
    col5: chromatin states; col7: p-value; col8 (if exist): augmented p-value
# Citation 
Zhang, Martin J., Fei Xia, and James Zou. "AdaFDR: a Fast, Powerful and Covariate-Adaptive Approach to Multiple Hypothesis Testing." bioRxiv (2018): 496372.

Xia, Fei, et al. "Neuralfdr: Learning discovery thresholds from hypothesis features." Advances in Neural Information Processing Systems. 2017.
