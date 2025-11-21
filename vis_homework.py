# %%

#%% libraries
import pandas as pd
import matplotlib.pyplot as plt
#%% data

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
covid_df = pd.read_csv('https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv', index_col=0)

#%% Instructions
'''
Overall instructions:
As described in the homework description, each graphic you make must:
   1. Have a thoughtful title
   2. Have clearly labelled axes 
   3. Be legible
   4. Not be a pie chart
I should be able to run your .py file and recreate the graphics without error.
As per usual, any helper variables or columns you create should be thoughtfully
named.
'''

# %%
#%% viz 1
'''
Create a visualization that shows all of the counties in Utah as a time series,
similar to the one shown in slide 22 during the lecture. The graphic should
-Show cases over time
-Have all counties plotted in a background color (something like grey)
-Have a single county plotted in a contrasting color (something not grey)
-Have well formatted dates as the X axis
'''
#get an idea of what data looks like
print("Data loaded. Shape:", covid_df.shape)
covid_df.info()
covid_df.columns
covid_df.head

# %%
import matplotlib.dates as mdates

# Filter by Utah counties
utah_df = covid_df[covid_df["Province_State"] == "Utah"].copy()

# Identify the date columns 
date_cols = utah_df.columns[utah_df.columns.str.contains(r"/")]
dates = pd.to_datetime(date_cols)

# Choose a county to highlight: I chose the one with the highest number of cases
latest_col = date_cols[-1]
highlight_idx = utah_df[latest_col].idxmax()
highlight_row = utah_df.loc[highlight_idx]
highlight_name = highlight_row["Admin2"]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot all counties in a grey background color
for _, row in utah_df.iterrows():
    ax.plot(
        dates,
        row[date_cols].values,
        color="lightgrey",
        linewidth=0.7,
        alpha=0.6,
    )

# Plot the highlighted county in a contrasting color (I chose blue to contrast the gray)
ax.plot(
    dates,
    highlight_row[date_cols].values,
    linewidth=2.0,
    label=f"{highlight_name} County",
)

# Titles and labels
ax.set_title("COVID-19 Confirmed Cases Over Time in Utah Counties")
ax.set_xlabel("Date")
ax.set_ylabel("Cumulative Confirmed Cases")

# Nicely formatted dates on the x-axis (one tick per month)
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

# Add legend to the graph
ax.legend()

# Make layout look a little more tiday as per instructions
fig.tight_layout()

plt.show()

# %%
#%% viz 2
'''
Create a visualization that shows the contrast between the county in Utah with
the most cases to date to a county in Florida with the most cases to date.
The graphic should:
-Have only two counties plotted
-Highlight the difference between the two comparison counties
You may use any style of graphic you like as long as it is effective (dense)
and readable
'''
# Identify date columns 
date_cols = covid_df.columns[covid_df.columns.str.contains(r"/")]
dates = pd.to_datetime(date_cols)

# Get Utah and Florida subsets that we need of most cases to date
utah_df = covid_df[covid_df["Province_State"] == "Utah"].copy()
florida_df = covid_df[covid_df["Province_State"] == "Florida"].copy()

# Latest date column (cumulative counts to date)
latest_col = date_cols[-1]

# Find county in Utah with most cases to date
utah_idx = utah_df[latest_col].idxmax()
utah_row = utah_df.loc[utah_idx]
utah_county_name = utah_row["Admin2"]

# Find county in Florida with most cases to date
fl_idx = florida_df[latest_col].idxmax()
fl_row = florida_df.loc[fl_idx]
fl_county_name = fl_row["Admin2"]

# Create the figure and axis
fig, ax = plt.subplots(figsize=(10, 6))

# Plot Utah county
ax.plot(
    dates,
    utah_row[date_cols].values,
    linewidth=2,
    label=f"{utah_county_name} County, Utah"
)

# Plot Florida county
ax.plot(
    dates,
    fl_row[date_cols].values,
    linewidth=2,
    linestyle='--',
    label=f"{fl_county_name} County, Florida"
)

# Titles and labels added in here
ax.set_title("Comparison of COVID-19 Confirmed Cases Over Time\nUtah vs. Florida County with Most Cases")
ax.set_xlabel("Date")
ax.set_ylabel("Cumulative Confirmed Cases")

# Monthly ticks on the x-axis, aka dates formatted nicely
ax.xaxis.set_major_locator(mdates.MonthLocator())
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.setp(ax.get_xticklabels(), rotation=45, ha='right')

# Add legend
ax.legend()

# Tidy layout
fig.tight_layout()

plt.show()

# %%
#%% viz 3
'''
Create a visualization that shows BOTH the running total of cases for a single
county AND the daily new cases. The graphic should:
-Use two y-axes (https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html)
-Use color to contrast the two series being plotted
-Have well formatted dates as the X axis
'''
#I'm going to pick Utah county since that is where I live

