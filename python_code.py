# **0: Importing Pandas and 311 Datasets, 2020-2025**

  ## Importing pandas.
    import pandas as pd

    ### Making all columns visible in imported CSV files.
      pd.set_option('display.max_columns', None)

  ## Importing datasets.

    ### Importing **2025** dataset for 311 complaints, then testing.
      df_25 =  pd.read_csv("jack-data/311_2025.csv", dtype = str)
      df_25.head()

    ### Importing **2024** dataset for 311 complaints, then testing.
      df_24 =  pd.read_csv("jack-data/311_2024.csv")
      df_24.head()

    ### Importing **2023** dataset for 311 complaints, then testing.
      df_23 =  pd.read_csv("jack-data/311_2023.csv")
      df_23.head()

    ### Importing **2022** dataset for 311 complaints, then testing.
      df_22 =  pd.read_csv("jack-data/311_2022.csv", dtype = str)
      df_22.head()

    ### Importing **2021** dataset for 311 complaints, then testing.
      df_21 =  pd.read_csv("jack-data/311_2021.csv", dtype = str)
      df_21.head()

    ### Importing **2020** dataset for 311 complaints, then testing.
      df_20 =  pd.read_csv("jack-data/311_2020.csv")
      df_20.head()

# **1: Filtering Annual Christmas Tree Removal Complaints**

  ## **2025**

    ### Identifying service code description(s) for missed Christmas tree removal.
      codes_test_25 = df_25['SERVICECODEDESCRIPTION'].unique()
      print(sorted(codes_test_25))

    ### Filtering Christmas tree removal complaints into a new dataframe.
      trees_25 = df_25[df_25['SERVICECODEDESCRIPTION'] == 'Christmas Tree Removal - Missed']
      print(trees_25)

    ### Counting rows in new dataframe, which reflect total Christmas tree removal complaints for **2025**.
      count_25 = len(trees_25)
      print(count_25)

  ## **2024**

    ### Identifying service code description(s) for missed Christmas tree removal.
      codes_test_24 = df_24['SERVICECODEDESCRIPTION'].unique()
      print(sorted(codes_test_24))

    ### Filtering Christmas tree removal complaints into a new dataframe.
      trees_24 = df_24[df_24['SERVICECODEDESCRIPTION'] == 'Christmas Tree Removal - Missed']
      print(trees_24)

    ### Counting rows in new dataframe, which reflect total Christmas tree removal complaints for **2024**.
      count_24 = len(trees_24)
      print(count_24)

  ## **2023**

    ### Identifying service code description(s) for missed Christmas tree removal.
      codes_test_23 = df_23['SERVICECODEDESCRIPTION'].unique()
      print(sorted(codes_test_23))

    ### Filtering Christmas tree removal complaints into a new dataframe.
      trees_23 = df_23[df_23['SERVICECODEDESCRIPTION'] == 'Christmas Tree Removal - Missed']
      print(trees_23)

    ### Counting rows in new dataframe, which reflect total Christmas tree removal complaints for **2023**.
      count_23 = len(trees_23)
      print(count_23)

  ## **2022**

    ### Identifying service code description(s) for missed Christmas tree removal.
      codes_test_22 = df_22['SERVICECODEDESCRIPTION'].unique()
      print(sorted(codes_test_22))

    ### Filtering Christmas tree removal complaints into new dataframe.
      trees_22 = df_22[df_22['SERVICECODEDESCRIPTION'] == 'Christmas Tree Removal - Missed']
      print(trees_22)

      trees_22_alt = df_22[df_22['SERVICECODEDESCRIPTION'] == 'Christmas Tree Removal-Missed']
      print(trees_22_alt)

    ### Counting rows in new dataframes, which reflect total Christmas tree removal complaints for **2022**.
      count_22 = (len(trees_22) + len(trees_22_alt))
      print(count_22)

  ## **2021**

    ### Identifying service code description(s) for missed Christmas tree removal.
      codes_test_21 = df_21['SERVICECODEDESCRIPTION'].unique()
      print(sorted(codes_test_21))

    ### Filtering Christmas tree removal complaints into new dataframes.
      trees_21 = df_21[df_21['SERVICECODEDESCRIPTION'] == 'Christmas Tree Removal-Missed']
      print(trees_21)

    ### Counting rows in new dataframes, which reflect total Christmas tree removal complaints for **2021**.
      count_21 = len(trees_21)
      print(count_21)

  ## **2020**

    ### Identifying service code description(s) for missed Christmas tree removal.
      codes_test_20 = df_20['SERVICECODEDESCRIPTION'].unique()
      print(sorted(codes_test_20))

    ### Filtering Christmas tree removal complaints into new dataframes.
      trees_20 = df_20[df_20['SERVICECODEDESCRIPTION'] == 'Christmas Tree Removal-Missed']
      print(trees_20)

      trees_20_alt = df_20[df_20['SERVICECODEDESCRIPTION'] == 'Christmas Tree Collection Concerns']
      print(trees_20_alt)

    ### Counting rows in new dataframes, which reflect total Christmas tree removal complaints for **2020**.
      count_20 = (len(trees_20) + len(trees_20_alt))
      print(count_20)

