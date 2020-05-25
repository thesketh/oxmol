# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line, and also
# from the environment for the first two.
SPHINXOPTS    ?=
SPHINXBUILD   ?= sphinx-build
SOURCEDIR     = .
BUILDDIR      = _build
# Autodoc complains if there's no oxmol.so, but this isn't
# present without compiling the Rust component!
# We can fake it by using a Python file with stub classes.
SO_FILE       = ../oxmol/oxmol.so
FAKE_OXMOL    = fake_oxmol.py
OXMOL_PY      = ../oxmol/oxmol.py

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile
	# Fake the oxmol.so file if necessary
	if [ ! -f "$(SO_FILE)" ]; then cp "$(FAKE_OXMOL)" "$(OXMOL_PY)"; fi
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	# And remove our fake oxmol.oxmol afterwards.
	if [ ! -f "$(SO_FILE)" ]; then rm "$(OXMOL_PY)"; fi
	
