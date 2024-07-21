all: clean blog deploy  # book

blog: build 

build:
	nikola build

deploy:
	nikola deploy

dorcas:
	nikola deploy dorcas

book:
	mkdir -p generated
	markdown-pp book.mdpp -o book.md
	pandoc book.md -o flancia-book.docx
	# pandoc book.md -o flancia-book.pdf
	mv book.md generated/book.md.generated
	mv flancia-book.* generated/

clean:
	rm -f generated/flancia-book.*
