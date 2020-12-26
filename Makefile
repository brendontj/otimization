# define the name of the virtual environment directory
VENV := venv

TESTE1 := $(PWD)/examples/teste1.txt

TESTE2 := $(PWD)/examples/teste2.txt

# default target, when make executed without arguments
all: venv

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	./$(VENV)/bin/pip install -r requirements.txt

# venv is a shortcut target
venv: $(VENV)/bin/activate

run: venv
	./$(VENV)/bin/python3 src/tarefas.py

run-tests: venv
	./$(VENV)/bin/python3 src/tarefas.py < $(TESTE1)
	
	./$(VENV)/bin/python3 src/tarefas.py < $(TESTE2)

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

.PHONY: all venv run clean