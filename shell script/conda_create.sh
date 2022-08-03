# create yml file
conda env export > environment_droplet.yml

# Create the environment from the environment.yml file:
conda env create -f environment.yml

# Activate the new environment:
conda activate myenv

# Verify that the new environment was installed correctly:
conda env list