import argparse
import os
import pandas as pd
import numpy as np

# Takes input and output directories as arguments
parser=argparse.ArgumentParser()
parser.add_argument('--input', default=".", help='The file path of the unzipped Grounded Emotions dataset')
parser.add_argument('--output', default="./data", help='The file path of the output dataset')

args = parser.parse_args()
INPUT_PATH = args.input
OUTPUT_PATH = args.output

datatypes = ["train", "test", "dev"]

for datatype in datatypes:
    if datatype == "train":
        file_prefix = ""
    else:
        file_prefix = "2018-"
    
    anger = pd.read_csv(INPUT_PATH +"/"+file_prefix+"EI-reg-En-anger-"+datatype+".txt", sep="\t", encoding="utf-8")
    fear = pd.read_csv(INPUT_PATH +"/"+file_prefix+"EI-reg-En-fear-"+datatype+".txt", sep="\t", encoding="utf-8")
    joy = pd.read_csv(INPUT_PATH +"/"+file_prefix+"EI-reg-En-joy-"+datatype+".txt", sep="\t", encoding="utf-8")
    sadness = pd.read_csv(INPUT_PATH +"/"+file_prefix+"EI-reg-En-sadness-"+datatype+".txt", sep="\t", encoding="utf-8")
    
    semeval2018task1 = anger.append(fear).append(joy).append(sadness).reset_index(drop=True)
    
    semeval2018task1.to_csv(OUTPUT_PATH+"/"+datatype+".tsv", sep='\t', encoding="utf-8")