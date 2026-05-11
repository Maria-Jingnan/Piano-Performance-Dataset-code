import matplotlib.pyplot as plt
import seaborn as sns
import ptitprince as pt
import matplotlib as mpl
import pandas as pd

# Years of experience = starting age - current age
# Practice hours = avg hours/ week * 52 weeks/ year * total years
# current age is in participants.tsv(column name: age), 
# start age(column name:start_age) and avg practice hours per week(column name:avg_practice_hours) are in phenotype/ Musical_experience.tsv
# Participant ID: participant_id

# Font setting (Optional, but this is the same font as on the paper)
mpl.rcParams.update({
	"font.family": "cmr10",
	"font.serif": ["Computer Modern Roman"],
	"axes.unicode_minus": False,  
	"axes.formatter.use_mathtext": True, 
})

# Matplotlib styling
sns.set_theme(style="whitegrid", context="talk")

# File path: put the path that stores participants.tsv, Musical_experience.tsv
participants_path = ""
musical_experience_path = ""

# Read files and merge on participant_id
participants_df = pd.read_csv(participants_path, sep="\t")
musical_experience_df = pd.read_csv(musical_experience_path, sep="\t")

df = pd.merge(participants_df, musical_experience_df, on="participant_id")

df = df.dropna(subset=["age", "start_age", "avg_practice_hours"])

# Calculate years of experience and accumulate practice hours
df["Experience_years"] = df["age"] - df["start_age"]
df["Practice_hours"] = df["avg_practice_hours"] * 52 * df["Experience_years"]

# Plot 1: Experience Years
color="grey"
pal = [color]
plt.figure(figsize=(7, 5))
pt.RainCloud(
	y="Experience_years",
	data=df,
	color="grey",
	palette=pal,
	bw=.2,
	width_viol=.6,
	width_box=0.1,
	box_linewidth=5,
	offset=0.1,
	alpha=0.8,
	move=0.2,
	scale="area",
	point_size=25,
	orient="h"
)

plt.xlabel("Years of Experience",fontsize=60)
plt.ylabel("")
plt.grid(True, linestyle='--', alpha=0.4)
plt.tick_params(axis='x', labelsize=55)
sns.despine(left=True, bottom=True)
plt.tight_layout()
plt.show()


# Plot 2: Practice hours
plt.figure(figsize=(7, 5))
pt.RainCloud(
	y="Practice_hours",
	data=df,
	color="grey",
	palette=pal,
	bw=.2,
	width_viol=.6,
	width_box=0.1,
	box_linewidth=5,
	offset=0.1,
	alpha=0.8,
	move=0.2,
	scale="area",
	point_size=25,
	orient="h"
)

plt.xlabel("Practice Hours",fontsize=60)
plt.ylabel("")
plt.grid(True, linestyle='--', alpha=0.4)
plt.tick_params(axis='x', labelsize=55)
sns.despine(left=True, bottom=True)
plt.tight_layout()
plt.show()
