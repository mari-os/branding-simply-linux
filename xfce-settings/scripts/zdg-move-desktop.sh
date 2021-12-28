#!/bin/sh
# Move XDG-Desktop.skel/ to XDG_DESKTOP_DIR.

SKEL_DESKTOP_DIR="$HOME/XDG-Desktop.skel"

if [ -d "$SKEL_DESKTOP_DIR" -a -f "$HOME/.config/user-dirs.dirs" -a \
	! -L "$SKEL_DESKTOP_DIR" ]; then

	. "$HOME/.config/user-dirs.dirs"

	if [ -n "$XDG_DESKTOP_DIR" -a "$XDG_DESKTOP_DIR" != "$HOME" -a \
		 "$XDG_DESKTOP_DIR" != "$SKEL_DESKTOP_DIR" ]; then
		if [ -d "$XDG_DESKTOP_DIR" ] && rmdir "$XDG_DESKTOP_DIR" ||
				mkdir -p "${XDG_DESKTOP_DIR%/*}"; then
			mv "$SKEL_DESKTOP_DIR" "$XDG_DESKTOP_DIR" ||:
			if [ -f "$XDG_DESKTOP_DIR"/indexhtml.desktop ]; then
				gio set "$XDG_DESKTOP_DIR"/indexhtml.desktop \
				  "metadata::trusted:" yes
				gio set "$XDG_DESKTOP_DIR"/indexhtml.desktop \
				  "metadata::xfce-exe-checksum" \
				  $(sha256sum "$XDG_DESKTOP_DIR"/indexhtml.desktop |
				  cut -f1 -d ' ')
				gio set "$XDG_DESKTOP_DIR"/indexhtml.desktop \
				  "metadata::trust" true
			fi
		fi
	fi

fi
