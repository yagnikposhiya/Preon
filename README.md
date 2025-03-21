# Preon
A custom Python-based CLI for Ubuntu that allows natural-language file and directory management commands.

## Installation Guide

Follow these steps to install **Preon** on your system:

### 1. Download the Preon Debian Package
Download the `.deb` package for **Preon**.

### 2. Install Preon
Run the following command to install the package:<br>
`sudo dpkg -i <preon_package>.deb`

### 3. Configure Python Path
Ensure that Preon's directory is added to the `PYTHONPATH` environment variable:<br>
`grep -qxF 'export PYTHONPATH="/usr/local/lib/preon/:$PYTHONPATH"' ~/.bashrc || echo 'export PYTHONPATH="/usr/local/lib/preon/:$PYTHONPATH"' >> ~/.bashrc && source ~/.bashrc`

### 4. Verify the Installation
Check whether **Preon** is successfully installed by running:<br>
`preon --help`

## Removal Guide

Follow these steps to completly remove **Preon** from your system:

### 1. Uninstall the Preon Debian Package
Run the following command to remove the installed package:<br>
`sudo dpkg --remove preon`

### 2. Remove Preon's Configuration
Run the following command to remove Preon's configuration completly:<br>
`sudo dpkg --purge preon`

### 3. Remove Preon's Python Path Configuration
If you manually added Preon's directory to the `PYTHONPATH`, remove it from `~/.bashrc`:<br>
`sed -i '/export PYTHONPATH="\/usr\/local\/lib\/preon\/:\$PYTHONPATH"/d' ~/.bashrc`
`source ~/.bashrc`

### 4. Verify the Preon is Completly Removed
Run the following command to ensure Preon is no longer installed:<br>
`preon --help`
If it outputs, then Preon has been successfully removed:<br>
`Command 'preon' not found`

## Build Your Own Debian Package for Preon

Follow these steps to create a Debian package (.deb) for **Preon** on your local system.

### 1. Clone the Repository
Clone the repository to your local machine:<br>
`git clone <WEB_URL>`

### 2. Build the Debian Package
Run the following command to generate the Debian package:<br>
`dpkg-deb --build Preon`

### 3. Locate the Generated `.deb` File
Once the build is complete, check for the .deb package in your current directory:<br>
`ls`<br>
You will find `Preon.deb`, ready to be shared and installed on any Debian-based system.

## Traditional vs. Preon Command Comparison

| Action | Traditional Command | Preon Command |
|--------|---------------------|---------------|
| Create a text file | touch demo.txt | preon create file demo.txt|
| Create a directory | mkdir demo_dir | preon create dir demo_dir |
| Create directories in recursive way | mkdir -p demo_dir/demo_dir_2 | preon create dir demo_dir/demo_dir_2 |
| Remove a text file | rm demo.txt | preon remove any demo.txt |
| Remove a directory | rmdir directory | preon remove any demo_dir |
| Remove directories in recursive way | rm -rf demo_dir | preon remove any demo_dir |
| List all file and directories | ls | preon show all |
| List all directories | ls -d */ | preon show dir |
| List all files | ls -p <vertical_pipe> grep -v '/' | preon show file |
