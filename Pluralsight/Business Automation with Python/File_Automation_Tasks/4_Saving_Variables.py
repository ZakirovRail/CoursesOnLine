import shelve

shelf = shelve.open('config')  # opens the config binary shelf
cfg = ['option1', 'option2']  # list of variables we want to save
shelf['options'] = cfg  # variables assigned to the shelf
shelf.close()  #stores the values in the shelf
shelf = shelve.open('config')  #reopens the config shelf
print(shelf['options']) #prints the values stored in the shelf
shelf.close() # closes the shelf







#==================================================================================






#==================================================================================






#==================================================================================





