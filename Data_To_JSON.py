__author__ = 'greg'

# Purpose: To convert the data files into JSON
# 1. Read file into a list
# 2. Create Json files from each file



############
# Modules
############

import json
from csv import reader
from collections import OrderedDict

################
# Functions
################

def file_2_list(file):
    '''
    Converts a file with ' ' delimiters
     to a list of lists by line.
    :param file: The file to convert
    :return: A lists of lists by line
    '''
    f = reader(open(file,'rb'),delimiter=" ")
    file_list =[]
    for i in f:
        file_list.append(i)
    return file_list

def file_2_list_2(file):
    '''
    Converts a file with '\t' delimiters
     to a list of lists by line.
    :param file: The file to convert
    :return: A lists of lists by line
    '''
    f = reader(open(file,'rb'),delimiter="\t")
    file_list =[]
    for i in f:
        file_list.append(i)
    return file_list

def create_gene_json(file_list):
    '''

    :param file_list:
    :return:
    '''
    genes = []
    file_list = file_list[1:]
    for i in file_list:
        genes.append(("Gene_Name",i[0]))
    gene_ids = list(xrange(genes))
    gene_ids_2 = []
    for i in gene_ids:
        gene_ids_2.append(("Gene_ID",i))
    genes_w_id = zip(gene_ids_2,genes)
    out_list = []
    for i in genes_w_id:
        file_dict = OrderedDict()
        file_dict = OrderedDict(i)
        out_list.append(file_dict)
    fout = open('genes_w_id.json','w')
    json.dump(out_list,fout)
    return fout.close()

def create_nutri_json(file_list):
    '''
    :param file_list:
    :return:
    '''
    nutrient = []
    file_list = file_list[0][1:]
    for i in file_list:
        nutrient.append(("Nutr_Name",i))
    nutr_ids = list(xrange(nutrient))
    nutr_ids_2 = []
    for i in nutr_ids:
        nutr_ids_2.append(("Nutr_ID",i))
    nutr_w_id = zip(nutr_ids_2,nutrient)
    out_list = []
    for i in nutr_w_id:
        file_dict = OrderedDict()
        file_dict = OrderedDict(i)
        out_list.append(file_dict)
    fout = open('nutrient.json','w')
    json.dump(out_list,fout)
    return fout.close()

def mean_count_json(mean_list):
    '''
    Creates a JSON from the mean counts file
    :Param mean_list : List of the Mean expression Data
    :return: JSON tagged File
    '''
    nutr_id = list(xrange(len(mean_list[0][1:])))
    gene_id = list(xrange(len(mean_list[1:])))
    mean_list = mean_list[1:]
    new_mean_list = []
    Out_list = []
    return

def biomass_JSON(file_list):
    '''
    :param file_list:
    :return:
    '''
    nutr_id = list(xrange(24))
    ids = []
    for i in nutr_id:
        ids.append([i,i,i,i,i,i,i,i,i,i])
    nutr_id = []
    for i in ids:
        for j in i:
            nutr_id.append(("Nutr_ID",j))
    biomass = []
    for i in file_list:
        biomass.append(("Biomass",i[3]))
    biomass_w_ID = zip(nutr_id,biomass)
    out_list =[]
    for i in biomass_w_ID:
        file_dict = OrderedDict(i)
        out_list.append(file_dict)
    fout = open('biomass.json','w')
    json.dump(out_list,fout)
    return fout.close()

def rep_count_json(rep_list):
    return

################
################

if __name__ == '__main__':
    print 'hello'
