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
build/bragg.pdf: bragg.py data/braggbedingung.csv matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python bragg.py
build/bismut.pdf: bismut.py data/bismut.csv matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python bismut.py
build/brom.pdf: brom.py data/brom.csv matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python brom.py
build/emission.pdf: emission.py data/emissionsspektrum.csv matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python emission.py
build/strontium.pdf: strontium.py data/strontium.csv matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python strontium.py
build/zink.pdf: zink.py data/zink.csv matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python zink.py
build/zirkonium.pdf: zirkonium.py data/zirkonium.csv matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python zirkonium.py

# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/bragg.pdf
build/main.pdf: build/bismut.pdf
build/main.pdf: build/brom.pdf
build/main.pdf: build/emission.pdf
build/main.pdf: build/zink.pdf
build/main.pdf: build/zirkonium.pdf
build/main.pdf: build/strontium.pdf

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
