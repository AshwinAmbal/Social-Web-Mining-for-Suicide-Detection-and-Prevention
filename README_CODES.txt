This file contains details about all the codes that are used in the project:

Spyder Codes/DB_Creations_PostgreSQL/DB_Creation.py - To create the Schema required for carrying out SQL Operations

Spyder Codes/Comment_Details/Comment_Scraping_From_Reddit.py - Scraping Reddit thread for comments related to Suicides and storing them in the 			
																PostgreSQL DB

Spyder Codes/Comment_Details/Cleaning_Comments_With_Contractions.py - To preprocess and clean comments in sentence level with contractions, white 
																		space, pipe ('|') symbol, carriage returns. Line breaks are replaced with '[BK]' tags

Spyder Codes/User_Details/Get_User_Details_From_Reddit.py - Using username obtained from comments scraped to get user details of user who has 
															commented on the Reddit submission.

IPython Data Exploration Codes/Suicide Method Categorization/Statistics_from_DB.ipynb - Statistical Analysis of Reddit thread
																						Objective: Initial Analysis of the Submission and Comments of 
																									Reddit Thread

IPython Data Exploration Codes/Suicide Method Categorization/Initial_General_Statistics_Using_NLP.ipynb - Applying NLP Techniques to Assess Comments 
																											and Obtain Statistics
																											Objective :To write the required CSV 
																														files for future use and obtain Initial Sentence Level Statistics

IPython Data Exploration Codes/Suicide Method Categorization/Deep_Data_Exploration_for_Method_Categorization.ipynb - Applying NLP Techniques to Assess 
																										Comments and Extract Patterns/Statistics
																										Objective: To explore comments, extract 	
																													possible POS Tag patterns and create train and test set

IPython Data Exploration Codes/Suicide Method Categorization/Categorization_Comments_Methods.ipynb - To apply various Machine Learning Estimators 
																										with the One VS Rest Classifier 
																										Objective: To apply various Machine Learning 
																													Estimators with the One VS Rest Classifier 

IPython Data Exploration Codes/Suicide Method Categorization/CRF_Method_Categorization.ipynb - CRF used for Categorizing Sentences Based on Methods 
																								Used to commit Suicide
																								Objective: Applying CRF to Extract 
																											Patterns/Statistics in Sentences with Methods and Predicting Labels

IPython Data Exploration Codes/Risk Factor Extraction/Risk_Factor_Extraction.ipynb - Exploratory Analysis for finding relevant factors and Forming 	
																						dictionaries using Lexicons
																						Objective: Extracting Patterns to use to extract relevant 
																									Risk Factors
																						Note: Still under progress... Hence not fully documented and 
																								commented
																						Categories to classify based on the following link: https://afsp.org/about-suicide/risk-factors-and-warning-signs/
	