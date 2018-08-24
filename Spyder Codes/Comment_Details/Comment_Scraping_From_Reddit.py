"""
Objective: Scraping Reddit thread for comments related to Suicides 
Packages used:
PRAW: 'Python Reddit API Wrapper'- Used for Scraping packages
psycopg2: Package to connect and use postgresql server with python
The Comments Table contains all the comments extracted from the Reddit Submission
The Related Table contains all the comment id's of comments related to each other as parent and child 
"""
import praw
import psycopg2
#DB Connection code
conn=psycopg2.connect("dbname=Reddit_Suicide user=postgres password='madgab@1'")
cur= conn.cursor()
cur1= conn.cursor()
#Connecting to Reddit Bot/App 
reddit = praw.Reddit(client_id='create_your_app',
                     client_secret='get_your_secret_client_code',
                     user_agent='get_your_user_agent',
                     username='create_your_account',
                     password='create_your_password') 
submission = reddit.submission(id='4e8oip')  #Getting the required submission
submission.comment_sort = 'best'     #Sorting of comment (Best,Top,Gilded,New,Rising,Controversial,Hot,Old,Q&A)
submission.comments.replace_more(limit = None)
#replace_more(limit,threshold(default=0))
#Limit: Maximum number of More Comments to replace
#threshold: Mimumum number of comments in a More Comments button to replace it 
#to replace 'More Comment' buttons in page  
comment_queue = submission.comments[:]
i=0
y=0
#Queue follows FIFO, Therefore we get Top, Second, Third, etc.... level comments in that order

while comment_queue :
        comment = comment_queue.pop(0)
        comment_queue.extend(comment.replies)
        if hasattr(comment,"id") :
            v1=comment.id
        else:
            v1=i
        #Check if Comment already exists in the Comments table
        cur.execute("""SELECT Com_id FROM Comments WHERE Com_Id=%s;""",
                          [comment.id])
        p=cur.fetchall()
        if p : 
#            if hasattr(comment,"author_flair_text") :
#                cur1.execute("""UPDATE Comments SET author_flair_text=%s where Com_Id=%s;""",
#                         (comment.author_flair_text,comment.id))
#            if hasattr(comment,"author_flair_css_class") :
#                    cur1.execute("""UPDATE Comments SET author_flair_css_class=%s where Com_Id=%s;""",
#                                 (comment.author_flair_css_class,comment.id))
            conn.commit()
            i=i+1
        else:
            if comment.author is None :
                v2="None"
            else :
                v2=comment.author.name
            v3=comment.body
            v4=comment.created_utc
            v5=comment.link_id
            v6=comment.score
            v7=comment.likes
            v8=comment.distinguished
            v9=comment.downs
            v10=comment.depth
            v11=comment.controversiality
            v12=comment.archived
            v13=comment.gilded
            v15=comment.removal_reason
            if comment.edited == False:
               v16=None
            else:
                v16=comment.edited
            v17 = comment.ups
            v18 = comment.author_flair_text
            v19 = comment.author_flair_css_class
            if '4e8oip' in comment.parent_id :      #All top level comments have parent as 4e8oip 
                v14="True"                          #All top level comments are marked with Flag = True
                cur.execute("""INSERT INTO Comments VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""",
                            (v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19))
            else :
                v14="False"
                cur.execute("""INSERT INTO Comments VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""",
                            (v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19))
                if hasattr(comment,"parent_id"):
                    q=comment.parent_id
                    q=q[3:]     #Removing first 3 characters
                else:
                    q=None   
                cur.execute("""INSERT INTO Related VALUES(%s,%s);""",    
                                (q,comment.id))      #Inserting all the Comments related to each other as Parent and Child
            conn.commit()
            y=y+1
print("INSERTED: ",y)
cur.close()
cur1.close()
conn.close()
        
 