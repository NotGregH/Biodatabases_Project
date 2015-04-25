__author__ = 'greg'


# This is a series of functions
# to place the data into tab delimited
# csv files for easy insertion into
# the sqlite db.


################
# Modules
################

from csv import reader
from csv import writer
import argparse as argp

#################
# Functions
#################

def file_2_list(file_name):
    '''
    Converts a file with ' ' delimiters
     to a list of lists by line.
    :param file: The file to convert
    :return: A lists of lists by line
    '''
    f = reader(open(file_name,'rb'),delimiter=" ")
    file_list =[]
    for i in f:
        file_list.append(i)
    return file_list

def file_2_list_2(file_name):
    '''
    Converts a file with '\t' delimiters
     to a list of lists by line.
    :param file: The file to convert
    :return: A lists of lists by line
    '''
    f = reader(open(file_name,'rb'),delimiter="\t")
    file_list =[]
    for i in f:
        file_list.append(i)
    return file_list

def create_gene_csv(file_list):
    '''
    Turns the raw File_list from
    shoot_exp data into a tab delim csv
    where the first column is an id and
    the second is the gene name.
    '''
    file_list = file_list[1:]
    genes = []
    for i in file_list:
        genes.append(i[0])
    genes_id = list(xrange(len(genes)))
    genes_w_id = zip(genes_id,genes)
    with open('genes.csv','wb') as f:
        write = writer(f,delimiter='\t')
        write.writerows(genes_w_id)
        f.close()
    return

def create_conditions_csv(file_list):
    '''
    Turns the raw File_list from
    shoot_exp data into a tab delim csv
    where the first column is an id and
    the second is the condition name.
    '''
    conditions = file_list[0][1:]
    con_ids = list(xrange(len(conditions)))
    con_w_id = zip(con_ids,conditions)
    with open('conditions.csv','wb') as f:
        write = writer(f,delimiter='\t')
        write.writerows(con_w_id)
        f.close()
    return

def create_biomass_csv(file_list):
    '''
    Turns the raw File_list from
    biomass table data into a tab delim csv
    where the first column is the con_id and
    the second is the biomass.
    '''
    file_list = file_list[1:]
    biomass = []
    for i in file_list:
        biomass.append((i[0],i[4]))
    with open('biomass.csv','wb') as f:
        write = writer(f,delimiter='\t')
        write.writerows(biomass)
        f.close()
    return

def create_mean_expression_csv(mean_exp_list):
    '''
    Creates a tab delim csv file from the mean counts data.
    Columns correspond to the following, Gene_id, Con_id, Rep_id, Expression.
    '''
    mean_exp_list = mean_exp_list[1:]
    mean_counts = []
    for i in mean_exp_list:
        mean_counts.append(i[1:])
    gene_ids = list(xrange(len(mean_exp_list)))
    mean_counts_w_id = zip(gene_ids,mean_counts)
    con_ids = list(xrange(24))
    out_list = []
    for i in con_ids:
        for j in mean_counts_w_id:
            out_list.append((j[0],i,0,j[1][i]))
    with open('mean_counts.csv','wb') as f:
        write = writer(f,delimiter='\t')
        write.writerows(out_list)
        f.close()
    return

def create_rep_exp_csv(rep_exp_list):
    '''
    Creates a tab delim csv file from the replicant counts data.
    Columns correspond to the following, Gene_id, Con_id, Rep_id, Expression.
    '''
    counts = []
    rep_exp_list = rep_exp_list[1:]
    for i in rep_exp_list:
        counts.append(i[1:])
    gene_ids = list(xrange(len(counts)))
    counts_w_ids = zip(gene_ids, counts)
    rep_ids = [1, 2, 3]*24
    con_id_col = [0, 0, 0, 18, 18, 18, 1, 1, 1, 19, 19, 19, 2, 2, 2, 20, 20, 20, 3, 3, 3, 21, 21, 21,
                  4, 4, 4, 22, 22, 22, 5, 5, 5, 23, 23, 23, 6, 6, 6, 12, 12, 12, 7, 7, 7,
                  13, 13, 13, 8, 8, 8, 14, 14, 14, 9, 9, 9, 15, 15, 15, 10, 10, 10, 16, 16,
                  16, 11, 11, 11, 17, 17, 17]
    col_num = list(xrange(72))
    con_w_col = zip(col_num,con_id_col)
    con_w_col = zip(con_w_col,rep_ids)
    col_id_list = []
    for i in con_w_col:
        col_id_list.append([list(i[0]),i[1]])
    all_counts = []
    for x in col_id_list:
        for i in counts_w_ids:
            all_counts.append((i[0],x[0][1],x[1],i[1][x[0][0]]))
    with open('rep_counts.csv','wb') as f:
        write = writer(f,delimiter='\t')
        write.writerows(all_counts)
        f.close()
    return

def main(mean_exp_file,rep_file,biomass_file):
    rep_exp_list = file_2_list(rep_file)
    biomass_list = file_2_list_2(biomass_file)
    mean_exp_list = file_2_list_2(mean_exp_file)
    create_conditions_csv(mean_exp_list)
    create_gene_csv(mean_exp_list)
    create_biomass_csv(biomass_list)
    create_mean_expression_csv(mean_exp_list)
    create_rep_exp_csv(rep_exp_list)
    return

#######################################


if __name__== '__main__':
    parser = argp.ArgumentParser()
    parser.add_argument("-r","--repexp",help="Rep Exp file")
    parser.add_argument("-m","--meanexp",help="Mean Exp File")
    parser.add_argument("-b","--biomass",help="Biomass File")
    args = parser.parse_args()
    main(args.meanexp,args.repexp,args.biomass)
