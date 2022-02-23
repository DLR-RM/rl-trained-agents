# Utility script to rename trained agents folders
# for gym 0.21 compatibility
import shutil
from glob import glob

# # Rename folders
# for folder in glob("*/Pend*"):
#     shutil.move(folder, folder.replace("-v0", "-v1"))
#
# # Rename checkpoints and sub-folders
# for folder in glob("*/Pendulum-v1*/Pend*"):
#     # print(folder)
#     shutil.move(folder, folder.replace("-v0", "-v1"))
