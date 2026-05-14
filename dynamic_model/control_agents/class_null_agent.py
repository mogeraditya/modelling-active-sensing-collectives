"""This module contains the code that describes a Bat object and its behaviours"""

from agents.class_bats import Bat
from agents.class_sounds import DirectSound
from supporting_files.utilities import call_directionality_factor


class CannotHearSoundBat(Bat):
    def __init__(self, parameters_df, output_dir):
        super().__init__(parameters_df, output_dir)

    def given_sound_objects_return_sounds_at_bat_position(
        self, current_time, sound_objects
    ):
        """given sounds generate list of sounds that a bat can hear
        HERE THE BAT CANNOT HEAR ANYTHING

        Args:
            current_time (float): Time, in seconds, for which the simualtion has been running.
            sound_objects (list): List containing all active sounds in the simulation
            detect_self_call (Bool): If true, add self call to detected, else, skip self call.

        Returns:
            list: sound detections given time.
        """
        array_of_sound_detections = []
        # if bat is calling it shouldnt hear anything
        return array_of_sound_detections
