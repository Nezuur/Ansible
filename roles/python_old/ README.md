# Ansible Role: Python Old

This Ansible role installs a specific version of Python from source and manages certain package dependencies on a target system.

## Tasks Overview

- **Set Archive and Host Facts**: Define variables for the Python archive and URL based on the desired version.
- **Install Dependencies**: Use `apt` to install necessary system packages required for building Python.
- **Setup Directories**: Create source and installation directories used during the Python build process.
- **Download and Unpack Source**: Retrieve and extract Python source code from the specified URL to the designated directory.
- **Build and Install Python**: Execute `configure`, `make`, and `make install` to compile and install Python from the source.
- **Create Symlinks**: Establish symbolic links for the installed Python binary in `/usr/bin`.
- **Install Pip Utilities**: Ensure `python3-distutils` and `python3-pip` are available for Python package management.
- **Cleanup**: Remove the source directory after installation to maintain system cleanliness.

## Configuration Variables

- **`python_ver`**: Version of Python to install (default: 3.9.17).
- **`python_install_dir`**: Directory where Python will be installed.

This role requires administrative privileges to install packages and create directories. Ensure you have the necessary permissions to execute the tasks on the target system.
