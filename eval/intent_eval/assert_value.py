from promptflow import tool


@tool
def assert_value(groundtruth: str, prediction: str):
    """
    This tool processes the prediction of a single line and returns the processed result.

    :param groundtruth: the "chat" or "support" value of a single line.
    :param prediction: the prediction of gpt 35 turbo model.
    """
    # Check if prediction include groundtruth
    if groundtruth in prediction:
        return "True"
    else:
        return "False"
    
    
