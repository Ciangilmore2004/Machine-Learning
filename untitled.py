import pandas as ps
import matplotlib.pyplot as pp
import csv
with open('"C:\\Users\\cians\\Downloads\\box_office\\boxofficemojointernationaltop1000.tsv"', 'r') as file:
    tsv_reader = csv.reader(file, delimiter=