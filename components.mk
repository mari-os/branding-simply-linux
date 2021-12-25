.PHONY: browser-qt ahttpd graphics gfxboot indexhtml gfxboot-install bootsplash-install grub-install system-settings-install xfce-settings-install

# browser-qt
components/browser-qt/design/bg.png: images/installer.png
	convert $< -resize '800x600!' -fill '#c62530' -font /usr/share/fonts/ttf/dejavu/DejaVuSansCondensed-Bold.ttf -style Normal -weight Normal -pointsize 20 -gravity northeast -draw 'text 25,25 "$(STATUS)"' $@

browser-qt: components/browser-qt/design/bg.png
	install -d $(datadir)/alterator-browser-qt/design
	cd components/browser-qt; rcc-qt5 -binary theme.qrc -o $(datadir)/alterator-browser-qt/design/$(THEME).rcc; cd -
	install -d $(sysconfdir)/alternatives/packages.d
	printf '/etc/alterator/design-browser-qt\t/usr/share/alterator-browser-qt/design/$(THEME).rcc\t$(ALTERATOR_BROWSER_WEIGHT)\n'>$(sysconfdir)/alternatives/packages.d/$(THEME).rcc

# ahttpd
ahttpd:
	install -d $(datadir)/alterator/design/styles
	cp -a components/ahttpd/images $(datadir)/alterator/design
#	install -Dpm644 images/product-logo.png $(datadir)/alterator/design/images/product-logo.png
	cp -a components/ahttpd/styles/*.css $(datadir)/alterator/design/styles

graphics:
	convert -colorspace YCbCr -sampling-factor 2x2 images/boot.png JPEG:images/boot.jpg
	for size in 1024x768 800x600 640x480; do \
		convert images/boot.jpg -quality 97 -resize "$$size!" -fill '#c62530' -font /usr/share/fonts/ttf/dejavu/DejaVuSansCondensed-Bold.ttf -style Normal -weight Normal -pointsize 20 -gravity northeast -draw 'text 25,25 "$(STATUS)"' boot-$$size.jpg ;\
	done
# background
	convert images/wallpaper.png -fill '#c62530' -font /usr/share/fonts/ttf/google-droid/DroidSans-Bold.ttf -style Normal -weight Normal -pointsize 20 -gravity northeast -draw 'text 25,25 "$(STATUS)"' wallpaper.png
	cp -al wallpaper.png graphics/backgrounds/default.png
	cp -al wallpaper.png graphics/backgrounds/xdm.png

# gfxboot
gfxboot: graphics
	cp -a  /usr/src/design-bootloader-source ./
	cp -a components/bootloader/config design-bootloader-source/
	cp -a components/bootloader/gfxboot.cfg design-bootloader-source/data-install/
	cp -a components/bootloader/gfxboot.cfg design-bootloader-source/data-boot/
	cp -al boot-800x600.jpg design-bootloader-source/data-boot/back.jpg
	convert images/boot.jpg -resize "800x600!" -fill '#c62530' -font /usr/share/fonts/ttf/dejavu/DejaVuSansCondensed-Bold.ttf -style Normal -weight Normal -pointsize 20 -gravity northeast -draw 'text 25,25 "$(STATUS)"' design-bootloader-source/data-install/back.jpg
	subst 's/label:ALT/label:Simply/g' design-bootloader-source/src/dia_install.inc
	DEFAULT_LANG='--lang-to-subst--' PATH=$(PATH):/usr/sbin make -C design-bootloader-source

# index html page, start page for all local browsers
INDEXHTML_DIR=$(datadir)/doc/indexhtml
indexhtml:
	for i in notes/index*.html components/indexhtml/*.css;do \
	  install -Dpm644 $$i $(INDEXHTML_DIR)/`basename $$i`; \
	done
	install -Dpm644 /dev/null $(INDEXHTML_DIR)/index.html
	cp -a components/indexhtml/images $(INDEXHTML_DIR)
#	install -Dpm644 images/product-logo.png $(INDEXHTML_DIR)/images/product-logo.png
	install -Dpm644 components/indexhtml/indexhtml.desktop $(datadir)/applications/indexhtml.desktop

# gfxboot
gfxboot-install:
	install -d -m 755  $(sysconfdir)/../boot/splash/$(THEME)
	install -d -m 755 $(datadir)/gfxboot/$(THEME)
	install -m 644 design-bootloader-source/message $(sysconfdir)/../boot/splash/$(THEME)
	install -m 644 design-bootloader-source/bootlogo $(datadir)/gfxboot/$(THEME)

#bootsplash
bootsplash-install:
	mkdir -p $(datadir)/plymouth/themes/$(THEME)
	cp -al images/background*.png $(datadir)/plymouth/themes/$(THEME)/
	cp -a components/bootsplash/* $(datadir)/plymouth/themes/$(THEME)
	mv $(datadir)/plymouth/themes/$(THEME)/theme.plymouth $(datadir)/plymouth/themes/$(THEME)/$(THEME).plymouth
	mkdir -p $(datadir)/pixmaps
	mv $(datadir)/plymouth/themes/$(THEME)/system-logo.png $(datadir)/pixmaps/

#grub
grub-install:
	install -d -m 755  $(sysconfdir)/../boot/grub/themes/$(THEME)
	cp -a components/grub2/* $(sysconfdir)/../boot/grub/themes/$(THEME)/
	install -m 644 images/boot.png $(sysconfdir)/../boot/grub/themes/$(THEME)/boot.png


system-settings-install:
	mkdir -p $(datadir)/polkit-1/rules.d/
	cp -a system-settings/polkit-rules/*.rules $(datadir)/polkit-1/rules.d/
	install -Dm644 system-settings/lightdm-gtk-greeter.conf $(datadir)/install3/lightdm-gtk-greeter.conf

xfce-settings-install:
	mkdir -p $(sysconfdir)/skel/XDG-Templates.skel/
	cp -r xfce-settings/etcskel/* $(sysconfdir)/skel/
	cp -r xfce-settings/etcskel/.config $(sysconfdir)/skel/
	cp -r xfce-settings/etcskel/.local $(sysconfdir)/skel/
	cp -r xfce-settings/etcskel/.vimrc $(sysconfdir)/skel/
	cp -r xfce-settings/etcskel/.gtkrc-2.0 $(sysconfdir)/skel/
	install -m 644 xfce-settings/etcskel/.wm-select $(sysconfdir)/skel/
	mkdir -p $(sysconfdir)/skel/XDG-Desktop.skel
	install -Dpm644 components/indexhtml/indexhtml.desktop $(sysconfdir)/skel/XDG-Desktop.skel
	chmod +x $(sysconfdir)/skel/XDG-Desktop.skel/indexhtml.desktop
	# remove templates
	find $(sysconfdir)/skel/ -type f -name '*.in' -delete
# backgrounds
	mkdir -p $(datadir)/backgrounds/xfce/
	install -m 644 xfce-settings/backgrounds/slinux*.png $(datadir)/backgrounds/xfce/
# scripts
	install -pDm0755 xfce-settings/scripts/zdg-move-templates.sh $(sysconfdir)/X11/profile.d/zdg-move-templates.sh
	install -pDm0755 xfce-settings/scripts/zdg-move-desktop.sh $(sysconfdir)/X11/profile.d/zdg-move-desktop.sh
