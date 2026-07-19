import os

assert os.path.exists("model(netflix).pkl"), "Model file missing!"
assert os.path.exists("preprocessor(netflix).pkl"), "Preprocessor file missing!"

print("All files found.")
