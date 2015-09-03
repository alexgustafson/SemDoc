#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import os

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
