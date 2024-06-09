import shutil
from pathlib import Path

def copy_file_new_name(source:Path, destination:Path) -> None:
    if not source.exists():
        print("Source file does NOT exist")
        return
    if destination.suffix:
        if not destination.parent.exists():
            print("Wrong destination path 1")
            return
    else:
        if not destination.exists():
            print("Wrong destination path 2")
            return
    print(f"Copying {source} to {destination} ...")
    return shutil.copy2(source, destination)
    

def cut_file_new_name(source:Path, destination:Path) -> None:
    output = copy_file_new_name(source, destination)
    if output:
        source.unlink()