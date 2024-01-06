from typing import List
from promptflow import tool


@tool
def get_accuracy(processed_results: str):
    """
    This tool aggregates the processed result of all lines and log metric.

    :param processed_results: List of the output of line_process node.
    """

    # Loop thru results and get number of true and false predictions
    true_count = 0
    false_count = 0

    load_list = [processed_results]
    for result in load_list:
        if result == "True":
            true_count += 1
        else:
            false_count += 1

    # Calculate accuracy
    accuracy = (true_count / (true_count + false_count)) * 100
    return {"accuracy": accuracy}