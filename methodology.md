# Methodology

For this project, I wanted to analyze how Christmas tree removal requests varied year over year, since the holidays are soon coming to an end. Noticing a major uptick in requests [in 2025](https://opendata.dc.gov/datasets/DCGIS::311-city-service-requests-in-2025/), I wanted to see what spurred the change.

From a quick search online, I found lots of posts on social media platforms like Reddit that suggested a major snowstorm spurred confusion over trash collection, including tree pickups, just after the winter holiday. This made me think the uptick was related to the timing of the winter snowstorm.

Approaching this dataset required three main steps:

1. **Analyzing** annual requests from 2020 to 2025 to identify an uptick
2. **Checking** how many requests came during the Jan. 5 and 6 snowstorm
3. **Verifying** findings by checking whether a zip code with higher reported snowfall saw more calls than one with less reported snowfall.

## 1. Analyzing annual requests

For this step, I imported 311 call logs from 2020 to 2025 and filtered just for calls the city tagged as related to Christmas tree removal.

Some years tagged this differently, and some had multiple tags for the same issue. That meant I had to identify the explicit name of the tag each year to ensure I collected all related call entries.

Some of the .CSV files had formatting issues; for the ones that did, I changed entries across the entire dataframe to strings.

Once I filtered just the tree removal calls for each year, I counted the number of rows in each dataframe, because each row represents a distinct 311 call. Once I had the number of calls for each year, I exported the figures as a .CSV and uploaded it to DataWrapper to visualize. This confirmed there was a sizable increase in calls in 2025.

## 2. Checking snowstorm requests

After learning that a severe snowstorm halted trash pickup in January 2025, I wanted to see if calls increased during that window, which could explain the uptick. Using my 2025 dataset, I filtered just the calls that came in on Jan. 5 or Jan. 6, 2025.

I then counted the number of rows, representing individual entries, and subtracted it from the total number of tree pickup calls from 2025 to determine how many fell outside the window.

I entered these figures directly into DataWrapper, and obtained a visualization showing the majority of calls came in during the winter snowstorm.

## 3. Verifying zip code variations

To explore this data from another angle, I wanted to see whether calls were more common in neighborhoods with higher snowfall. This proved more difficult, because I could find limited data on neighborhood by neighborhood snowfall.

The National Weather Service listed snowfall measurements from different locations. Two where the neighborhoods were clearly specified were a measurement site at American University (that measured 6.3 inches of snow) and a site in Anacostia (that measured 7.7 inches of snow.) Since there was a notable difference between the two neighborhoods, I examined how calls varied in each zip code.

Like in the step prior, I filtered the dataframe of Christmas tree-related calls in 2025 just for those that fell in the zip codes for the two areas, 20016 and 20020 respectively. I then counted the number of rows, representing individual entries for each zip code. I entered these figures directly into DataWrapper, and obtained a visualization showing calls varied according to snowfall at least in these two zip codes.

I wanted to create two choropleth maps to compare snowfall and call entries. To standardize my colors, I set the range on the snowfall map from 6 to 12 inches, reflecting the range of snowfall documented in the greater DMV.

For the 311 call map, I went back and found the zip code with the most Christmas tree-related 311 calls in 2025 and counted its number of calls. I set this as my maximum for my color scale, and set 0 calls as the minimum.

These efforts helped ensure color variation was not exaggerated on either map, since maps with just two data points would otherwise display them as the extreme ends of a color scale.

## Conclusion

I did not hear back from the D.C. Department of Public Works directly about why they think the District saw an uptick. But based on my analysis and records from social media platforms, there seems to be a strong correlation between the major snowstorm and the rise in Christmas tree pickup confusion.

This correlation seems further supported by the fact that the week after new years marks the end of the holiday season, when many residents would likely want to dispose of their Christmas trees.

### Caveats

While this project found a correlation between the weather and 311 calls over missed tree pickups, it cannot confirm every call in the datasets filtered by time of year or zip code was caused by confusion over the snowstorm. With more time, we could substantiate these claims by interviewing residents and the public works department.

The project also does not filter out duplicate calls from the same caller or household. Meanwhile, snowfall across zip codes is generalized from individual measurement sites within the neighborhood, and may not reflect the exact amount of snowfall in every part of a zip code.

*(For a closer look, you can access the code I used for this project [at this link](https://github.com/jack-walk/IRW-01/blob/main/test.ipynb).)*
