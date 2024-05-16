python3 -m venv env

source ./env/bin/activate

#pip install scipy==1.10.1

# in case some troubles arises with installing gensim, this should work (scipy dependency broken because of update)

sudo apt update
sudo apt install libopenblas-dev

# install old version of scipy manually 
pip install scipy==1.11.0

# install packages from requirements file
pip install -r requirements.txt

deactivate 