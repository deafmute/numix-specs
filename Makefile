TIMESTAMP?=none

srpm: numix-999-$(TIMESTAMP).tar.gz
	rpmbuild -D"timestamp $(TIMESTAMP)" -bs numix.spec

numix-999-$(TIMESTAMP).tar.gz:
	tar czf numix-999-$(TIMESTAMP).tar.gz numix-*-theme*
	cp -f numix-999-$(TIMESTAMP).tar.gz $(shell rpm --eval "%_sourcedir")/

mock: srpm
	mock -n -D"timestamp $(TIMESTAMP)" --rebuild $(shell rpm --eval "%_srcrpmdir")/numix-999-$(TIMESTAMP)*.src.rpm

tag:
	git tag $(TIMESTAMP)
	git push origin $(TIMESTAMP)
