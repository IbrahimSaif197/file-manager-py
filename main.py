import utils
from pathlib import Path


source = Path(input("Enter source: "))
destination = Path(input("Enter destination: "))

utils.cut_file_new_name(source, destination)