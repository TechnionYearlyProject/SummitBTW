import os
from re import finditer

import pandas as pd

from management.functionality.algorithm_compare import compare_algorithms, TEMP_OUT_DIR
from management.gui.visual_statistics import load_statistics_widgets
from scheduler.scheduler_constants import schedulers_name_map
from simulator.simulate_tripinfo import run_simulation_example
from statistics.get_statistics import create_statistics

__author__ = "Eylon Shoshan"

from flask import Flask, request, render_template
from flask import Markup

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')
last_compare_stats = None


@app.route('/')
@app.route('/index.html')
def root():
    """
    Loading home page
    :return: html page of the dashboard
    """
    return render_template('index.html')


@app.route('/run_simulation', methods=['GET', 'POST'])
def run_simulation():
    """
    Running simulation at background
    :return: Simulation page
    """
    scheduler = schedulers_name_map["AdvancedScheduler"]
    run_simulation_example(request.args['simulation_example'], scheduler, gui=True)
    return "Simulation has finished."


def _camel_case_to_name(identifier):
    matches = finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    return ' '.join([m.group(0) for m in matches])


@app.route('/compare_schedulers', methods=['GET', 'POST'])
def compare_schedulers():
    """
    Compare scheduling algorithms and present results
    :return: Result statistics
    """
    simulation_example = request.args['simulation_example']
    schedulers = dict(request.args)['schedulers']

    stats = compare_algorithms(simulation_example, *schedulers)
    schedulers_names = [_camel_case_to_name(s) for s in schedulers]
    return load_statistics_widgets(stats, schedulers_names)


if __name__ == "__main__":
    app.run()