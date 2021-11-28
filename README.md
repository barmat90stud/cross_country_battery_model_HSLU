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

## Run dash (visualized Kafka streams)
Open `Anaconda Prompt`
(via Windows start menu)
```
# change to the directory of this README.md file
cd c:\projects\cross_country_battery_model_HSLU

conda activate .venv/
python visualize_streams.py
```

Now, you can open http://127.0.0.1:8050/
in the browser on your developer PC.


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