# Identify date columns
date_cols = covid_df.columns[covid_df.columns.str.contains(r"/")]
dates = pd.to_datetime(date_cols)

# Filter to Utah County specifically
utah_county_df = covid_df[
    (covid_df["Province_State"] == "Utah") &
    (covid_df["Admin2"] == "Utah")
].copy()

# Extract the row for utah_county
county_row = utah_county_df.iloc[0]

county_name = "Utah County"

# Prepare cumulative and daily new case series
cumulative_cases = county_row[date_cols].astype(float)
daily_new_cases = cumulative_cases.diff().fillna(0)

# Create figure with two y-axes  as per the instructions
fig, ax1 = plt.subplots(figsize=(10, 6))

ax2 = ax1.twinx()

# Plot cumulative cases
line1, = ax1.plot(
    dates,
    cumulative_cases.values,
    linewidth=2,
    label="Cumulative cases",
)

# Plot daily new cases
line2, = ax2.plot(
    dates,
    daily_new_cases.values,
    linestyle="--",
    linewidth=1,
    label="Daily new cases",
)

# Titles and labels
ax1.set_title("COVID-19 Cases in Utah County Over Time")
ax1.set_xlabel("Date")
ax1.set_ylabel("Cumulative confirmed cases")
ax2.set_ylabel("Daily new cases")

# Monthly ticks on x-axis
ax1.xaxis.set_major_locator(mdates.MonthLocator())
ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
plt.setp(ax1.get_xticklabels(), rotation=45, ha='right')

# Legend combining both axes
lines = [line1, line2]
labels = [l.get_label() for l in lines]
ax1.legend(lines, labels, loc="upper left")

fig.tight_layout()
plt.show()

# %%
#%% viz 4
'''
Create a visualization that shows a stacked bar chart of county contributions
to a given state's total cases. You may choose any state (or states).
(https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html#sphx-glr-gallery-lines-bars-and-markers-bar-stacked-py)
The graphic should:
-Have a single column delineate a state
-Have each 'slice' or column compontent represent a county
'''
#I'm going to do AZ since this is where I grew up. 

# Identify date columns
date_cols = covid_df.columns[covid_df.columns.str.contains(r"/")]
latest_col = date_cols[-1]

# Filter to Arizona
az_df = covid_df[covid_df["Province_State"] == "Arizona"]

# Extract county names and their latest cumulative case counts
county_names = az_df["Admin2"].tolist()
county_cases = az_df[latest_col].astype(float).tolist()

# Create stacked bar chart
fig, ax = plt.subplots(figsize=(8, 6))

bottom_vals = 0  

for county, cases in zip(county_names, county_cases):
    ax.bar(
        "Arizona",      
        cases,
        bottom=bottom_vals,
        label=county
    )
    bottom_vals += cases

# Title and labels
ax.set_title("County Contributions to Total COVID-19 Cases in Arizona")
ax.set_ylabel("Cumulative Confirmed Cases")

# I want to shrink legend so it fits better for my graph
ax.legend(
    title="Counties",
    bbox_to_anchor=(1.05, 1),
    loc='upper left',
    fontsize="small",
)

fig.tight_layout()
plt.show()

# %%
#%% extra credit (5 points)
'''
Use Seaborn to create a grouped box plot of all reported states. Each boxplot
should be a distinct state. Have the states ordered from most cases (FL) to fewest 
cases. (https://seaborn.pydata.org/examples/grouped_boxplot.html)
'''


import seaborn as sns


# Identify date columns and get latest date
date_cols = covid_df.columns[covid_df.columns.str.contains(r"/")]
latest_col = date_cols[-1]

# Subset needed columns for states
state_cases = covid_df[["Province_State", latest_col]].copy()
state_cases[latest_col] = state_cases[latest_col].astype(float)

# Calculate the total cases per state
state_totals = state_cases.groupby("Province_State")[latest_col].sum()

# Order states from most to least cases
state_order = state_totals.sort_values(ascending=False).index.tolist()

# Create box plots
fig, ax = plt.subplots(figsize=(16, 8))

sns.boxplot(
    data=state_cases,
    x="Province_State",
    y=latest_col,
    order=state_order,
    ax=ax
)

# Titles and Axis Labels
ax.set_title("Distribution of County COVID-19 Case Counts by State\n(Ordered by Total Cases, High → Low)")
ax.set_xlabel("State")
ax.set_ylabel("Cumulative Confirmed Cases (per county)")

plt.xticks(rotation=90)
fig.tight_layout()

plt.show()

#it looks like california and texax actually had a higher cumulative cases count, not Florida like the directions stated. 


