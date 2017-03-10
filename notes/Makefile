
install:
	install -d $(datadir)/alt-notes
	cp -a livecd-*.html $(datadir)/alt-notes
	cp -a release-notes.*.html $(datadir)/alt-notes
	for relnotes in release-notes.*.html; do \
		suffix="$${relnotes#release-notes.}"; \
		ln -s $$relnotes $(datadir)/alt-notes/livecd-finish.$$suffix; \
	done
	install -d $(datadir)/branding-data-current/alt-notes
	cp -a license.*.html $(datadir)/branding-data-current/alt-notes
