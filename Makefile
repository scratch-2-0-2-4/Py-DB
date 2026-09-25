ifeq ($(OS),Windows_NT)
    PYTHON = python
    RM = rmdir /s /q
else
    PYTHON = python3
    RM = rm -rf
endif

run:
	$(PYTHON) script.py