all: clean blog deploy  # book

blog: build 

build:
	echo "this Makefile assumes you have [[uv]] installed."
	uv run nikola build

deploy:
	uv run nikola deploy

dorcas:
	uv run nikola deploy dorcas

paramita:
	uv run nikola deploy local

book:
	mkdir -p generated
	markdown-pp book.mdpp -o book.md
	pandoc book.md -o flancia-book.docx
	# pandoc book.md -o flancia-book.pdf
	mv book.md generated/book.md.generated
	mv flancia-book.* generated/

clean:
	rm -f generated/flancia-book.*
