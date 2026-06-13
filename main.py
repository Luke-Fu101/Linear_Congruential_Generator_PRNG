from LCG_Function import LCG
import sys
import random
print("EXECUTIVE PYTHON PATH:", sys.executable)
from rich.console import Console
from rich.prompt import Prompt, IntPrompt
from rich.panel import Panel
from rich.table import Table

console = Console()

def Title():
    console.clear
    console.rule()
    console.print("[cyan]Linear Congruential Generator (LCG) Implementation[/cyan]", style="bold magenta")
    console.rule()

def run_LCG():
    Key = Prompt.ask("What is the desired key length?", default="128")
    console.print("[dark blue]" + str(LCG(int(Key))) + "[/dark blue]", style="bold green")

Title()
run_LCG()