#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import os

# english

os.system("rm main.aux")
os.system("rm main.bbl")
os.system("rm main.blg")
os.system("rm main.out")

os.system("pdflatex main.tex")
os.system("bibtex main")
os.system("pdflatex main.tex")
os.system("pdflatex main.tex")

os.system("open main.pdf")

os.system("rm main.aux")
os.system("rm main.bbl")
os.system("rm main.blg")
os.system("rm main.out")

# german

os.system("rm main_de.aux")
os.system("rm main_de.bbl")
os.system("rm main_de.blg")
os.system("rm main_de.out")

os.system("pdflatex main_de.tex")
os.system("bibtex main_de")
os.system("pdflatex main_de.tex")
os.system("pdflatex main_de.tex")

os.system("open main_de.pdf")

os.system("rm main_de.aux")
os.system("rm main_de.bbl")
os.system("rm main_de.blg")
os.system("rm main_de.out")
