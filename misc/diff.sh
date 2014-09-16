
BRANCHES=/d/src/git/OReilly-TDDWithPyhon-book-example/BRANCHES_CHAPTERS/
#CHAPTER=chapter_08/
CHAPTER=chapter_09/

cd /d/z/bin/py/TDD-with-Python/superlists

[ ! -L $CHAPTER ] && ln -s $BRANCHES/$CHAPTER .

clear() {
	    echo; echo; echo; echo; echo; echo; echo; echo; echo; echo;
}

clear
diff --exclude=.git* --exclude=__pycache__ --exclude=*~ -rq $CHAPTER/ .

