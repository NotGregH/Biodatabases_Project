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

####################
# Functions
####################

def expression_data_by_con(con_id,exp_out):
    con = sql.connect('Project.db')
    cur = con.cursor()
    cur.execute()
    cur.commit()
    query_data = cur.fetchall()
    con.close()
    with open(exp_out, 'wb') as f:
        write = writer(f,delimiter='\t')
        write.writerows(query_data)
        f.close()
    return


def biomass_by_con(con_id,biomass_out):
    con = sql.connect('Project.db')
    cur = con.cursor()
    cur.execute()
    cur.commit()
    query_data = cur.fetchall()
    con.close()
    with open(biomass_out, 'wb') as f:
        write = writer(f,delimiter='\t')
        write.writerows(query_data)
        f.close()
    return

def main():
    return


#######################

if __name__ == '__main__':
    print "In Progress"
