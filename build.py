#!/usr/bin/env python
# -*- coding: utf-8 -*-

import shutil
import os

os.system("rm main.4ct")
os.system("rm main.4tc")
os.system("rm main_de.4ct")
os.system("rm main_de.4tc")
os.system("rm main.dvi")
os.system("rm main_de.dvi")
os.system("rm main.idv")
os.system("rm main_de.idv")

os.system("rm main_de.aux")
os.system("rm main_de.bbl")
os.system("rm main_de.blg")
os.system("rm main_de.out")
os.system("rm main.aux")
os.system("rm main.bbl")
os.system("rm main.blg")
os.system("rm main.out")
os.system("rm main.out")
os.system("rm main.out")


# english

os.system("pdflatex main.tex")
os.system("bibtex main")
os.system("pdflatex main.tex")
os.system("pdflatex main.tex")

os.system("open main.pdf")

# german

os.system("pdflatex main_de.tex")
os.system("bibtex main_de")
os.system("pdflatex main_de.tex")
os.system("pdflatex main_de.tex")

os.system("open main_de.pdf")

#html


os.system('htlatex main.tex "html,word" \'symbol/!\' "-cvalidate"')
os.system('htlatex main_de.tex "html,word" \'symbol/!\' "-cvalidate"')


#cleanup

os.system("rm main.4ct")
os.system("rm main.4tc")
os.system("rm main_de.4ct")
os.system("rm main_de.4tc")
os.system("rm main.dvi")
os.system("rm main_de.dvi")
os.system("rm main.idv")
os.system("rm main_de.idv")

os.system("rm main_de.aux")
os.system("rm main_de.bbl")
os.system("rm main_de.blg")
os.system("rm main_de.out")
os.system("rm main.aux")
os.system("rm main.bbl")
os.system("rm main.blg")
os.system("rm main.out")
os.system("rm main.out")
os.system("rm main.out")