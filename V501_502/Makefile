ifeq (,$(shell sh -c 'cygpath --version 2> /dev/null'))
  # Unix
  pwd := $$(pwd)
  translate = $1
else
  # Windows mit MSys2/Cygwin
  pwd := $$(cygpath -m "$$(pwd)")
  translate = $(shell echo '$1' | sed 's/:/;/g')
endif

all: build/main.pdf

# hier Python-Skripte:
build/180V.pdf: 180V.py data/180V.csv matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python 180V.py
build/200V.pdf: 200V.py data/200V.csv matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python 200V.py
build/250V.pdf: 250V.py data/250V.csv matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python 250V.py
build/280V.pdf: 280V.py data/280V.csv matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python 280V.py
build/300V.pdf: 300V.py data/300V.csv matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python 300V.py
build/UB.pdf: UB.py matplotlibrc header-matplotlib.tex | build
		TEXINPUTS="$(call translate,$(pwd):)" python UB.py
build/250Vmag.pdf: 250Vmag.py data/250Vmag.csv matplotlibrc header-matplotlib.tex | build
		TEXINPUTS="$(call translate,$(pwd):)" python 250Vmag.py
build/350Vmag.pdf: 350Vmag.py data/350Vmag.csv matplotlibrc header-matplotlib.tex | build
			TEXINPUTS="$(call translate,$(pwd):)" python 350Vmag.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/180V.pdf
build/main.pdf: build/200V.pdf
build/main.pdf: build/250V.pdf
build/main.pdf: build/280V.pdf
build/main.pdf: build/300V.pdf
build/main.pdf: build/UB.pdf
build/main.pdf: build/250Vmag.pdf
build/main.pdf: build/350Vmag.pdf

build/main.pdf: FORCE | build
	  TEXINPUTS="$(call translate,build:)" \
	  BIBINPUTS=build: \
	  max_print_line=1048576 \
	latexmk \
	  --lualatex \
	  --output-directory=build \
	  --interaction=nonstopmode \
	  --halt-on-error \
	main.tex

build:
	mkdir -p build

clean:
	rm -rf build

FORCE:

.PHONY: all clean
