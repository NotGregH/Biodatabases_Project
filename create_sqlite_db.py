__author__ = 'greg'


# Simple set of functions to create the sqlite3
# database.

################
# Modules
################

import sqlite3 as sql

################
# Functions
################


def create_gene_table():
    '''
    creates a table for storing Gene ids.
    '''
    con = sql.connect('Project.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE Genes"
                "(Gene_id int(20) PRIMARY KEY,"
                "Gene_Name varchar(255))")
    con.commit()
    con.execute('pragma foreign_keys') # enables foreign keys
    con.commit()
    return con.close()

def create_conditions_table():
    '''
    Creates a table for storing condition ids.
    '''
    con = sql.connect('Project.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE Conditions"
                "(Con_id int(20) PRIMARY KEY,"
                "Condition_Name varchar(255))")
    con.commit()
    return con.close()

def create_biomass_table():
    '''
    Creates a table for storing biomass data.
    '''
    con = sql.connect('Project.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE Biomass"
                "(ID INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT NULL,"
                "Con_id int(20),"
                "Biomass num(20),"
                "FOREIGN KEY (Con_id) REFERENCES Conditions (Con_id))")
    con.commit()
    return con.close()

def create_experiment_table():
    '''
    Creates a table for storing replicate/experiment ids.
    '''
    con = sql.connect('Project.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE Experiment"
                "(Rep_id int(2) PRIMARY KEY,"
                "Rep_name varchar(10))")
    con.commit()
    return con.close()


def create_expression_table():
    '''
    Creates a data for storing expression data.
    '''
    con = sql.connect('Project.db')
    cur = con.cursor()
    cur.execute("CREATE TABLE Expression"
                "(ID INTEGER PRIMARY KEY AUTOINCREMENT DEFAULT NULL,"
                "Gene_id int(20),"
                "Con_id int(20),"
                "Rep_id varchar(2),"
                "Expression int(20),"
                "FOREIGN KEY (Con_id) REFERENCES Conditions (Con_id),"
                "FOREIGN KEY (Gene_id) REFERENCES Genes (Gene_id),"
                "FOREIGN KEY (Rep_id) REFERENCES Experiment (Rep_id))")
    con.commit()
    return con.close()


def create_data_tables():
    con = sql.connect('Project.db')
    cur = con.cursor()
    return


def main():
    create_gene_table()
    create_conditions_table()
    create_biomass_table()
    create_experiment_table()
    create_expression_table()
    return

#######################################

if __name__ == '__main__':
    main()




