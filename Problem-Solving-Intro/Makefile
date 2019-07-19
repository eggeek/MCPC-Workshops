main.pdf: *.tex
	-pdflatex main 
	-bibtex main
	-pdflatex main
	-pdflatex main
clean:
	rm -f *.aux *.bbl *.blg *.log main.pdf
