"""
This is an API for the City class. It is built for the scheduling algorithm,
and it encapsulates the city's junctions.
"""

__author__ = "Yair Feldman"

from collections import defaultdict
import traci
from .junction import Junction


class City(object):
    """A city, containing all of the traffic lights currently loaded to the simulator.

    """
    def __init__(self):
        self._traffic_light_ids = traci.trafficlights.getIDList()
        self._detector_ids = traci.lanearea.getIDList()
        junction_detector_dict = self._get_junction_detector_dict()
        self._junctions = {i: Junction(traffic_light_id=i, detector_ids=junction_detector_dict[i])
                           for i in self._traffic_light_ids}

    def _get_junction_detector_dict(self):
        """returns a dictionary of juntion_id -> list of detector id's

        :return: a dictionary
        """
        junction_detector_dict = defaultdict(list)
        for det_id in self._detector_ids:
            junction_detector_dict[det_id.split('_')[0]].append(det_id)
        return junction_detector_dict

    def get_junctions(self):
        """returns a list containing the city's junctions

        :return: list of Junctions
        """
        return list(self._junctions.values())

    def get_junction_by_id(self, junction_id):
        return self._junctions[junction_id]