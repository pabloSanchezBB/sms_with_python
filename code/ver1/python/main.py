# @author pabloSanchezBB

##########################################################################################
""" Imports:"""
##########################################################################################
from contact import Contact
##########################################################################################


##########################################################################################
""" Program Structure:"""
##########################################################################################
"""
Copy phone_number_list.txt into a list

For each Phone Number...
	Send a Message from Frank about whether the client is interested
	If No: Remove Number from the List

               ########################################################               

Problem: How to store the Phone Numbers?
   Simple Dict with 'num' : 'yes/no/unanswered' for storage?
   Database in the Future but for now use a .txt file

Prototype will just use a text document and I'll figure out the DB solution later
"""
##########################################################################################


##########################################################################################
""" Function Definitions:"""
##########################################################################################

# Create a List of Phone Number Objects:
#	This Operates under the assumption that the .txt file is formatted as:
#
# num1
# num2
# ...
# numN
#
def init_phone_number_list():
	lines = [] # List Object to store the lines of the file
	with open('phone_number_list.txt') as f: # open the phone number files
	    lines = f.readlines() # this turns the text in the file into a string
	
	# Create a Phone Number Object and add it to a list of Objects
	phone_num_list = []
	for line in lines:
		print(line)
		phone_num_list.append(Contact(line))

	# TESTING ONLY: prints numbers to console
#	for pn in phone_num_list:
#		print(pn.get_phone_num())

	return phone_num_list
	
               ########################################################               

# Establish the Client Object for the SMS Messages
def init_phone_client():
    pass
    
               ########################################################               

# Send a test Text Message
def phone_convo_step1():
    pass
    
##########################################################################################

# vvv TESTING ONLY: vvv
init_phone_number_list()