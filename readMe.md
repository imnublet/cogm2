# Tower of Hanoi ACT-R solver

## Installation

In order to run the program python 2 and ccmsuite is required. ccm can be installed in the following way:


```bash
git clone https://github.com/tcstewar/ccmsuite
```

Using a conda env (in python 2 environment):
```bash
pip install .
conda install --file requirements.txt
```
Using pip:
```bash
pip install ccmsuite/.
pip install -r requirements.txt
```

## Usage
To run the ACT-R model that solves Hanoi you can run the command below in the shell.
Every time you run the model the total steps it takes to solve the problem gets saved in results.txt
```bash
python myModel.py
```

To visualize the results
```bash
python dataviz.py
```

