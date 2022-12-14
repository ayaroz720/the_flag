import os
import csv
import pandas as pd

global data_frame
global name_file
global list_of_index
pd.options.display.max_rows = 9


def create_database():
    global name_file
    global list_of_index
    name_file = "previous_states_game.csv"
    if not os.path.exists("previous_states_game.csv"):
        with open(name_file, 'w', newline='') as file:
            writer = csv.writer(file)
    list_of_index = []
    create_list_of_previous_index()


def create_list_of_previous_index():
    global list_of_index
    df = pd.read_csv(name_file, dtype=object)
    for row in range(len(df)):
        list_of_index.append(int(df.loc[row, "num_press"]))

def save_data(state):
    global data_frame
    global name_file
    global list_of_index
    if len(list_of_index) != 0 and state["number_press"] in list_of_index:
        df = pd.read_csv(name_file, dtype=object)
        for row in range(len(df)):
            if int(df.loc[row, "num_press"]) == state["number_press"]:
                list_row = [state["number_press"], state["soldier_location"], state["mine_location"],
                            state["grass_location"]]
                df.loc[row] = list_row
        df.to_csv(name_file, header=True, sep=',', index=False, mode='w')



    elif len(list_of_index) != 0 and state["number_press"] not in list_of_index:
        df = pd.read_csv(name_file)
        list_row = [state["number_press"], state["soldier_location"], state["mine_location"],
                    state["grass_location"]]
        df.loc[len(df)] = list_row
        df.to_csv(name_file, header=True, sep=',', index=False, mode='w')
        df = pd.read_csv(name_file)
        list_of_index.append(state["number_press"])

    else:
        list_of_index.append(state["number_press"])
        data = {"num_press":[ state["number_press"]],
                "location_soldier":  [state["soldier_location"]],
                "location_mine": [state["mine_location"]],
                "location_grass": [state["grass_location"]]}
        df = pd.DataFrame(data)
        df.to_csv(name_file, header=True, sep=',', index=False, mode='w')
        df = pd.read_csv(name_file)


def return_previous_game(state):
    global name_file
    if len(list_of_index) != 0 and state["number_press"] in list_of_index:
        df = pd.read_csv(name_file, dtype=object)
        for row in range(len(df)):
            if int(df.loc[row, "num_press"]) == state["number_press"]:
                return df.loc[row].to_dict()
    else:
        return ""
