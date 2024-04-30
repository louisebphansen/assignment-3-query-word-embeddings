python3 -m venv env

source ./env/bin/activate

# in case some troubles arises with installing gensim, this should word (scipy dependency broken because of update)

sudo apt update
sudo apt install libopenblas-dev

# install old version of scipy manually 
pip install scipy==1.11.0

# install packages from requirements file
pip install -r requirements.txt

deactivate 