# Module 3: Critical Thinking Assignment
# Use Python to write a script that will print out the names and number of pages in your prototype and the sequence or flow of the pages.

# Potential solution using a Python dictionary
# Set dictionary of the page names and page numbers
Mod3_CT_Dict = {'Page 1': 'App Diagram', 'Page 2': 'Home Screen', 'Page 3': 'Cart Main Menu', 'Page 4': 'Item Main Menu'}
print('Potential solution using a Python dictionary')

# Iterate through dictionary and display the page names and page numbers
for page in Mod3_CT_Dict:
    print(page + ': ' + Mod3_CT_Dict[page])

# Potential solution using Python list and enumerate
# Set list of the pages names 
Mod3_CT_List = ['App Diagram', 'Home Screen', 'Cart Main Menu', 'Item Main Menu']
print('Potential solution using Python list and enumerate')

# Iterate through list and display page names by index (set index starting postition to 1)
#for i, page in enumerate(Mod3_CT_List, 1):
    #print('Page {}: {}'.format(i, page))