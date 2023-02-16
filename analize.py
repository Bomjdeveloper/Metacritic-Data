import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

#remove lines with tbd
data = pd.read_csv('data.csv')
data = pd.DataFrame(data)
data = data[data["User score"].astype('str').str.contains('0') == False]
data["User score"] = pd.to_numeric(data["User score"]).astype('Int64')
data["Meta score"] = pd.to_numeric(data["Meta score"]).astype('Int64')
data = data.drop('Unnamed: 0', axis=1)

#show Meta and User score graphic
plt.plot(data["Meta score"])
plt.plot(data["User score"], alpha=0.6)
plt.show()

#find the most common game grade
print("Meta score:" + str(data["Meta score"].value_counts().idxmax()))
print("User score:" + str(data["User score"].value_counts().idxmax()))
print(data.mean(numeric_only=True))

data_platform_user_score = data.pivot(index=None, columns='Platform name', values='User score')

#get plaforms most common user grade
wii_u = data_platform_user_score["WiiU"].value_counts().idxmax()
ds3 = data_platform_user_score["3DS"].value_counts().idxmax()
DS = data_platform_user_score["DS"].value_counts().idxmax()
Dreamcast = data_platform_user_score["Dreamcast"].value_counts().idxmax()
GameBoyAdvance = data_platform_user_score["GameBoyAdvance"].value_counts().idxmax()
GameCube = data_platform_user_score["GameCube"].value_counts().idxmax()
Nintendo64 = data_platform_user_score["Nintendo64"].value_counts().idxmax()
PC = data_platform_user_score["PC"].value_counts().idxmax()
PSP = data_platform_user_score["PSP"].value_counts().idxmax()
PlayStation = data_platform_user_score["PlayStation"].value_counts().idxmax()
PlayStation2 = data_platform_user_score["PlayStation2"].value_counts().idxmax()
PlayStation3 = data_platform_user_score["PlayStation3"].value_counts().idxmax()
PlayStation4 = data_platform_user_score["PlayStation4"].value_counts().idxmax()
PlayStation5 = data_platform_user_score["PlayStation5"].value_counts().idxmax()
PlayStationVita = data_platform_user_score["PlayStationVita"].value_counts().idxmax()
Stadia = data_platform_user_score["Stadia"].value_counts().idxmax()
Switch = data_platform_user_score["Switch"].value_counts().idxmax()
Wii = data_platform_user_score["Wii"].value_counts().idxmax()
Xbox = data_platform_user_score["Xbox"].value_counts().idxmax()
Xbox360 = data_platform_user_score["Xbox360"].value_counts().idxmax()	
XboxOne = data_platform_user_score["XboxOne"].value_counts().idxmax()
XboxSeriesX = data_platform_user_score["XboxSeriesX"].value_counts().idxmax()

most_common_user_grade = {
    wii_u,
    ds3,
    DS,
    Dreamcast,
    GameBoyAdvance,
    GameCube,
    Nintendo64,
    PC,
    PSP,
    PlayStation,
    PlayStation2,
    PlayStation3,
    PlayStation4,
    PlayStation5,
    PlayStationVita,
    Stadia,
    Switch,
    Wii,
    Xbox,
    Xbox360,
    XboxOne,
    XboxSeriesX
}

most_common_user_grade_names = {
    "WiiU",
    "3DS",
    "DS",
    "Dreamcast",
    "GameBoyAdvance",
    "GameCube",
    "Nintendo64",
    "PC",
    "PSP",
    "PlayStation",
    "PlayStation2",
    "PlayStation3",
    "PlayStation4",
    "PlayStation5",
    "PlayStationVita",
    "Stadia",
    "Switch",
    "Wii",
    "Xbox",
    "Xbox360",
    "XboxOne",
    "XboxSeriesX"
}

#get platform arithmetic averages
wii_u_averages = data_platform_user_score["WiiU"].mean()
ds3_averages = data_platform_user_score["3DS"].mean()
DS_averages = data_platform_user_score["DS"].mean()
Dreamcast_averages = data_platform_user_score["Dreamcast"].mean()
GameBoyAdvance_averages = data_platform_user_score["GameBoyAdvance"].mean()
GameCube_averages = data_platform_user_score["GameCube"].mean()
Nintendo64_averages = data_platform_user_score["Nintendo64"].mean()
PC_averages = data_platform_user_score["PC"].mean()
PSP_averages = data_platform_user_score["PSP"].mean()
PlayStation_averages = data_platform_user_score["PlayStation"].mean()
PlayStation2_averages = data_platform_user_score["PlayStation2"].mean()
PlayStation3_averages = data_platform_user_score["PlayStation3"].mean()
PlayStation4_averages = data_platform_user_score["PlayStation4"].mean()
PlayStation5_averages = data_platform_user_score["PlayStation5"].mean()
PlayStationVita_averages = data_platform_user_score["PlayStationVita"].mean()
Stadia_averages = data_platform_user_score["Stadia"].mean()
Switch_averages = data_platform_user_score["Switch"].mean()
Wii_averages = data_platform_user_score["Wii"].mean()
Xbox_averages = data_platform_user_score["Xbox"].mean()
Xbox360_averages = data_platform_user_score["Xbox360"].mean()	
XboxOne_averages = data_platform_user_score["XboxOne"].mean()
XboxSeriesX_averages = data_platform_user_score["XboxSeriesX"].mean()

