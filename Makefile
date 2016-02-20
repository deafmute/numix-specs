TIMESTAMP?=none

srpm: numix-999-$(TIMESTAMP).tar.gz prep
	rpmbuild -D"timestamp $(TIMESTAMP)" -bs numix.spec
	cp $(shell rpm --eval "%_srcrpmdir")/numix-999-$(TIMESTAMP)*.src.rpm .

prep:
	mkdir -p $(shell rpm --eval '%_topdir')/{BUILD,BUILDROOT,RPMS,SOURCES,SPECS,SRPMS}

numix-999-$(TIMESTAMP).tar.gz: check prep
	tar czf numix-999-$(TIMESTAMP).tar.gz numix-*-theme*
	cp -f numix-999-$(TIMESTAMP).tar.gz $(shell rpm --eval "%_sourcedir")/

mock: srpm
	mock -n -D"timestamp $(TIMESTAMP)" --rebuild $(shell rpm --eval "%_srcrpmdir")/numix-999-$(TIMESTAMP)*.src.rpm

tag: check
	git tag $(TIMESTAMP)
	git push origin $(TIMESTAMP)

check:
	if [ "$(TIMESTAMP)" == "none" ]; then \
		echo "ERROR: TIMESTAMP not set"; \
		exit 1; \
	fi
