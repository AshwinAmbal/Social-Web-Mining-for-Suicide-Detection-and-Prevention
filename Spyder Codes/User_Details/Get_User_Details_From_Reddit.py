"""
Objective: Using username, scraping user details from Reddit
Packages used:
PRAW: 'Python Reddit API Wrapper'- Used for Scraping packages
psycopg2: Package to connect and use postgresql server with python
"""
import praw
import psycopg2
#DB Connection code
conn=psycopg2.connect("dbname=Reddit_Suicide user=postgres password='madgab@1'")
cur= conn.cursor()
cur1=conn.cursor()
#Connecting to Reddit Bot/App 
reddit = praw.Reddit(client_id='create_your_app',
                     client_secret='get_your_secret_client_code',
                     user_agent='get_your_user_agent',
                     username='create_your_account',
                     password='create_your_password') 
submission = reddit.submission(id='4e8oip') #Getting the required submission
# We use userID as integer numbers for authors who do not have a user id in reddit so that
# we can uniquely identify their information later on... The below two lines get the highest 
# integer number assigned till now and assign the next possible integer number to the next author 
# who appears without a username 
cur.execute("""SELECT MAX(cast(userid as Int)) FROM About 
            where date_created=-1 or date_created IS NULL;""")   
                                
i=cur.fetchone()[0]
# For first time execution there won't be any such numbers
if i is None:
    i=0
q=0
#Retrieving from Comments table and Filling the About table
cur.execute("""SELECT distinct author FROM Comments WHERE author NOT IN 
            (Select username FROM About);""")
while 1: 
    username=cur.fetchone()
    if username is None:
        break
    i=i+1
    try:
        redditor1 = reddit.redditor(username[0])
        if redditor1 is None : 
            continue
        elif hasattr(redditor1,"is_suspended") :
            if redditor1.is_suspended == "True":
                #Suspended users
                v1=i
                cur1.execute("""INSERT INTO About VALUES(%s,%s,NULL,NULL,NULL);""",
                             (v1,username[0]))          #Flag is set to NULL for Suspended Users
                q=q+1
                conn.commit()
                continue
            else:
                #Normal users who have is_suspended attribute set to false
                v1=redditor1.id
                v3=redditor1.comment_karma
                v4=redditor1.link_karma
                v5=redditor1.created_utc
                cur1.execute("""INSERT INTO About VALUES(%s,%s,%s,%s,%s);""",
                         (v1,username[0],v3,v4,v5))     
                q=q+1
                conn.commit()
                continue
        else:
            #Users without the is_suspended attribute
            v1=redditor1.id
            v3=redditor1.comment_karma
            v4=redditor1.link_karma
            v5=redditor1.created_utc
            cur1.execute("""INSERT INTO About VALUES(%s,%s,%s,%s,%s);""",
                         (v1,username[0],v3,v4,v5))
            q=q+1
            conn.commit()
    except :
        #Userid's which raise exceptions
        v1=i
        cur1.execute("""INSERT INTO About VALUES(%s,%s,NULL,NULL,-1);""",
                     (v1,username[0]))  #Flag is set to -1 for userid's raising exceptions
        q=q+1
        conn.commit()
        continue
#Closing statements
print("INSERTED: ",q)
cur1.close()
cur.close()
conn.close()