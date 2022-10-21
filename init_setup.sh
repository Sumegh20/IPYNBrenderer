echo [$(date)]: "START"
echo [$(date)]: "Creating conda env with python 3.8"
conda create --prefix ./env python==3.8 -y
echo [$(date)]: "Activate the conda env"
source activate ./env
echo [$(date)]: "installing dev requirements"
pip install -r requirements_dev.txt
echo [$(date)]: "END"

# Run the file by following command in the terminal
# bash init_setup.sh