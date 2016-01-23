TIME=$(shell date -u +%s)

srpm:
	rpmbuild -bs numix.spec

mock:
	mock -n --rebuild $(shell rpmbuild -bs numix.spec | cut -d: -f2)

tag:
	git tag $(TIME)
	git push origin $(TIME)
