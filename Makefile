# define the name of the virtual environment directory
VENV := venv

# default target, when make executed without arguments
all: venv

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV) --without-pip
	./$(VENV)/bin/pip install -r requirements.txt
	chmod +x $(PWD)/src/main.py
	chmod +x $(PWD)/tarefas

# venv is a shortcut target
venv: $(VENV)/bin/activate

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

.PHONY: all venv clean