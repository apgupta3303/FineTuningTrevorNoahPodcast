number_of_files = 75

# Iterate over the range from 1 to number_of_files
for i in range(1, number_of_files + 1):
    # Construct the file name
    file_name = f"transcript{i}.txt"
    
    # Open the file in write mode to create an empty file
    with open(file_name, 'w') as file:
        # No need to write anything, just opening in 'w' mode creates the file
        pass