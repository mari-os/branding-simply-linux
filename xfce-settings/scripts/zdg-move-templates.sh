#!/bin/sh
# Move XDG-Templates.skel/ to XDG_TEMPLATES_DIR.

SKEL_TEMPLATES_DIR="$HOME/XDG-Templates.skel"

if [ -d "$SKEL_TEMPLATES_DIR" -a -f "$HOME/.config/user-dirs.dirs" -a \
	! -L "$SKEL_TEMPLATES_DIR" ]; then

	. "$HOME/.config/user-dirs.dirs"

	if [ -n "$XDG_TEMPLATES_DIR" -a "$XDG_TEMPLATES_DIR" != "$HOME" -a \
		 "$XDG_TEMPLATES_DIR" != "$SKEL_TEMPLATES_DIR" ]; then
		if [ -d "$XDG_TEMPLATES_DIR" ] && rmdir "$XDG_TEMPLATES_DIR" ||
				mkdir -p "${XDG_TEMPLATES_DIR%/*}"; then
			mv "$SKEL_TEMPLATES_DIR" "$XDG_TEMPLATES_DIR" ||:
		fi
	fi
fi
