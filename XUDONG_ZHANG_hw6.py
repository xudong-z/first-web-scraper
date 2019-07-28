import argparse

from source1 import *
from source2 import *
from source3 import *

from local_computation import *
from remote_computation import *


# -help for description
parser = argparse.ArgumentParser(description = "This program is for you to extract the information about Academy Awarded films")
parser.add_argument("source_type", type=str, help = "Input the source: 'remote' or 'local'")
parser.add_argument("--source", type=int, help ="Input an integer for Source: 1/2/3!")
parser.add_argument("--nfilm", type=int, help = "Any integer between 0-170")

# below is the code to avoid wrong input format
if __name__=='__main__':

    nfilm = 5 # by default, nfilm = 20

    args = parser.parse_args()
    source_type = args.source_type
    source = args.source

    if args.nfilm:
        nfilm = args.nfilm

    # to regulate the nfilm should be lower than 170
    if int(nfilm) > 170 or int(nfilm) < 0:  # the number should be within 0 and 308
        print("--Please input an integer (from 0 to 170)!")
    else:
        if source_type == 'local':
            if source: # if specify the sub-source 1/2/3
                if source == 1:
                    source1 = pd.read_csv("local_data/local_source1.csv")
                    print(source1.head(nfilm))
                elif source == 2:
                    source2 = pd.read_csv("local_data/local_source2.csv")
                    print(source2.head(nfilm))
                elif source == 3:
                    source3 = pd.read_csv("local_data/local_source3.csv", encoding='latin-1') # encoding, to avoid encoding exceptions
                    print(source3.head(nfilm))
            else: # if not specify the sub-source 1/2/3, it will give the aggregated results
                print('*** Outputing local data ***')
                print("--Intro: For films that have won more than 2 awards,\n below is the table that contains information of their awards latest news\n")
                # process the data that has been store in local_data folder
                local_computation(nfilm)

        elif source_type == 'remote':
            if source: # if specify the sub-source 1/2/3
                if source == 1:
                    source1(nfilm)
                    source1 = pd.read_csv("remote_data/remote_source1.csv")
                    print(source1)
                elif source == 2:
                    source1(nfilm)
                    source2()
                    source2 = pd.read_csv("remote_data/remote_source2.csv")
                    print(source2)
                elif source == 3:
                    source1(nfilm)
                    source3()
                    source3 = pd.read_csv("remote_data/remote_source3.csv")
                    print(source3)
            else: # if not specify the sub-source 1/2/3, it will give the aggregated results
                print('*** Outputing remote data ***')
                print("--Intro: For films that have won more than 2 awards,\n below is the table that contains information of their awards latest news")
                # source1() is to extract information about films Academy awards and nominations
                source1(nfilm)
                # source2() is to extract information about films Academy awards and nominations, inheriting the length of above source1
                source2()
                # source3() is to extract information about films Academy awards and nominations, inheriting the length of above source1
                source3()
                remote_computation()
        else:
            print('--Please input a correct source code (remote/local)')
