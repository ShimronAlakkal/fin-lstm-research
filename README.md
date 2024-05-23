# LSTM & Mean reversion for stock price prediction.

## Prerequisites

- Data: Data has to downloaded online. Due to large size of the data it has been ignored from the source control. 
> For the model, data can contains parameters like data, open, close, high, low, and adjusted close. 

- Miniconda should be installed on your system. You can download Miniconda from the official [Miniconda website](https://docs.conda.io/en/latest/miniconda.html).

## Installation

Follow these steps to set up the project environment and install the required packages.

### Step 1: Download and Install Miniconda

1. Download the Miniconda installer for your operating system from the [Miniconda website](https://docs.conda.io/en/latest/miniconda.html).
2. Run the installer and follow the installation instructions.

### Step 2: Set Up a Conda Environment

1. Open your terminal or command prompt and move to the preferred directory as your virtual environment will be set up inside your current working directory.

2. Create a new conda environment with Python 3.8 (or your preferred version) by running the following command:

    ```bash
    conda create --prefix ./env
    ```

3. Activate the newly created environment:
        ```bash
        conda activate ./env
        ```

### Step 3: Install Required Packages

1. Ensure you are in the root directory of your project where the `requirements.txt` file is located.
2. Install the required packages using the following command:

    ```bash
    pip install -r requirements.txt
    ```

#### Step 4: Setting up Tensorflow (MacOS)

1. Install X-Code setup tools 
    ```bash
    xcode-select --install
    ```

2. Install tensorflow and its dependencies 

    ```bash
    conda install -c apple tensorflow-deps
    pip install tensorflow-macos
    pip install tensorflow-metal
    ```

3. Install jupyter deps and run jupyter notebook from where you can access the model
    ```bash
    conda install -c conda-forge -y pandas jupyter
    jupyter notebook
    ```

## ToDo
- []

