# cross_country_battery_model_HSLU

The Python library `faust` was investigated to consume
the kafka messages, but was not used in the end.

These instructions here are not needed,
but give you a head-start if you want to
use faust in the future...

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


## Run faust (Kafka streams consumer) (optional)
(not necessary for the visualisation for now,
 but the `faust` library could be used instead of
 `kafka-python` which in the future)

Open `Anaconda Prompt`
(via Windows start menu)
```
# change to the directory of this README.md file
cd c:\projects\cross_country_battery_model_HSLU

conda activate .venv/
python -m faust -A consume worker -l info
```
