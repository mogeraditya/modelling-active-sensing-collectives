import random
import sys
import uuid

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.path.append("./dynamic_model/")
sys.path.append("./JammingExperiment/Scripts/ProcessingScripts/")
from agents.class_bats import Bat
from make_jammer_positions import make_jammers
from simulation.class_simulation import Simulation
from supporting_files.utilities import make_vector
from supporting_files.vectors import Vector

sys.path.append("./dynamic_model/")
from agents.class_bats import Bat
from agents.class_obstacles import Obstacle
from agents.class_sounds import DirectSound
from agents.make_walls import make_walls
from plotting.single_bat_plotter import visualize
from supporting_files.utilities import (
    creation_time_calculation,
    load_parameters,
    read_temporal_masking_fn,
)
from supporting_files.vectors import Vector


class Modified_Simulation(Simulation):
    def __init__(
        self,
        parameters_df,
        output_dir,
        initial_release_point,
    ):
        super().__init__(parameters_df, output_dir, store_history=True)
        self.bats = []

        num_bats = 1  # len(bat_locations.keys()) %2 # just how the csv is organised

        self.bats = [
            Bat(self.parameters_df, self.output_dir) for _ in range(int(num_bats))
        ]

        self.jammers = make_jammers(self.parameters_df)

        initial_release_point = make_vector(initial_release_point)
        self.bats[0].position = initial_release_point
        self.bats[0].direction = Vector(0, 1)
        self.bats[0].id = 0

    def convert_necessary_information_into_dict(self):
        dictionary_w_information = {
            "time": np.round(self.time_elapsed, self.rounding_based_on_time_step),
            "bat_call_time": [bat.emit_times[-1] for bat in self.bats],
            "bat_positions": [(bat.position.x, bat.position.y) for bat in self.bats],
        }
        dictionary_w_information.update(self.parameters_df)
        return dictionary_w_information

    def save_history_csv(self):
        df_position_data = pd.DataFrame.from_dict(self.history, orient="columns")
        df_position_data.to_pickle(self.output_dir + "/full_history.pkl")
