__author__ = 'greg'

'''
Set of tools for pulling Expression data
and Biomass data from the database by
Condition Id.  It puts the data into
tab delimited csv files so they can be easily
read into your favorite analysis tools!
'''

###################
# Modules
###################

import sqlite3 as sql
from csv import writer
import argparse as argp

####################
# Functions
####################

def expression_data_by_con(con_id, exp_out):
    '''
    Pulls Expression Data by condition ID from Project.db into
    a tab delimited CSV file.
    :param con_id: The ID for the condition you'd like to pull.
    :param exp_out: Name of the desired output file.
    :return: Tab delimited file with the following columns Gene_Name, Condition_Name, Rep_Name,
    and Expression_Count
    '''
    con = sql.connect('Project.db')
    cur = con.cursor()
    cur.execute("select Gene_name,Condition_Name,Rep_name,Expression FROM "
                "Expression, Conditions, Genes, Experiment "
                "WHERE Expression.Con_id=Conditions.Con_id AND Expression.Con_id=? "
                "AND Expression.Gene_id=Genes.Gene_id AND Expression.Rep_id=Experiment.Rep_id", (con_id,))
    query_data = [[str(item) for item in results] for results in cur.fetchall()]
    con.close()
    title = ['Gene_Name', 'Condition_Name', 'Rep_name', 'Expression_Count']
    query_data.insert(0,title)
    with open(exp_out, 'wb') as f:
        write = writer(f, delimiter='\t')
        write.writerows(query_data)
        f.close()
    return


def biomass_by_con(con_id,biomass_out):
    '''
    Pulls Biomass data from Project.db by Condition ID into a tab delimited
    CSV File.
    :param con_id: The ID for the condition you'd like to pull
    :param biomass_out: Name of the output file
    :return: Tab delimited file with Condition_name in the first column
    and Biomass in the second column.
    '''
    con = sql.connect('Project.db')
    cur = con.cursor()
    cur.execute("select Condition_Name, Biomass FROM Biomass, Conditions "
                "WHERE Biomass.Con_id = Conditions.Con_id AND Biomass.Con_id=?", (con_id,))
    query_data = [[str(item) for item in results] for results in cur.fetchall()]
    con.close()
    title = ['Condition_Name', 'Biomass(g)']
    query_data.insert(0, title)
    with open(biomass_out, 'wb') as f:
        write = writer(f, delimiter='\t')
        write.writerows(query_data)
        f.close()
    return

def main(biomass_out, exp_out, con_id):
    biomass_by_con(con_id, biomass_out)
    expression_data_by_con(con_id, exp_out)
    return


#######################

if __name__ == '__main__':
    parser = argp.ArgumentParser()
    parser.add_argument("-b", "--biomassout", help="Name of the biomass output file")
    parser.add_argument("-e", "--expout", help="Name of the expression output file")
    parser.add_argument("-c", "--conid", help="The condition ID you'd like to pull")
    arg = parser.parse_args()
    main(arg.biomassout, arg.expout, arg.conid)
