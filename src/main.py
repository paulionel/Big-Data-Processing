'''

Paul Steiner
CS 1440
ASSN 2: Big Data Processing
Sources used can be found in README

'''

import time
import sys
from Report import Report

if __name__ == '__main__':
    rpt = Report()

    '''if sys.argv[1] is not given, print a usage message and exit'''
    if len(sys.argv) < 2:
        print("Usage: src/main.py DATA_DIRECTORY", file=sys.stderr)
        sys.exit(1)

    print("Reading the databases...", file=sys.stderr)
    before = time.time()

    '''if opening the file 'sys.argv[1]/area_titles.csv' fails, let your program crash here'''
    directory = sys.argv[1]
    directoryWithAreaCsvFile = directory + "/area_titles.csv"
    '''print("DIRECTORY = " + directory, file=sys.stderr)'''
    fileAreaTitlesCsv = open(directoryWithAreaCsvFile)
    # print(fileAreaTitlesCsv.read())
    fileAreaTitlesCsv.close()

    '''Convert the file 'sys.argv[1]/area_titles.csv' into a dictionary'''
    areaTitlesDictionary = {}
    f = open(directoryWithAreaCsvFile)
    for line in f:
        k, v = line.rstrip().split(",", 1)
        areaTitlesDictionary[k] = v
    f.close()
    # print(f"There are {len(areaTitlesDictionary)} pairs of data in the dictionary")
    # I tried the commented out code below, but it didn't work...
    '''for key in areaTitlesDictionary:
        if key.endswith("000\""):
            del directoryWithAreaCsvFile[key]
        elif key.startswith("\"US"):
            del directoryWithAreaCsvFile[key]
        elif key.startswith("\"C"):
            del directoryWithAreaCsvFile[key]
        elif key.startswith("\"M"):
            del directoryWithAreaCsvFile[key]'''
    # So I ended up with this code and I think it works
    # basically it gathers up all the stuff I don't want
    remove = [k for k in areaTitlesDictionary if k.endswith("000\"") or k.startswith("\"US") or k.startswith("\"C") or k.startswith("\"M")]
    # and then it deletes it here VvVvV
    for k in remove: del areaTitlesDictionary[k]
    # print(f"There are {len(areaTitlesDictionary)} pairs of data in the dictionary")
    # for key in areaTitlesDictionary:
    #    print(f"{key} => {areaTitlesDictionary[key]}")

    # if opening the file 'sys.argv[1]/2019.annual.singlefile.csv' fails, let your program crash here
    directoryWithAnnualSingleFile = directory + "/2019.annual.singlefile.csv"
    fileAnnualSingleFile = open(directoryWithAnnualSingleFile)

    "Collect information from 'sys.argv[1]/2019.annual.singlefile.csv', place into the Report object rpt"
    # Values for all industries
    numAreas = 0
    grossAnnualWages = 0
    maxAnnualWageArea = ""
    maxAnnualWageAmount = 0
    totalEstab = 0
    maxEstabArea = ""
    maxEstabAmount = 0
    totalEmploy = 0
    maxEmployArea = ""
    maxEmployAmount = 0

    # Values for software publishing industry
    softNumAreas = 0
    softGrossAnnualWages = 0
    softMaxAnnualWageArea = ""
    softMaxAnnualWageAmount = 0
    softTotalEstab = 0
    softMaxEstabArea = ""
    softMaxEstabAmount = 0
    softTotalEmploy = 0
    softMaxEmployArea = ""
    softMaxEmployAmount = 0

    for row in fileAnnualSingleFile:
        line = row.rstrip().split(",")
        # checks if fip is in areaTitlesDictionary
        if line[0] in areaTitlesDictionary:
            # all industries
            # `industry_code` is equal to `"10"` and `own_code` is equal to `"0"`
            if line[2] == "\"10\"" and line[1] == "\"0\"":
                # takes care of num areas
                numAreas += 1
                # takes care of gross annual wages
                grossAnnualWages += float(line[10])
                # takes care of maxAnnualWageArea and maxAnnualWageAmount
                if float(line[10]) > maxAnnualWageAmount:
                    maxAnnualWageArea = areaTitlesDictionary[line[0]]
                    maxAnnualWageAmount = float(line[10])
                # Takes care of totalEstabs
                totalEstab += float(line[8])
                # takes care of maxEstabArea and maxEstabAmount
                if float(line[8]) > maxEstabAmount:
                    maxEstabArea = areaTitlesDictionary[line[0]]
                    maxEstabAmount = float(line[8])
                # takes care of total employ
                totalEmploy += float(line[9])
                # takes care of maxEmployArea and maxEmployAmount
                if float(line[9]) > maxEmployAmount:
                    maxEmployArea = areaTitlesDictionary[line[0]]
                    maxEmployAmount = float(line[9])

            # Software industries
            # `industry_code` is equal to `"5112"` and `own_code` is equal to `"5"`
            elif line[2] == "\"5112\"" and line[1] == "\"5\"":
                # takes care of num areas
                softNumAreas += 1
                # takes care of gross annual wages
                softGrossAnnualWages += float(line[10])
                # takes care of maxAnnualWageArea and maxAnnualWageAmount
                if float(line[10]) > softMaxAnnualWageAmount:
                    softMaxAnnualWageArea = areaTitlesDictionary[line[0]]
                    softMaxAnnualWageAmount = float(line[10])
                # Takes care of totalEstabs
                softTotalEstab += float(line[8])
                # takes care of maxEstabArea and maxEstabAmount
                if float(line[8]) > softMaxEstabAmount:
                    softMaxEstabArea = areaTitlesDictionary[line[0]]
                    softMaxEstabAmount = float(line[8])
                # takes care of total employ
                softTotalEmploy += float(line[9])
                # takes care of maxEmployArea and maxEmployAmount
                if float(line[9]) > softMaxEmployAmount:
                    softMaxEmployArea = areaTitlesDictionary[line[0]]
                    softMaxEmployAmount = float(line[9])
    fileAnnualSingleFile.close()

    after = time.time()
    print(f"Done in {after - before:.3f} seconds!", file=sys.stderr)

    "Fill in the report for all industries"
    rpt.all.num_areas = numAreas
    rpt.all.total_annual_wages = int(grossAnnualWages)
    rpt.all.max_annual_wage = (maxAnnualWageArea.replace('"', ''), int(maxAnnualWageAmount))
    rpt.all.total_estab = int(totalEstab)
    rpt.all.max_estab = (maxEstabArea.replace('"', ''), int(maxEstabAmount))
    rpt.all.total_empl = int(totalEmploy)
    rpt.all.max_empl = (maxEmployArea.replace('"', ''), int(maxEmployAmount))

    "Fill in the report for the software publishing industry"
    rpt.soft.num_areas = softNumAreas
    rpt.soft.total_annual_wages = int(softGrossAnnualWages)
    rpt.soft.max_annual_wage = (softMaxAnnualWageArea.replace('"', ''), int(softMaxAnnualWageAmount))
    rpt.soft.total_estab = int(softTotalEstab)
    rpt.soft.max_estab = (softMaxEstabArea.replace('"', ''), int(softMaxEstabAmount))
    rpt.soft.total_empl = int(softTotalEmploy)
    rpt.soft.max_empl = (softMaxEmployArea.replace('"', ''), int(softMaxEmployAmount))

    # Print the completed report
    print(rpt)
