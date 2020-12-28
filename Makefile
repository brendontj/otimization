# define the name of the virtual environment directory
VENV := venv

# default target, when make executed without arguments
all: venv

$(VENV)/bin/activate: requirements.txt
	virtualenv -p python3 $(VENV)
	. $(PWD)/$(VENV)/bin/activate
	./$(VENV)/bin/pip3 install -r requirements.txt
	touch tarefas
	echo "#!/bin/sh" >> tarefas
	echo ". venv/bin/activate" >> tarefas
	echo "python3 ./src/main.py" >> tarefas
	chmod +x $(PWD)/src/main.py
	chmod +x $(PWD)/tarefas

# venv is a shortcut target
venv: $(VENV)/bin/activate

clean:
	rm -rf $(VENV)
	rm tarefas
	find . -type f -name '*.pyc' -delete

.PHONY: all venv clean
