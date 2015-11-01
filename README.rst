Installation instructions
^^^^^^^^^^^^^^^^^^^^^^^^^

Initialize App
-------------------------------------------

- Install pip
    curl https://bootstrap.pypa.io/get-pip.py > /tmp/get-pip.py
    sudo python /tmp/get-pip.py
- Install virtualenv and virtualenv-wrapper
    sudo pip install virtualenv
    sudo pip install virtualenvwrapper
- Append the following lines to ~/.bashrc & run source ~/.bashrc after making below change
    export WORKON_HOME=$HOME/.virtualenvs
    source /usr/local/bin/virtualenvwrapper.sh
- Address possible pip permission issues
    sudo rm -rf ~/.cache/pip


Run App
--------------------------------------

- Clone the repo:
    git clone https://github.com/himudianda/REST-Assignment.git
- Create new or activate existing virtualenv
    mkvirtualenv rest #creates a new virtuakenv
    workon rest # activates existing virtualenv
- pip install --editable .
- pip install -r requirements.txt
- run all


Author
^^^^^^^^^^^^^^^^

- Harshit Imudianda | `GitHub <https://github.com/himudianda>`_
