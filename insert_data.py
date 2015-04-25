_author__ = 'greg'

# Set of functions for inserting
# data from tab delimited csv/txt
# files into the project database.


##################
# Modules
##################

import argparse as argp
import sqlite3 as sql
from csv import reader

##################
# Functions
##################

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

def insert_2_gene(gene_file_list):
    '''
    For inserting a list of genes into the
    genes table.
    '''
    con = sql.connect('Project.db')
    cur = con.cursor()
    cur.executemany("INSERT INTO Genes VALUES (?,?)", gene_file_list)
    con.commit()
    return con.close()

def insert_2_experiment(experiment_file_list):
    '''
    For inserting experiment/replicate data
    into the Experiment table.
    '''
    con = sql.connect('Project.db')
    cur = con.cursor()
    cur.executemany("INSERT INTO Experiment "
                    "VALUES (?,?)", experiment_file_list)
    con.commit()
    return con.close()

def insert_2_biomass(biomass_file_list):
    '''
    For inserting biomass data
    into the biomass table.
    '''
    con = sql.connect('Project.db')
    cur = con.cursor()
    cur.executemany("INSERT INTO Biomass "
                    "VALUES (NULL,?,?)", biomass_file_list)
    con.commit()
    return con.close()

def insert_2_conditions(conditions_file_list):
    '''
    For inserting conditions data into
    the conditions table.
    '''
    con = sql.connect('Project.db')
    cur = con.cursor()
    cur.executemany("INSERT INTO Conditions VALUES (?,?)", conditions_file_list)
    con.commit()
    return con.close()

def insert_2_expression(exp_file_list):
    '''
    For inserting expression data into
    the expression table.
    '''
    con = sql.connect('Project.db')
    cur = con.cursor()
    cur.executemany("INSERT INTO Expression VALUES(NULL, ?, ?, ?, ?)", exp_file_list)
    con.commit()
    return con.close()

def main(rep_file, mean_file, biomass_file, con_file, exp_file, gene_file):
    rep = file_2_list_2(rep_file)
    mean = file_2_list_2(mean_file)
    gene = file_2_list_2(gene_file)
    biomass = file_2_list_2(biomass_file)
    con = file_2_list_2(con_file)
    exp = file_2_list_2(exp_file)
    insert_2_gene(gene)
    insert_2_conditions(con)
    insert_2_experiment(exp)
    insert_2_biomass(biomass)
    insert_2_expression(mean)
    insert_2_expression(rep)
    return

##########################

if __name__ == '__main__':
    parser = argp.ArgumentParser()
    parser.add_argument("-g","--genefile",help="Tab-delim gene file")
    parser.add_argument("-c","--confile",help="Tab delim conditions file")
    parser.add_argument("-e","--expfile",help="Tab delim exp id file")
    parser.add_argument("-b",'--biomassfile',help='Tab delim biomass file')
    parser.add_argument("-m",'--meanexpfile',help='Tab delim mean expression file')
    parser.add_argument('-r','--repexpfile',help='Tab delim rep expression file')
    arg = parser.parse_args()
    main(arg.repexpfile, arg.meanexpfile, arg.biomassfile, arg.confile,
         arg.expfile, arg.genefile)
