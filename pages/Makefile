all: book blog

blog: build deploy

build:
	nb	

deploy:
	nd

book:
	markdown-pp flancia.mdpp -o book.md
	pandoc book.md -o flancia.docx
	rm book.md

clean:
	rm book.md flancia.docx
