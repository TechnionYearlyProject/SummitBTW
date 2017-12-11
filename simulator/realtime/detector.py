"""
Author: EylonSho

API for detectors, which represent physical sensors in junctions.
Those can be queried for information about traffic.
"""


class Detector(object):
    """Detector class which contains real-time information about loads on them.
    """

    def __init__(self, identifier):
        self.identifier = identifier
        raise NotImplementedError

    def get_length(self):
        """Get the length of a detector.

        Getting length of a detector in meters.

        :return: Detector length
        """

        raise NotImplementedError

    def get_occupancy(self):
        """Query a detector for the occupancy in it, as it was during the last simulation step.

        Fetching status of a the self detector. This method is querying the detector
        and returns a number between 0-100, which represents how massive was the
        occupancy during the last simulation step, in percents.

        :return: Occupancy percentage
        """

        raise NotImplementedError

    def get_mean_speed(self):
        """Querying a detector for the mean speed in it, as it was during the last simulation step.

        Fetching status of a detector and getting the average speed in it during the last
        simulation step. This method returns the speed in km/h which represents that speed.

        :return: Mean speed
        """

        raise NotImplementedError
