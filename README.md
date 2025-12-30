# **IRW Assessment:** Christmas Tree Removal Requests

## By **[Jack Walker](https://jackwalker.xyz/)** | Updated Dec. 29, 2025

### [Read the story at this link.](https://jack-walk.github.io/IRW-01/)

--

### About this project

**Project Description:** In this repository we analyze trends in 311 calls requesting Christmas tree removals in D.C. from 2020 to 2025. D.C. trash collectors pick up trees placed on the curb in January and February, so calls reflect requests related to pickups that the city missed. We explore a spike in calls in 2025, and whether a period of inclement weather shortly after the holiday played a role in the uptick.

**Want to run this code?**

**Required packages/libraries:** pandas

1. Download the data.
    - Create a `/jack-data` directory (in the project root).
    - Visit D.C. open data portal and download CSV files for 311 calls in [2025](https://opendata.dc.gov/datasets/DCGIS::311-city-service-requests-in-2025/), [2024](https://opendata.dc.gov/datasets/DCGIS::311-city-service-requests-in-2024/), [2023](https://opendata.dc.gov/datasets/DCGIS::311-city-service-requests-in-2023/), [2022](https://opendata.dc.gov/datasets/DCGIS::311-city-service-requests-in-2022/), [2021](https://opendata.dc.gov/datasets/DCGIS::311-city-service-requests-in-2021/), and [2020](https://opendata.dc.gov/datasets/DCGIS::311-city-service-requests-in-2020/). (You can click each year to access dataset link.)
    - Rename the CSVs to match the format `311_YEAR.csv` and put them into `/jack-data`.
2. Install python 3.13.
3. [Install pandas](https://pandas.pydata.org/docs/getting_started/install.html)
4. If using the Jupyter Notebook:
   - Install [jupyter notebook](https://jupyter.org/install#jupyter-notebook).
   - From the project root, run `jupyter notebook test.ipynb`.
5. OR if running the python file:
   - From the project root, run `python_code.py`.
7. Upload the generated .CSV files (`complaints.csv` and `zipcodes.csv`) into a visualization program like [DataWrapper](datawrapper.de).
