import os
import sys
import json

""" This script is used to assert that the metric value in the file at file_path is greater than or equal to the expected value.

    Usage: python assert.py <file_path> <expected_value>
"""
def assert_metric(file_path:str, expected_value: str) -> bool:
    result = json.load(open(file_path))

    # Get metric values from json result
    groundedness_metric_value = result['gpt_groundedness']
    coherence_metric_value = result['gpt_coherence']
    relevance_metric_value = result['gpt_relevance']
    fluency_metric_value = result['gpt_fluency']

    # Check if each metric is not null then check against expected value
    result = False
    if groundedness_metric_value is not None:
        result = float(groundedness_metric_value) >= float(expected_value)
        #break if false
        if result == False:
            return result
    if coherence_metric_value is not None:
        result = float(coherence_metric_value) >= float(expected_value)
        #break if false
        if result == False:
            return result
    if relevance_metric_value is not None:
        result = float(relevance_metric_value) >= float(expected_value)
        #break if false
        if result == False:
            return result
    if fluency_metric_value is not None:
        result = float(fluency_metric_value) >= float(expected_value)
        #break if false
        if result == False:
            return result
    
    return True
    
def main():
    cwd = os.getcwd()
    path = os.path.join(cwd,sys.argv[1])
    expected_value = sys.argv[2]

    pass_bool = assert_metric(path, expected_value)
    
    return pass_bool

if __name__ == "__main__":
    result = main()
    print(bool(result))
    
