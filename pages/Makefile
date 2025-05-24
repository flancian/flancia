all: clean blog deploy  # book

blog: build 

build:
	echo "this Makefile assumes you have [[uv]] installed."
	uvx nikola build

deploy:
	uvx nikola deploy

dorcas:
	uvx nikola deploy dorcas

paramita:
	uvx nikola deploy local

book:
	mkdir -p generated
	markdown-pp book.mdpp -o book.md
	pandoc book.md -o flancia-book.docx
	# pandoc book.md -o flancia-book.pdf
	mv book.md generated/book.md.generated
	mv flancia-book.* generated/

clean:
	rm -f generated/flancia-book.*
