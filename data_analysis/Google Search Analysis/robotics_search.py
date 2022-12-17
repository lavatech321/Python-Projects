import pandas as pd
from pytrends.request import TrendReq
import matplotlib.pyplot as plt
trends = TrendReq()
trends.build_payload(kw_list=["Robotics"])
data = trends.interest_by_region()
data = data.sort_values(by="Robotics", ascending=False)
data = data.head(10)
print(data)
data.reset_index().plot(x="geoName", 
                        y="Robotics", 
                        figsize=(15,12), kind="bar")
plt.style.use('fivethirtyeight')
plt.show()

data = TrendReq(hl='en-US', tz=360)
data.build_payload(kw_list=['Robotics'])
data = data.interest_over_time()
fig, ax = plt.subplots(figsize=(15, 12))
data['Robotics'].plot()
plt.style.use('fivethirtyeight')
plt.title('Total Google Searches for Robotics', 
          fontweight='bold')
plt.xlabel('Year')
plt.ylabel('Total Count')
plt.show()