pd.set_option('display.max_rows', None)

data_platform_meta_score = data.pivot(index=None, columns='Platform name', values='Meta score').apply(lambda data_platform_meta_score: pd.Series(data_platform_meta_score.dropna().to_numpy()))

#get plaforms most common user grade
wii_u_meta = data_platform_meta_score["WiiU"].value_counts().idxmax()
ds3_meta = data_platform_meta_score["3DS"].value_counts().idxmax()
DS_meta = data_platform_meta_score["DS"].value_counts().idxmax()
Dreamcast_meta = data_platform_meta_score["Dreamcast"].value_counts().idxmax()
GameBoyAdvance_meta = data_platform_meta_score["GameBoyAdvance"].value_counts().idxmax()
GameCube_meta = data_platform_meta_score["GameCube"].value_counts().idxmax()
Nintendo64_meta = data_platform_meta_score["Nintendo64"].value_counts().idxmax()
PC_meta = data_platform_meta_score["PC"].value_counts().idxmax()
PSP_meta = data_platform_meta_score["PSP"].value_counts().idxmax()
PlayStation_meta = data_platform_meta_score["PlayStation"].value_counts().idxmax()
PlayStation2_meta = data_platform_meta_score["PlayStation2"].value_counts().idxmax()
PlayStation3_meta = data_platform_meta_score["PlayStation3"].value_counts().idxmax()
PlayStation4_meta = data_platform_meta_score["PlayStation4"].value_counts().idxmax()
PlayStation5_meta = data_platform_meta_score["PlayStation5"].value_counts().idxmax()
PlayStationVita_meta = data_platform_meta_score["PlayStationVita"].value_counts().idxmax()
Stadia_meta = data_platform_meta_score["Stadia"].value_counts().idxmax()
Switch_meta = data_platform_meta_score["Switch"].value_counts().idxmax()
Wii_meta = data_platform_meta_score["Wii"].value_counts().idxmax()
Xbox_meta = data_platform_meta_score["Xbox"].value_counts().idxmax()
Xbox360_meta = data_platform_meta_score["Xbox360"].value_counts().idxmax()	
XboxOne_meta = data_platform_meta_score["XboxOne"].value_counts().idxmax()
XboxSeriesX_meta = data_platform_meta_score["XboxSeriesX"].value_counts().idxmax()

#get platform arithmetic averages
wii_u_averages_meta = data_platform_meta_score["WiiU"].mean()
ds3_averages_meta = data_platform_meta_score["3DS"].mean()
DS_averages_meta = data_platform_meta_score["DS"].mean()
Dreamcast_averages_meta = data_platform_meta_score["Dreamcast"].mean()
GameBoyAdvance_averages_meta = data_platform_meta_score["GameBoyAdvance"].mean()
GameCube_averages_meta = data_platform_meta_score["GameCube"].mean()
Nintendo64_averages_meta = data_platform_meta_score["Nintendo64"].mean()
PC_averages_meta = data_platform_meta_score["PC"].mean()
PSP_averages_meta = data_platform_meta_score["PSP"].mean()
PlayStation_averages_meta = data_platform_meta_score["PlayStation"].mean()
PlayStation2_averages_meta = data_platform_meta_score["PlayStation2"].mean()
PlayStation3_averages_meta = data_platform_meta_score["PlayStation3"].mean()
PlayStation4_averages_meta = data_platform_meta_score["PlayStation4"].mean()
PlayStation5_averages_meta = data_platform_meta_score["PlayStation5"].mean()
PlayStationVita_averages_meta = data_platform_meta_score["PlayStationVita"].mean()
Stadia_averages_meta = data_platform_meta_score["Stadia"].mean()
Switch_averages_meta = data_platform_meta_score["Switch"].mean()
Wii_averages_meta = data_platform_meta_score["Wii"].mean()
Xbox_averages_meta = data_platform_meta_score["Xbox"].mean()
Xbox360_averages_meta = data_platform_meta_score["Xbox360"].mean()	
XboxOne_averages_meta = data_platform_meta_score["XboxOne"].mean()
XboxSeriesX_averages_meta = data_platform_meta_score["XboxSeriesX"].mean()

def draw_bars(list_with_data, name_of_data, name):
    plt.rcdefaults()
    fig, ax = plt.subplots()

    y_position = np.arange(len(name_of_data))

    ax.barh(y_position, list_with_data, align='center')
    ax.set_yticks(y_position, labels=name_of_data)
    ax.invert_yaxis()
    ax.xlabel(name)

    plt.show()

draw_bars(most_common_user_grade, most_common_user_grade_names, 'Name')