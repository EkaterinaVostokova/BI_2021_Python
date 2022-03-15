#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv
import sqlite3


# In[2]:


connection = sqlite3.connect('genetics_data_new.db')
# creating new database or connecting to it

# Opening both CSV files, selecting data
# In[31]:


with open('genstudio.csv', 'r') as f:
    file = csv.DictReader(f)
    to_db = [(i['SNP Name'], i['SNP Index'], i["SNP Aux"], i["Sample ID"], i["SNP"], i["Allele1 - Top"],
            i["Allele2 - Top"], i["Allele1 - Forward"], i["Allele2 - Forward"], i["Allele1 - AB"], 
            i["Allele2 - AB"], i["Chr"], i["Position"], i["GC Score"], i["GT Score"], i["Theta"], i["R"],
            i["B Allele Freq"], i["Log R Ratio"]) for i in file]


# In[44]:


with open('metadata.csv', 'r') as f1:
    file1 = csv.DictReader(f1)
    to_db1 = [(j["dna_chip_id"], j["breed"], j["sex"]) for j in file1]


# Creating two tables - one for genstudio file, another for metadata

# In[40]:


query_genetics = '''CREATE TABLE genes_4(
                            gen_id INTEGER PRIMARY KEY,
                            SNP_name TEXT,
                            SNP_index INTEGER,
                            SNP_Aux INTEGER,
                            Sample_ID TEXT,
                            SNP TEXT,
                            Allele1_Top TEXT,
                            Allele2_Top TEXT,
                            Allele1_Forward TEXT,
                            Allele2_Forward TEXT,
                            Allele1_AB TEXT,
                            Allele2_AB TEXT,
                            Chr TEXT,
                            Position TEXT,
                            GC_Score REAL,
                            GT_Score REAL,
                            Theta REAL,
                            R REAL,
                            B_Allele_Freq REAL,
                            Log_R_Ratio REAL
                            )'''

# In[ ]:


connection.execute(query_genetics)


# In[ ]:


query_meta = '''CREATE TABLE meta(
                            gen_id INTEGER PRIMARY KEY,
                            dna_chip_id TEXT,
                            breed TEXT,
                            sex TEXT)'''


# In[ ]:


connection.execute(query_meta)


# Inserting data into the tables

# In[39]:


connection.executemany('''INSERT INTO genes_4 ('SNP_Name', 'SNP_Index', 'SNP_Aux', 'Sample_ID', 'SNP', 'Allele1_Top',
    'Allele2_Top', 'Allele1_Forward','Allele2_Forward','Allele1_AB','Allele2_AB','Chr', 'Position', 'GC_Score','GT_Score',
    'Theta','R','B_Allele_Freq','Log_R_Ratio')
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);''', to_db)


# In[41]:


connection.commit()


# In[32]:


connection.executemany("INSERT INTO meta ('dna_chip_id', 'breed', 'sex') VALUES (?, ?, ?);", to_db1)


# In[35]:


connection.commit()


# Joining data on dna chip id and presenting SNP name and Chromosome number

# In[38]:


select_query = '''SELECT SNP_name, Chr FROM genes_4
                JOIN meta ON genes_4.Sample_ID = meta.dna_chip_id'''

result = connection.execute(select_query).fetchall()


# In[ ]:


connection.close()
