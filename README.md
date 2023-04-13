# PVABirds
Population viability analysis code for birds from NE Madagascar using the Vortex10 package. 

## Introduction
The simulatePVA.py script modifies a Vortex10* scenario template to specify parameters for a set of bird species from Northeast Madagascar gathered by Cortni Borgerson *et al.* (2023). Values for many of the life history parameters that are used to populate the simulations life tables came from Bird et al. (2020).

*Vortex PVA software (Lacy & Pollak 2022) is provided under a CreativeCommons Attribution-NoDerivatives International License, courtesy of the Species Conservation Toolkit Initiative (https://scti.tools).

## Usage
The script simulatePVA.py has generated all the datafiles in this repo by taking a predefined Vortex10 template file and modifying key parameters for each species using the aforementioned data sources. simulatePVA.py expects that there will be the following resources in the working directory simulatePVA.py is located in:

* A pre-built executable version of Vortex10 contained in an eponymous directory
* A template file for a Vortex10 scenario (ctest1pop.xml in this repo)
* A datafile with tabular values for expected variables (exact variables to be manipulated are specified in the commented code)

Parameters that should be set before running the script are:

* Location and name of template file - set in simulatePVA.py, line 94 (default value is "ctest1pop.xml")
* Location and name of datafile - set in simulatePVA.py, line 8 (default value is "03_08_ 2022_PVA_Bird_Data_cleaned.xlsx")
* Number of model simulations - set in the template file, line 55 (default value is "<nRuns>5000</nRuns>")

Parameters that can be further set before running the script are:

* Number of years that the model should be run for - set in the template file, line 56 (default value is "<nYears>100</nYears>")

To run the simulations, change to the working directory containing the repo and enter the following command into a terminal:
```python simulatePVA.py```

This will initiate a loop that will cycle through every species named in the excel datafile, creating a directory for each species within a superdirectory called "VOutput/species_folders/". Within each species folder (e.g. "Accipiter henstii"), there will be two subfolders: "Harvest" and "Control". 

* The "Harvest" folder contains the model outputs for models run with a harvest stage at each step of the model, representing human intervention (hunting and trapping) in the natural population dynamics.
* The "Control" folder contains the model outputs for models run without a harvest stage, simulating natural population dynamics in the absence of direct human-induced mortality. 

Harvest simulations in this work come in two flavors, "Constant", where the number of harvested animals stays consistent from year-to-year regardless of the population size, and "Population-dependent", where the number of individuals collected varies as a constant proportion of the population's dynamic size at each step of the model. These simulations were produced by using different pre-set templates, one of which used a constant number in the harvest column while the other was modified to contain a formula for producing a raw number as a function of a constant proportion of a dynamic population. The data generated by these different starting conditions are stored in separate final results directories:
 
 * species_by_flat_value_5000x
 * species_by_proportional_value_5000x

As each set of models was run 5,000x, and each "Harvest" run was accompanied by a "Control" run, for each species in this dataset with sufficient data to model (63 species total) there are:

* 5,000 simulations of constantly harvested populations
* 5,000 simulations of population-dependent harvested populations
* 10,000 simulations of non-harvested populations

## Bibliography
Bird, J. P., Martin, R., Akçakaya, H. R., Gilroy, J., Burfield, I. J., Garnett, S. T., ... & Butchart, S. H. (2020). Generation lengths of the world's birds and their implications for extinction risk. Conservation Biology, 34(5), 1252-1261.

Lacy, R.C., and J.P. Pollak. 2022. Vortex: A stochastic simulation of the extinction process. Version 10.5.6. Chicago Zoological Society, Brookfield, Illinois, USA.

