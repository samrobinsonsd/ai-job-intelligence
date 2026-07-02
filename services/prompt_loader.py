def load_prompt(path):
    """
    Loads a prompt from a text file.

    Parameters:
        path (str): Path to the prompt file.

    Returns:
        str: Prompt text.
    """

    with open(path, "r", encoding="utf-8") as file:
        return file.read()