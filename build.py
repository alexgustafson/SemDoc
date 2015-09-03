#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import os

os.system("pdflatex main.tex")
os.system("bibtex main")
os.system("pdflatex main.tex")
os.system("pdflatex main.tex")