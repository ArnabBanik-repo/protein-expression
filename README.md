# Protein Expression

## How to Use?

- Create a folder where you want to store the files
- Clone the repository
```git
git clone https://github.com/ArnabBanik-repo/protein-expression .
```
- Create a virtual environment
```bash
python -m venv venv
```
- Activate the virtual environment
```bash
venv\Scripts\activate
```
- Install all the dependencies
```bash
pip install -r requirements.txt
```
- Create a `data` folder 
- Inside the `data` folder, place the following files:
    1. `InputData.csv` (Containing list of all the proteins)
    2. `act_inh.csv` (Containing the proteins in cols A and B and the activation and inhibition values as 0 or 1 in cols C and D respectively)
    **Note**: `act_inh.csv` should have column names: `ENTITYA`, `ENTITYB`, `ACTIVATION`, `INHIBITION`
- Either provide or generate a `expression_values.csv` with the default expression values for all the proteins.
    **Note**: To generate default expression values run `python generate_exp.py`
- Generate the list of default activation and inhibition potential values with `python generate_pot.py`
- Run the main program to add custom patient data with `python main.py`
