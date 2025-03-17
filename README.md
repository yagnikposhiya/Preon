# Preon
A custom Python-based CLI for Ubuntu that allows natural-language file and directory management commands.

## Installation Guide

Follow these steps to install **Preon** on your system:

### 1. Download the Preon Debian Package
Download the `.deb` package for **Preon**.

### 2. Install Preon
Run the following command to install the package:
`sudo dpkg -i <preon_package>.deb`

### 3. Configure Python Path
Ensure that Preon's directory is added to the `PYTHONPATH` environment variable:
`grep -qxF 'export PYTHONPATH="/usr/local/lib/preon/:$PYTHONPATH"' ~/.bashrc || echo 'export PYTHONPATH="/usr/local/lib/preon/:$PYTHONPATH"' >> ~/.bashrc && source ~/.bashrc`

### 4. Verify the Installation
Check whether **Preon** is successfully installed by running:
`preon --help`