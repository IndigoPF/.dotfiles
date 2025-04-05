import os


def terminal():
    print(
        "### Terminal ###",
        "# Basic Commands:",
        "#  'ls': command to list files",
        "#  'll': lists all files (includes hidden files)",
        "#  'cd <name_of_directory>': change directory to 'name_of_directory'",
        "#  'pwd': print working directory (shows you where you are)",
        "#  'clear': clears the screen",
        "#  'rm <name_of_file>': delete the named file (WARNING!!! CANNOT BE UNDONE)",
    sep="\n")


def tmux():
    print(
        "### TMUX ###",
        "#  Starting Up:",
        "#   'tml': 'tmux list', to see if there are any active sessions",
        "#   'tma': 'tmux attach' connect to previous session (only works if one exists)",
        "#   'tm': 'tmux', create new tmux session",
        "#  Navigation:",
        "#   NOTE: Alt+A is your modifier key (MOD)",
        "#   NOTE: Vim keybindings (h,j,k,l) are used for naviation",
        "#   'MOD + |': Split screen (creates new 'pane')",
        "#   'Alt + <vim_motion>': Move in the direction of the vim motion pressed",
        "#   'MOD + z': Toggle zoom into pane (make fill whole screen)",
        "#   'Alt + d': Close the current pane (confirm with 'y', deny with 'n')",
        "#   'MOD + d': Exit session (does not kill it just puts in background)",
    sep="\n")


def vim():
    print(
        "### Vim ###",
        "#  Starting Up:",
        "#   'vim <name_of_file>': will open the named file (will create if doesn't exist)",
        "#  Vim Modes:",
        "#   NOTE: if not in normal mode, the mode will be shown in the bottom left corner",
        "#   Normal: For navigating through the file (the default mode)",
        "#   Insert: For entering text (Status: '--INSERT--')",
        "#   Visual: For selecting text",
        "#   Command: For running commands",
        "#  Vim Motions:",
        "#   'h, j, k, l': left, down, up, right",
        "#   'v': Enter visual mode to select text ('V' to select entire lines)",
        "#   'y': Yank (copy)",
        "#   'p': Paste",
        "#   'i': Enter insert mode before cursor ('I' for beginning of line)",
        "#   'a': Enter insert mode after cursor ('A' for end of line)",
        "#   'o': Enter insert mode and (open)/create line below cursor ('O' to open line above)",
        "#   'jk': Exit insert mode",
        "#   ':': Begin command mode",
        "#   'Esc': Exit any mode (May have a bit of a delay)",
        "#  Commands:",
        "#   NOTE: ':' to enter command mode",
        "#   'w': write (save) file",
        "#   'q': quit",
        "#   'q!': quit (without saving)",
        "#  NOTE: To learn more above vim run 'vimtutor'",
    sep="\n")


def python():
    print(
        "### Python ###",
        "# 'python <name_of_file>.py': to run the named python file",
        "# 'python': enter python interactive mode '>>>' (can exit with 'Ctrl + d')",
    sep="\n")


# Map of names of argument to the function that it will call
# NOTE: all functions must be defined above here
help_funcs_map = {
    "term": terminal,
    "tmux": tmux,
    "vim": vim,
    "py": python,
}

def get_help() -> str:
    print(
        "### Here to Help ###",
        " NOTE: This command is run with 'python ~/.help.py'",
        " NOTE: This command can also be run with 'help' (the alias)",
        " Input one of the following to get help (Enter anything else to exit):",
        *[f"  '{v}'" for v in help_funcs_map.keys()],
    sep="\n")

    # Makes sure that it holds the information on screen until next input received
    inp = input(": ")

    # This will clear the screen (same as typing 'clear' in the terminal)
    os.system('clear')

    return inp


def main():
    while True:
        inp = get_help()
        help_func = help_funcs_map.get(inp, None)  # Get function from map, or None if dne
        if help_func == None:  # (Clean) Exit if no function matches input
            return

        help_func()
        print("####################\n")


if __name__ == "__main__":
    main()
