srpm:
	rpmbuild -bs numix.spec

mock:
	mock -n --rebuild $(shell rpmbuild -bs numix.spec | cut -d: -f2)
