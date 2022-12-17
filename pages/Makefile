all: book blog

blog: build deploy

build:
	nikola build

deploy:
	nikola deploy

book:
	markdown-pp flancia.mdpp -o book.md
	pandoc book.md -o flancia.docx

clean:
	rm book.md flancia.docx
