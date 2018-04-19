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
build/plot.pdf: plot.py matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python plot.py
build/histo.pdf: histo.py data/histo.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python histo.py
build/5mmenergie.pdf: 5mmenergie.py data/5mm.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python 5mmenergie.py
build/25mmenergie.pdf: 25mmenergie.py data/25mm.txt matplotlibrc header-matplotlib.tex | build
	TEXINPUTS="$(call translate,$(pwd):)" python 25mmenergie.py
build/5mmcounts.pdf: 5mmcounts.py data/5mm.txt matplotlibrc header-matplotlib.tex | build
		TEXINPUTS="$(call translate,$(pwd):)" python 5mmcounts.py
build/25mmcounts.pdf: 25mmcounts.py data/25mm.txt matplotlibrc header-matplotlib.tex | build
		TEXINPUTS="$(call translate,$(pwd):)" python 25mmcounts.py
# hier weitere Abhängigkeiten für build/main.pdf deklarieren:
build/main.pdf: build/plot.pdf
build/main.pdf: build/histo.pdf
build/main.pdf: build/5mmenergie.pdf
build/main.pdf: build/25mmenergie.pdf
build/main.pdf: build/5mmcounts.pdf
build/main.pdf: build/25mmcounts.pdf

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
