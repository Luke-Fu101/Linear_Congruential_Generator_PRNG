from LCG_Function import LCG
import sys
from rich.console import Console
from rich.prompt import Prompt

console = Console()

def title():
    console.clear()
    console.rule()
    console.print("[cyan]Linear Congruential Generator (LCG) Implementation[/cyan]", style="bold magenta")
    console.rule()

def run_LCG():
    key_length_input = Prompt.ask("What is the desired key length?", default="128")
    return int(key_length_input)

def clean_key(raw_bit_list):
    key_clean = ""
    for bit in raw_bit_list:
        key_clean = key_clean + str(bit)
    return key_clean

# 1. Display the UI Title
title()

# 2. Get the key length from the user
chosen_key_length = run_LCG()

# 3. Call the LCG function with the user's length and capture the generated list
generated_bits = LCG(chosen_key_length)

# 4. Convert the list of bits into a single contiguous string
final_key_value = clean_key(generated_bits)

# 5. Print out the final binary key string safely
console.print(f"\n[bold green]Final Key Result:[/bold green] [dark_blue]{final_key_value}[/dark_blue]")