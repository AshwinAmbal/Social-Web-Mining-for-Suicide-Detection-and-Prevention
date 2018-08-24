This file contains details about all the resources that are used in the project:

Line Breaks in the Original Comments are signified by "[BK]"
Separators used are '|' except for files with '*'

Resources/All_Comment_Details.csv - It is the CSV File written from the PostgreSQL Database with all the comments. 
									First line has heading.
									It contains all the comments scraped from the Reddit thread.

Resources/All_Comments_Without_Removed.csv - It is the CSV File written by the Python Code in Cleaning_Comments_With_Contractions.py. 
												First Line has heading.
												It contains all the cleaned comments and without those with the tags '[removed]' or '[deleted]'

Resources/Top_Level_Comment_Without_Removed.csv - It is the CSV File written by the Python Code in Cleaning_Comments_With_Contractions.py. 
													First Line has heading.
													It contains only the top level comments in the thread without those which have the tag '[removed]' or '[deleted]'
										
Resources/Sentence_Comment.csv - It is the CSV File written by the IPython Code in Initial General Statistics Using NLP.ipynb.
									It contains all the sentences and their respective comment ID's and sentence index number as in the order of appearance while reading.

Resources/Sentence_Without_BK - It is the CSV File written by the IPython Code in Initial General Statistics Using NLP.ipynb.
								It contains all the sentences without '[BK]' and their index number as in the order of appearance while reading
						
Resources/Sentence_Original - It is the CSV File written by the IPython Code in Initial General Statistics Using NLP.ipynb.
								It contains all the sentences and their index number as in the order of appearance while reading
						
Resources/Top_Comments_Content_Alone.csv - It is the CSV File written by the IPython Code in Initial General Statistics Using NLP.ipynb.
											It contains all the content of the comments alone without its attributes.
									
Resources/Method_Pre_Defined.csv - It is the CSV File that was created previously for a paper written by Bilel, Sandra and Jerome.
									It is used in the IPython Code in Initial General Statistics Using NLP.ipynb.
							
Resources/MethodSyn.csv - It is the CSV File written by the IPython Code in Deep Data Exploration for Method Categorization.ipynb.
							It contains all the Methods and the synonyms in the same line after querying the Advanse API. 
							All related words are in this file.
			
Resources/*Final_Methods.csv - It is the CSV File written by the IPython Code in Deep Data Exploration for Method Categorization.ipynb. 
								It contains all the filtered and distinct methods after careful processing of each method.
								Note: This file has a '\n' delimiter.
								Note: All methods have been found from the Synonym finder and filtered for relevance manually.
					
Resources/FAnnotationsforSent.csv - It is the CSV File written by the IPython Code in Deep Data Exploration for Method Categorization.ipynb.
									It contains the Sentences along with the Annotations of Sentences.
							
Resources/FAnnotations.csv - It is the CSV File written by the IPython Code in Deep Data Exploration for Method Categorization.ipynb.
								It contains the Comments along with the Annotations of Sentences.
							
Resources/Test_Data.csv - It is the CSV File written by the IPython Code in Deep Data Exploration for Method Categorization.ipynb.
							It contains all the Comments that have not been annotated.
							It is the test set for Machine Learning
							
Resources/Manual_Annotations_Sent.csv - It is a CSV File in which all the sentences were first obtained from FAnnotationsforSent.csv and then the 	
										sentence annotations were corrected and manually annotated.
										For sentences which have more than one annotation, the sentences are repeated so that each sentence has only one annotation.
							  
Resources/Dictionary_Map.csv - It is the CSV File written initially by CRF_Method_Categorization.ipynp . The mapping was refined multiple times 
								before the final version and so the code has been split up across files and is not mentioned in a single unit.
								It is the CSV File which contains all the methods in Final_Methods mapped to the different types of annotations that we have.
								It is used in Deep Data Exploration.ipynb and in CRF_Method_Categorization.ipynb
						
Resources/Comment_relation.csv - It is the CSV File received from PostgreSQL. 
									This file contains the ID's of all the child nodes and their corresponding parent nodes.
									First line is heading.

Resources/User_Data.csv - It is the CSV File received from PostgreSQL Database. 
							This file contains data about User's who have commented in the reddit thread.
							First line is heading.

Resources/Submission_Details.csv - It is the CSV File received from PostgreSQL Database.
									It contains all the details related to the submission/reddit thread.
									First line is heading.
						
Resources/BingLiu/positive-words.txt - It is a list of positive words compiled for the Bing Liu Lexicon

Resources/BingLiu/negative-words.txt - It is a list of negative words compiled for the Bing Liu Lexicon

Resources/NRC/NRC-emotion-lexicon-wordlevel-alphabetized-v0.92.txt - It is a list of words which have been mapped to 8 emotions made for the NRC 	
																		Lexicon.

Resources/MPQA_Lexicon/subjectivity_clues_hltemnlp05/subjclueslen1-HLTEMNLP05.tff - It is a list of words which has been marked with the labels based 
																					on pos tags, subjectivity and sentiments as positive or negative.
																		
Resources/Dictionaries/abilityverbs.txt - Contains the three ability verbs 'can','handle' and 'support'
											Used in getting the POS Tags as 'ABLT' for these words
								
Resources/Dictionaries/All_Negative_Words.csv - It is a list of negative words that have been compiled from 6 lexicons namely:
												Afinn, Bing_Liu, TextBlob, Vader, NRC, MPQA
											
Resources/Dictionaries/All_Postive_Words.csv - It is a list of positive words that have been compiled from 6 lexicons namely:
												Afinn, Bing_Liu, TextBlob, Vader, NRC, MPQA

Resources/Dictionaries/extreme_intensifiers_level0.txt - It is a list of intensifier words that add add emphasis to a word. Level 0 is less severe.
															Note: These intensifier words have not been verified completely and are subject to change.

Resources/Dictionaries/extreme_intensifiers_level1.txt - It is a list of intensifier words that add add emphasis to a word. Level 1 is more severe.
															Note: These intensifier words have not been verified completely and are subject to change.

Resources/Dictionaries/FPRP.txt - It is a list of First Personal Pronouns in English like 'I', 'my', etc.

Resources/Dictionaries/Negations.csv - It is a list of negation words in English. 
										They contain words which contain spelling mistakes just in case.

Resources/Dictionaries/POSEmo.csv - They contain a set of regular expression rules which are used to find definite Positive emotion words like LOL, 
									LMAO, ROFL, etc. and the regular expression is used to ensure the same sequence but any number of letters in between. For Example, LOOOOOOOOOL will be recognized and so will LOL as long as it appears in that sequence.

Resources/Dictionaries/SPRP.txt - It is a list of Second Personal Pronouns in English.

Resources/Dictionaries/swear.txt - It is a rough list of Swear words in English.

Resources/Dictionaries/WPRP.txt - It is a list of First Personal Pronouns like 'we', 'our', etc.