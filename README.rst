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


Question
^^^^^^^^^^^^^^^^

1. REST API Service.
--------------------------------------

Develop a REST service using Python. The REST API should expose CRUD operations allowing
individual users to provide comments, i.e. short text strings, about a discussion topics/tags. It is
recommended to use Django or Twisted for the implementation of the service. The capabilities of the
service should include:

a. Data-model - Create a data-model that will be used for the service.

b. REST API - This should allow a client to retrieve all evaluations and to filter based on criteria
    of your choice. Examples could include user and topic/tag.

c. While you program your code please answer the following questions -
    i. What are some axioms you follow for designing a REST API?
    ii. How do HTTP protocol header values aid in the design of the interface?
    iii. When a public REST API needs to be changed what considerations must the developer consider?
    iv. What is a good testing strategy for an API?
    v. How does the “Principle of Least Astonishment” factor into a good API design?

2. Multi-User blackboard Service
--------------------------------------

Extend the REST service from exercise 1 allowing multiple users to use the service in a collaborative
blackboard application style. This means that multiple users should be able to edit a comment at the
same time and the API should be able to determine that the resource has changed and take appropriate
action.

3. Compose a programming exercise question
------------------------------------------

Compose a programming test question, along with its answer, that you would like to have been asked.
This should be a question where the answer exhibits some aspect of your skills better than the other
questions and answers. A new standalone question is preferred, or a set that go together like the ones
above. It should be something that can be solved, implemented, and tested in no more than an hour if
the person answering it already has strong knowledge and experience in the areas it addresses. If
additional research is needed or bugs have to be fixed, it could of course take a couple hours longer. It
should test skills in C, Unix/Linux, networking, filesystems, cryptography, memory management, etc, or
another skillset specific to the role you’re applying for. It should be a new question and not something
that can just be found out on the Internet, although sensible mashups of existing questions are allowable.
The important part is that it's not something someone could just look up and find a direct answer to. This
is your chance to contribute to our collection of test questions for future prospective employees.


Author
^^^^^^^^^^^^^^^^

- Harshit Imudianda | `GitHub <https://github.com/himudianda>`_
