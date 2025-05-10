import h5py

# Open the file
file = h5py.File('optimized_model.h5', 'r')

# List all groups/datasets inside
print("Keys:", list(file.keys()))

# (Optional) Access a dataset if you know its name
# data = file['your_dataset_name'][:]
# print(data)

file.close()
