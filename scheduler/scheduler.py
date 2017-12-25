import operator

"""
Assumptions:
1) traffic light is a Detector object. This is because there is no Taffic_Light class.
2) is_green method to Detector object. no input, output boolean True iff the traffic light is green.
"""

"""
Public Methods:
Scheduler.schedule(): called every iteration of the simulator.
"""


class Scheduler(object):
    def __init__(self, junction):
        # the juction to schedule
        self.junction = junction

        # the traffic lights in the junction
        self.lights = junction.get_lights()

        # map from traffic light, to its mutual traffic lights
        self.mutual_lights = {light: junction.get_mutual_lights(light) for light in self.lights}

        # map from TL to it's detector's length
        self.length = {light: light.get_length()}

        # how many cycles each traffic hasn't been scheduled. prevents starvation
        self.epoch = {light: 0 for light in self.lights}

        """constants"""
        # occupancy's mesurement error.
        self.eps = 0.00001
        # starving time threshold
        self.starve_time = 20 * 10 ** 6
        # bonus for scheduling the current green light
        self.green_bonus_scheduling = 10
        # penalty for switching a currenlty green light by another.
        self.context_switch_penalty = 10

    # returns the list of detectors with occupancy > 0
    def get_non_empty_lanes(self):
        return set([light for light in self.lights if light.get_occupancy() > self.eps])

    # returns the detector with maximum starvation time if it not empty and starved for time > thershold.
    # if there is no such detector, returns None
    def get_starved_light():
        occupied_lanes = self.get_non_empty_lanes()
        waiting_queues = {light: self.epoch[light] for light in occupied_lanes}  # from non-empty TL to the time waiting
        max_starved, time = max(waiting_queues.iteritems(), key=operator.itemgetter(1))
        if time > self.starve_time:
            return max_starved
        else:
            return None

    # input: a detector
    # returns the constant green_bonus_scheduling iff the light is green.
    def green_bonus(light):
        return self.green_bonus_scheduling if light.is_green() else 0

    # returns the list of green lights in the junction
    def get_green_lights():
        return [light for light in self.lights if lights.is_green()]

    # returns the best traffic light to schedule at the current time.
    def get_best_traffic_to_schedule():
        # check starvation
        starved_light = self.get_starved_light()
        if starved_light != None:
            return starved_light

        # get the most busy lane:
        queue_length = {light: length[light] * light.get_occupancy() + self.green_bonus(light) for light in self.lights}
        green_lights = self.get_green_lights()
        max_green_queue = max([queue_length[light] for light in green_lights])
        max_busy_light, max_queue_len = max(queue_length.iteritems(), key=operator.itemgetter(1))

        if max_queue_len - self.context_switch_penalty > max_green_queue:
            return max_busy_light
        return None

    # input: list of lights to turn green.
    # Make the context switch
    # output: None
    def context_switch(lights):
        self.junction.set_green(lights)

    # update the epoch variable.
    def update_epoch():
        for light in self.lights:
            if light.is_green():
                self.epoch[light] = 0
            else:
                self.epoch[light] += 1

    # the main function that is called every iteration.
    # returns True iff a context switch has occured.
    def schedule():
        best_tl = self.get_best_traffic_to_schedule()
        if best_tl != None:
            best_partner_tl = self.find_best_partner(best_tl)
            self.contex_switch([best_tl, best_partner_tl])

        # TODO: can find the best partner to schedule to the best light if there wan't a context switch.
        #       This is good if len(mutual_lights[best_light]) > 1.

        self.update_epoch()
        return True if best_tl != None else False