# **2: Exporting Annual Complaints As CSV**

  ## Creating a new dictionary containing complaints per year.
    complaints_per_year = {'Year': ['2025', '2024', '2023', '2022', '2021', '2020'], 'Complaints': [count_25, count_24, count_23, count_22, count_21, count_20]}

  ## Checking the dictionary data is accurate.
    print(complaints_per_year)

  ## Converting the dictionary to a dataframe.
      complaints = pd.DataFrame.from_dict(complaints_per_year)
      complaints.head(6)

  ## Exporting the dataframe to CSV, for upload and visualization in DataWrapper.
      complaints.to_csv('complaints.csv')

# **3: Examining Time of Year, 2025 Complaints**

  ## Creating a new dictionary containing complaints filed during winter snowstorm (Jan. 5 to 6, 2025).
    snow_related = df_25[(df_25['ADDDATE'] > '2025/01/04 23:59:59+00') & (df_25['ADDDATE'] < '2025/01/07 00:00:00+00')]

  ## Verifying that the dictionary data is accurate.
    print(snow_related)

  ## Counting rows, which reflects total complaints lodged during snowstorm.
    count_snowstorm = (len(snow_related))
    print(count_snowstorm)

  ## Counting complaints outside snowstorm window.
    count_non_snowstorm = (count_25-count_snowstorm)
    print(count_non_snowstorm)

# **4: Examining Zip Codes, 2025 Complaints**

  ## Checking possible zip codes.
    zip_codes_test = df_25['ZIPCODE'].unique()
    print(zip_codes_test)

  ## Creating a new dictionary containing complaints filed in zip code with higher snowfall level (7.7 inches in zip code 20020).
    snow_high = snow_related[(snow_related['ZIPCODE'] == '20020')]
    print(snow_high)

  ## Counting rows, which reflects total complaints in zip code 20020.
    count_high_snow = (len(snow_high))
    print(count_high_snow)

  ## Creating a new dictionary containing complaints filed in zip code with lower snowfall level (6.3 inches in zip code 20016).
    snow_low = snow_related[(snow_related['ZIPCODE'] == '20016')]
    print(snow_low)

  ## Counting rows, which reflects total complaints in zip code 20016.
    count_low_snow = (len(snow_low))
    print(count_low_snow)

  ## Moving zip code counts into a dataframe.
    zipcodes = {'Zipcode': ['20020', '20016'], 'Complaints': [count_high_snow, count_low_snow]}
    zipcodes_count = pd.DataFrame.from_dict(zipcodes)
    zipcodes_count.head()

  ## Exporting the dataframe to CSV, for upload and visualization in DataWrapper.
    zipcodes_count.to_csv('zipcodes.csv')

  ## Finding most common zip code for call entries to help standardize colors.
    most_common_zip = snow_related.ZIPCODE.mode()
    print(most_common_zip)

  ## Counting the number of calls in the most commonly entered zip code to set as maximum on color scale.
    zip_high = snow_related[(snow_related['ZIPCODE'] == '20011')]
    print(zip_high)

  ## Returning the count.
    zip_count_max = (len(zip_high))
    print(zip_count_max)
