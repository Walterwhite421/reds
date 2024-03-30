import os
import pandas as pd
import numpy as np
from pybaseball import batting_stats
from pybaseball import pitching_stats
from pybaseball import playerid_lookup
from pybaseball import statcast_pitcher

START = 2022
END = 2023

batting = batting_stats(START, END, qual=200)

batting.to_csv("batting.csv")
batting = batting.groupby("IDfg", group_keys=False).filter(lambda x: x.shape[0] > 1)
