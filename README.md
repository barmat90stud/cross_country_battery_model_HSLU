# cross_country_battery_model_HSLU


## Installation
Open `Anaconda Prompt`
(via Windows start menu)
```
# change to the directory of this README.md file
cd c:\projects\cross_country_battery_model_HSLU

# create a new conda environment in this directory
conda create --prefix ./.venv
conda activate .venv/

conda install python=3.9

# install the Python packages
python -m pip install -r requirements.txt
```

## Run faust (Kafka streams consumer)
Open `Anaconda Prompt`
(via Windows start menu)
```
# change to the directory of this README.md file
cd c:\projects\cross_country_battery_model_HSLU

conda activate .venv/
python -m faust -A consume worker -l info
```
