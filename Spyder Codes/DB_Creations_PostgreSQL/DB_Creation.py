"""
Objective: To create the Schema required for carrying out SQL Operations
Packages used:
psycopg2 - Used to connect to Postgresql
"""

import psycopg2

conn=psycopg2.connect("dbname=Reddit_Suicide user=postgres password='madgab@1'")
cur= conn.cursor()

#Create Table for Users
cur.execute("""CREATE TABLE About
            (Userid VARCHAR(8),
            Username VARCHAR(25),
            com_upvote DECIMAL,              
            sub_upvote DECIMAL,
            Date_created INTEGER,
            PRIMARY KEY(Userid)
            );""")

#Create table for Comments
cur.execute("""CREATE TABLE Comments
            (Com_Id VARCHAR(8),
            Author VARCHAR(25),
            Content TEXT,
            Dated INTEGER,
            link_id VARCHAR(13),
            Score DECIMAL,
            Likes VARCHAR(5),
            Distinguished VARCHAR(5),
            Down DECIMAL,
            Depth DECIMAL,
            Controversy DECIMAL,
            Archived CHAR(7),
            Gilded DECIMAL,
            Flag CHAR(6),
            removal_reason TEXT,
            edited INTEGER,
            upvote INTEGER,
            author_flair_text VARCHAR(20),
            author_flair_css_class VARCHAR(20),
            PRIMARY KEY(Com_Id)
            );""")

#Create table for Submission
cur.execute("""CREATE TABLE Submission
            (Sub_Id VARCHAR(8),
            Title TEXT,
            Author_name VARCHAR(25),
            Created INTEGER,
            URL TEXT,
            Perma TEXT,
            Gilded DECIMAL,
            Downs DECIMAL,
            upvote DECIMAL,
            upvote_ratio REAL,
            Numberofcomments DECIMAL,
            Score DECIMAL,
            Over18 CHAR(6),
            is_self CHAR(6),
            PRIMARY KEY(Sub_Id)
            );""")

#Create table for the Relation between Comments
cur.execute("""CREATE TABLE Related
            (Comdad_Id VARCHAR(8),
            Comson_Id VARCHAR(8)
            );""")

conn.commit()
cur.close()
conn.close()