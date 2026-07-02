def print_banner():
    """
    Displays the application banner.
    """

    print("=" * 50)
    print("         AI JOB INTELLIGENCE")
    print(" Gmail + OpenAI + BeautifulSoup")
    print("=" * 50)
    print()

def print_step(step):
    """
    Prints a workflow step.
    """

    print(f"[ ] {step}")
    
def print_success(step):
    """
    Prints a completed workflow step.
    """

    print(f"[✓] {step}")
    
def print_divider():
    print("-" * 50)