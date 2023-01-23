import subprocess
import os
import re
import pandas as pd
import xml.etree.ElementTree as ET

# Read in bird data with cleaned headers
bird_data_infile = pd.read_excel(io='03_08_ 2022_PVA_Bird_Data_cleaned.xlsx', engine='openpyxl')

# Counter to track rows
counter = 0

# Define variable
bird_species: object

# For every bird species
for bird_species in bird_data_infile['Species'].tolist():

    # Variable definition block
    Order = bird_data_infile['Order'].tolist()[counter]
    Family = bird_data_infile['Family'].tolist()[counter]
    Genus = bird_data_infile['Genus'].tolist()[counter]
    Species = bird_data_infile['Species'].tolist()[counter]
    EngCommonName = bird_data_infile['EngCommonName'].tolist()[counter]
    MalCommonName1 = bird_data_infile['MalCommonName1'].tolist()[counter]
    AgeOfFirstOffspring = bird_data_infile['AgeOfFirstOffspring'].tolist()[counter]
    MaxAgeReproduction = bird_data_infile['MaxAgeReproduction'].tolist()[counter]
    MaxLifeSpan = bird_data_infile['MaxLifeSpan'].tolist()[counter]
    GenLength = bird_data_infile['GenLength'].tolist()[counter]
    # Max
    MeanClutchSizePerYr = bird_data_infile['MeanClutchSizePerYr'].tolist()[counter]
    IncubationTimeDays = bird_data_infile['IncubationTimeDays'].tolist()[counter]
    SexRatioBirthPercM = bird_data_infile['SexRatioBirthPercM'].tolist()[counter]
    AdultSurvivalPropFromBirthToMaxLongevity = bird_data_infile['AdultSurvivalPropFromBirthToMaxLongevity'].tolist()[counter]
    InitialPopulationSizeMasoalaPlus10k = bird_data_infile['InitialPopulationSizeMasoalaPlus10k'].tolist()[counter]
    MoreThan30Observations_Y_N = bird_data_infile['MoreThan30Observations_Y_N'].tolist()[counter]
    PopHarvestedAfterAgeAtFirstOffspringPerYr = bird_data_infile['PopHarvestedAfterAgeAtFirstOffspringPerYr'].tolist()[counter]
    MeanCatchPerHHPerYr = bird_data_infile['MeanCatchPerHHPerYr'].tolist()[counter]
    AbundancePerHectare2015_to_2022 = bird_data_infile['AbundancePerHectare2015_to_2022'].tolist()[counter]
    AbundancePerkm2 = bird_data_infile['AbundancePerkm2'].tolist()[counter]
    ObsCount2015_to_2022 = bird_data_infile['ObsCount2015_to_2022'].tolist()[counter]

    # Constant columns
    YrsDepEst = bird_data_infile['YrsDepEst'].tolist()[counter]
    HumanHHMNP_Plus10k = bird_data_infile['HumanHHMNP_Plus10k'].tolist()[counter]
    HumanPopMNP_Plus10k = bird_data_infile['HumanPopMNP_Plus10k'].tolist()[counter]
    HumanPopDensMNP_Plus10k = bird_data_infile['HumanPopDensMNP_Plus10k'].tolist()[counter]
    AreaMNP = bird_data_infile['AreaMNP'].tolist()[counter]
    AreaLessThan10kmFromMNP = bird_data_infile['AreaLessThan10kmFromMNP'].tolist()[counter]
    TotalMNP_Plus10kAreakm2 = bird_data_infile['TotalMNP_Plus10kAreakm2'].tolist()[counter]
    MNPPercForCov = bird_data_infile['MNPPercForCov'].tolist()[counter]
    LessThan10kmMNP_PercForCov = bird_data_infile['LessThan10kmMNP_PercForCov'].tolist()[counter]

    # Empty columns
    # Turn into constant 1
    MaxBroodPerYr = bird_data_infile['MaxBroodPerYr'].tolist()[counter]
    MaxProgPerBrood = bird_data_infile['MaxProgPerBrood'].tolist()[counter]
    DensityDepReproduction = bird_data_infile['DensityDepReproduction'].tolist()[counter]
    PercBreedingAtLow = bird_data_infile['PercBreedingAtLow'].tolist()[counter]
    PercBreedingAtCarryingCap = bird_data_infile['PercBreedingAtCarryingCap'].tolist()[counter]
    AlleePar = bird_data_infile['AlleePar'].tolist()[counter]
    SteepnessPar = bird_data_infile['SteepnessPar'].tolist()[counter]
    Monogamous = bird_data_infile['Monogamous'].tolist()[counter]
    Polygynous = bird_data_infile['Polygynous'].tolist()[counter]
    Hermaphroditic = bird_data_infile['Hermaphroditic'].tolist()[counter]
    LongTermMonogamy = bird_data_infile['LongTermMonogamy'].tolist()[counter]
    LongTermPolygyny = bird_data_infile['LongTermPolygyny'].tolist()[counter]
    PercAdFemBreeding = bird_data_infile['PercAdFemBreeding'].tolist()[counter]
    SDPercAdFemBreedingDueToEnvVar = bird_data_infile['SDPercAdFemBreedingDueToEnvVar'].tolist()[counter]
    MortalityRate_0_to_1 = bird_data_infile['MortalityRate_0_to_1'].tolist()[counter]
    MortalityRate_SD_0_to_1 = bird_data_infile['MortalityRate_SD_0_to_1'].tolist()[counter]
    MortalityRate_1_to_2 = bird_data_infile['MortalityRate_1_to_2'].tolist()[counter]
    MortalityRate_SD_1_to_2 = bird_data_infile['MortalityRate_SD_1_to_2'].tolist()[counter]
    MortalityRate_2_and_older = bird_data_infile['MortalityRate_2_and_older'].tolist()[counter]
    MortalityRate_SD_2_and_older = bird_data_infile['MortalityRate_SD_2_and_older'].tolist()[counter]
    PercMaleInBreedingPool_Alt_MateMonopolization = bird_data_infile['PercMaleInBreedingPool_Alt_MateMonopolization'].tolist()[counter]
    SizePerAgeYr = bird_data_infile['SizePerAgeYr'].tolist()[counter]
    CarryingCapMasoalaPlus10k = bird_data_infile['CarryingCapMasoalaPlus10k'].tolist()[counter]
    CarryingCapMasoalaPlus10k_SD = bird_data_infile['CarryingCapMasoalaPlus10k_SD'].tolist()[counter]
    ChangeInCarCap = bird_data_infile['ChangeInCarCap'].tolist()[counter]
    ChangeInCarCapInYrs = bird_data_infile['ChangeInCarCapInYrs'].tolist()[counter]

    # Formatting block
    bird_species_formatted = re.sub(' ', '_', bird_species)

    # Increment counter
    counter += 1

    yearlyMortality = (1 - float(AdultSurvivalPropFromBirthToMaxLongevity)) * 100
    # print("Yearly Mortality: " + str(yearlyMortality))
    # Open template test xml as f
    if pd.isna(InitialPopulationSizeMasoalaPlus10k) is False:
        print(counter)
        with open('ctest1pop.xml', encoding='latin-1') as f:

            # Read xml tree
            tree = ET.parse(f)

            # Get tree root
            root = tree.getroot()

            # Find relevant xml fields block
            title = root.find('.//ProjectTitle')
            nPops = root.find('.//nPops')
            nRuns = root.find('.//nRuns')
            nYears = root.find('.//nYears')
            FemaleBreedingAge = root.find('.//FemaleBreedingAge')
            MaleBreedingAge = root.find('.//MaleBreedingAge')
            FemaleLastBreedingAge = root.find('.//FemaleLastBreedingAge')
            MaleLastBreedingAge = root.find('.//MaleLastBreedingAge')
            MaximumAge = root.find('.//MaximumAge')
            maxBroodSize = root.find('.//maxBroodSize')
            SexRatio = root.find('.//SexRatio')
            DepOffspring = root.find('.//DepOffspring')
            PercentBreed = root.find('.//PercentBreed')
            FemaleMort = root.findall('.//FemaleMort')
            MaleMort = root.findall('.//MaleMort')
            InitialN = root.find('.//InitialN')
            Ks = root.find('.//CarryingCapacity/K')
            EVK = root.find('.//EVK')
            HarvestStartYear = root.find('.//Harvest/StartYear')
            HarvestEndYear = root.find('.//Harvest/EndYear')
            HarvestInterval = root.find('.//Harvest/Interval')
            HarvestFemale = root.findall('.//FemalesAge')
            HarvestMale = root.findall('.//MalesAge')
            FemaleMort = root.findall('.//MortalityRates/FemaleMort')
            MaleMort = root.findall('.//MortalityRates/MaleMort')
            EVFemaleMort = root.findall('.//MortalityRates/EVFemaleMort')
            EVMaleMort = root.findall('.//MortalityRates/EVMaleMort')
            AgeOfFirstOffspringRounded = round(AgeOfFirstOffspring)

            # Set variables from template file to species-specific values
            try:
                title.text = title.text.replace('qwre', bird_species_formatted)
                nPops.text = nPops.text.replace('2', '1')
                MaxLifeSpanRounded = round(MaxLifeSpan)
                MaximumAge.text = MaximumAge.text.replace('10', str(MaxLifeSpanRounded))
                MaxAgeReproductionRounded = round(MaxAgeReproduction)
                FemaleLastBreedingAge.text = FemaleLastBreedingAge.text.replace('10', str(MaxAgeReproductionRounded))
                MaleLastBreedingAge.text = MaleLastBreedingAge.text.replace('10', str(MaxAgeReproductionRounded))
                FemaleBreedingAge.text = FemaleBreedingAge.text.replace('2', str(AgeOfFirstOffspringRounded))
                MaleBreedingAge.text = MaleBreedingAge.text.replace('2', str(AgeOfFirstOffspringRounded))
                maxBroodSizeRounded = round(MeanClutchSizePerYr)
                maxBroodSize.text = maxBroodSize.text.replace('2', str(maxBroodSizeRounded))
                PercentBreed.text = PercentBreed.text.replace('50', '100')
                HarvestStartYear.text = HarvestStartYear.text.replace('0', str(AgeOfFirstOffspringRounded))
                HarvestEndYear.text = HarvestEndYear.text.replace('0', str(MaxLifeSpanRounded))

                for child in FemaleMort:
                    currentAge = child.get('age')
                    if currentAge != '0':
                        child.text = child.text.replace('10', str(yearlyMortality))
                    else:
                        child.text = child.text.replace('50', str(yearlyMortality))
                for child in MaleMort:
                    currentAge = child.get('age')
                    if currentAge != '0':
                        child.text = child.text.replace('10', str(yearlyMortality))
                    else:
                        child.text = child.text.replace('50', str(yearlyMortality))

                InitPopRounded = round(InitialPopulationSizeMasoalaPlus10k)
                InitialN.text = InitialN.text.replace('50', str(InitPopRounded))
                TenPercSD = round(InitPopRounded/10)
                Ks.text = Ks.text.replace('100', str(InitPopRounded))
                EVK.text = EVK.text.replace('0', str(TenPercSD))
                PopHarvestedAfterAgeAtFirstOffspringPerYrRounded = round(PopHarvestedAfterAgeAtFirstOffspringPerYr)
                print("p: " + str(PopHarvestedAfterAgeAtFirstOffspringPerYrRounded))
                percentOption = PopHarvestedAfterAgeAtFirstOffspringPerYrRounded/InitPopRounded
                rawNumberOption = round(PopHarvestedAfterAgeAtFirstOffspringPerYrRounded/2)
                print("empiricalOption: " + str(percentOption))
                #SexUnbiasedHarvestEstimate = '(N/2)*' + str(percentOption)
                SexUnbiasedHarvestEstimate = rawNumberOption

                for child in HarvestFemale:
                    currentAge = int(child.get('age'))
                    if currentAge == AgeOfFirstOffspringRounded:
                        child.text = child.text.replace('0', str(SexUnbiasedHarvestEstimate))
                    elif currentAge > AgeOfFirstOffspringRounded:
                        child.text = re.sub('0', 'DELETEME', child.text)

                for child in HarvestMale:
                    currentAge = int(child.get('age'))
                    if currentAge == AgeOfFirstOffspringRounded:
                        child.text = child.text.replace('0', str(SexUnbiasedHarvestEstimate))
                    elif currentAge > AgeOfFirstOffspringRounded:
                        child.text = re.sub('0', 'DELETEME', child.text)

                for child in FemaleMort:
                    currentAge = int(child.get('age'))
                    if currentAge > AgeOfFirstOffspringRounded:
                        child.text = re.sub(r"(.*)", 'DELETEME', child.text)

                for child in MaleMort:
                    currentAge = int(child.get('age'))
                    if currentAge > AgeOfFirstOffspringRounded:
                        child.text = re.sub(r"(.*)", 'DELETEME', child.text)

                for child in EVFemaleMort:
                    currentAge = int(child.get('age'))
                    if currentAge > AgeOfFirstOffspringRounded:
                        child.text = re.sub(r"(.*)", 'DELETEME', child.text)

                for child in EVMaleMort:
                    currentAge = int(child.get('age'))
                    if currentAge > AgeOfFirstOffspringRounded:
                        child.text = re.sub(r"(.*)", 'DELETEME', child.text)

            except AttributeError:
                pass

            # Output directory and file creation block
            dir_name = 'species_folders\\' + bird_species_formatted

            # Get working directory
            working_dir = os.getcwd()

            # Make new path for species-level directories
            path = os.path.join(working_dir, dir_name)

            # Make new directories from path
            try:
                os.mkdir(path)
            except FileExistsError:
                pass

            # Make names for pre_processed xml files for PVA
            output_name = dir_name + '\\pre_processing' + bird_species_formatted + '.xml'
            output_name_harvested = dir_name + '\\processed_' + bird_species_formatted + '_harvested.xml'
            output_name_control = dir_name + '\\processed_' + bird_species_formatted + '_control.xml'
            command_output_name_harvested = path + '\\processed_' + bird_species_formatted + '_harvested.xml'
            command_output_name_control = path + '\\processed_' + bird_species_formatted + '_control.xml'
            script_path = os.path.join(working_dir, "Vortex10\\Vortex10Command.exe")

            # Write preprocessed xml
            tree.write(output_name)

            # Process inconsistencies in organism age throughout
            with open(output_name, encoding='latin-1') as preprocessed:

                # Read xml tree
                tree = ET.parse(preprocessed)

                # Get tree root
                root = tree.getroot()

                for HarvestRemoval in root.iter('Harvest'):
                    for MalesAge in HarvestRemoval.findall('MalesAge'):
                        if re.match('DELETEME', MalesAge.text):
                            HarvestRemoval.remove(MalesAge)
                    for FemalesAge in HarvestRemoval.findall('FemalesAge'):
                        if re.match('DELETEME', FemalesAge.text):
                            HarvestRemoval.remove(FemalesAge)

                for Mortality in root.iter('MortalityRates'):
                    for FemaleMortInstance in Mortality.findall('FemaleMort'):
                        if re.match('DELETEME', FemaleMortInstance.text):
                            Mortality.remove(FemaleMortInstance)
                    for MaleMortInstance in Mortality.findall('MaleMort'):
                        if re.match('DELETEME', MaleMortInstance.text):
                            Mortality.remove(MaleMortInstance)
                    for EVFemaleMortInstance in Mortality.findall('EVFemaleMort'):
                        if re.match('DELETEME', EVFemaleMortInstance.text):
                            Mortality.remove(EVFemaleMortInstance)
                    for EVMaleMortInstance in Mortality.findall('EVMaleMort'):
                        if re.match('DELETEME', EVMaleMortInstance.text):
                            Mortality.remove(EVMaleMortInstance)

                # Write xml for harvest scenario
                tree.write(output_name_harvested)

                # Change Harvest variable to False
                HarvestBool = root.find('.//Harvest/Harvest')
                HarvestBool.text = HarvestBool.text.replace('True', 'False')

                # Write xml for control scenario
                tree.write(output_name_control)

            # Print command string for manual
            PrePath = path + "\\VOutput"
            HarvestPath = path + "\\Harvested"
            ControlPath = path + "\\Control"

            # Print command line input to screen for harvest scenario
            commandStringHarvest = "\"" + script_path + "\" " + "\"" + command_output_name_harvested + "\""
            print(commandStringHarvest)

            # Run Vortex10 for harvest scenario, save and rename output
            subprocess.run([script_path, command_output_name_harvested])
            os.rename(PrePath, HarvestPath)

            # Print command line input to screen for control (non-harvested) scenario
            commandStringControl = "\"" + script_path + "\" " + "\"" + command_output_name_control + "\""
            print(commandStringControl)

            # Run Vortex10 for control scenario, save and rename output
            subprocess.run([script_path, command_output_name_control])
            os.rename(PrePath, ControlPath)

