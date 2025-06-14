# 0x03. Shell, Initialization Files, Variables, and Expansions

![Shell Scripting](https://img.shields.io/badge/Shell-Bash-green) ![Ubuntu](https://img.shields.io/badge/Tested%20on-Ubuntu%2020.04-orange)

This project explores shell initialization, variables, expansions, and aliases in Bash scripting.

## Learning Objectives

### General Shell Concepts
- Understand what happens when you type `$ ls -l *.txt`
- Explain shell initialization files:
  - `/etc/profile` and `/etc/profile.d` directory
  - `~/.bashrc` file

### Variables
- Differentiate between local and global variables
- Understand reserved variables
- Create, update, and delete shell variables
- Explain special parameters (`$?`, etc.)
- Roles of reserved variables:
  - `HOME`
  - `PATH`
  - `PS1`

### Expansions
- Understand and use shell expansions
- Difference between single (`'`) and double (`"`) quotes
- Command substitution with `$()` and backticks (`` ` ``)

### Shell Arithmetic
- Perform arithmetic operations in shell

### Alias Command
- Create and list aliases
- Temporarily disable aliases

### Other Concepts
- Execute commands from a file in the current shell

## Resources
- [Shell Expansions](https://www.gnu.org/software/bash/manual/html_node/Shell-Expansions.html)
- [Shell Arithmetic](https://www.gnu.org/software/bash/manual/html_node/Shell-Arithmetic.html)
- [Shell Variables](https://www.gnu.org/software/bash/manual/html_node/Shell-Variables.html)
- [Shell Initialization Files](https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html)
- [The alias Command](https://www.gnu.org/software/bash/manual/html_node/Aliases.html)

## Man Pages
```bash
man printenv
man set
man unset
man export
man alias
man unalias
man .
man source
man printf
