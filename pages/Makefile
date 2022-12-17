all: book blog

blog: build deploy

build:
	nikola build

deploy:
	nikola deploy

website:
	nikola deploy dorcas

book:
	markdown-pp flancia.mdpp -o book.md
	pandoc book.md -o flancia.docx
	mv book.md book.md.generated

clean:
	rm book.md flancia.docx
