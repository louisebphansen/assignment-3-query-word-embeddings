python3 -m venv env

source ./env/bin/activate

pip install scipy==1.10.1

# install packages from requirements file
pip install -r requirements.txt

deactivate 