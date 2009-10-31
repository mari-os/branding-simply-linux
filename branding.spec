%define theme slinux
%define Name Simply GNU/Linux
%define codename Billy
%define status %nil
%define variants altlinux-office-desktop altlinux-office-server altlinux-desktop

Name: branding-simply-linux
Version: 5.0.0
Release: alt8
BuildArch: noarch

BuildRequires: cpio gfxboot >= 4 fonts-ttf-dejavu
BuildRequires: design-bootloader-source >= 5.0-alt2

BuildRequires(pre): libqt4-core 
BuildRequires: libalternatives-devel
BuildRequires: libqt4-devel

BuildRequires: ImageMagick fontconfig

Packager: Denis Koryavov <dkoryavov@altlinux.org>

Source: %name-%version.tar

Group: Graphics
Summary: System/Base
License: GPL

%description
Distro-specific packages with design and texts for Simply GNU/Linux distribution.

%description -l ru_RU.UTF-8
Пакеты, для дистрибутива "Просто Линукс" (Simply GNU/Linux)

%package bootloader
Group: System/Configuration/Boot and Init
Summary: Graphical boot logo for lilo and syslinux
Summary(ru_RU.UTF-8): Тема для экрана выбора вариантов загрузки (lilo и syslinux) 
License: GPL

PreReq: coreutils
Provides: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme branding-alt-%theme-bootloader

Obsoletes: design-bootloader-system-%theme design-bootloader-livecd-%theme design-bootloader-livecd-%theme design-bootloader-%theme branding-alt-%theme-bootloader
Conflicts: %(for n in %variants ; do [ "$n" = %theme ] || echo -n "branding-$n-bootloader ";done )

%description bootloader
Here you find the graphical boot logo for Simply GNU/Linux distribution. 
Suitable for both lilo and syslinux.

%description bootloader -l ru_RU.UTF-8
В данном пакете находится тема для экрана выбора вариантов загрузки (lilo и syslinux) 
для дистрибутива "Просто Линукс" (Simply GNU/Linux). 

%package bootsplash
Summary: Theme for splash animations during bootup
Summary(ru_RU.UTF-8): Тема для экрана загрузки для дистрибутива "Просто Линукс"
License: Distributable
Group:  System/Configuration/Boot and Init
Provides: design-bootsplash design-bootsplash-%theme  branding-alt-%theme-bootsplash
Requires: bootsplash >= 3.3
Obsoletes:  branding-alt-%theme-bootsplash

Conflicts: %(for n in %variants ; do [ "$n" = %theme ] || echo -n "branding-$n-bootsplash ";done )

%description bootsplash
This package contains graphics for boot process for Simply GNU/Linux
(needs console splash screen enabled).

%description bootsplash -l ru_RU.UTF-8
В данном пакете находится тема для экрана загрузки для дистрибутива 
"Просто Линукс" (Simply GNU/Linux). 

%package alterator
Summary: Design for alterator for Simply GNU/Linux 
Summary(ru_RU.UTF-8): Тема для "Центра управления системой" и QT для дистрибутива "Просто Линукс"
License: GPL
Group: System/Configuration/Other
Packager: Denis Koryavov <dkoryavov@altlinux.org>
Provides: design-alterator-browser-%theme  branding-alt-%theme-browser-qt branding-altlinux-%theme-browser-qt
Provides: alterator-icons design-alterator design-alterator-%theme
Obsoletes:  branding-alt-%theme-browser-qt  branding-altlinux-%theme-browser-qt 

Conflicts: %(for n in %variants ; do [ "$n" = %theme ] || echo -n "branding-$n-browser-qt ";done )
Obsoletes: design-alterator-server design-alterator-desktop design-altertor-browser-desktop  design-altertor-browser-server 
PreReq(post,preun): alternatives >= 0.2 alterator

%description alterator
Design for QT and web alterator for Simply GNU/Linux.

%description alterator -l ru_RU.UTF-8
В данном пакете находится тема для "Центра управления системой" (Alterator)
и модулей библиотеки QT для дистрибутива "Просто Линукс" (Simply GNU/Linux). 

%package graphics
Summary: Design for Simply GNU/Linux
Summary(ru_RU.UTF-8): Тема для дистрибутива "Просто Линукс"
License: Different licenses
Group: Graphics

Provides: design-graphics-%theme  branding-alt-%theme-graphics
Obsoletes:  branding-alt-%theme-graphics design-graphics-%theme
PreReq(post,preun): alternatives >= 0.2
Conflicts: %(for n in %variants ; do [ "$n" = %theme ] || echo -n "branding-$n-graphics ";done )

%description graphics
This package contains some graphics for Simply GNU/Linux design.

%description graphics -l ru_RU.UTF-8
В данном пакете находится необходимые графические элементы для дистрибутива 
"Просто Линукс" (Simply GNU/Linux). 


%define provide_list altlinux fedora redhat system altlinux
%define obsolete_list altlinux-release fedora-release redhat-release
%define conflicts_list altlinux-release-sisyphus altlinux-release-4.0 altlinux-release-junior altlinux-release-master altlinux-release-server altlinux-release-terminal altlinux-release-small_business
%package release

Summary: Simply GNU/Linux release file
Summary(ru_RU.UTF-8): Описание дистрибутива "Просто Линукс"
Copyright: GPL
Group: System/Configuration/Other
Packager: Denis Koryavov <dkoryavov@altlinux.org>
Provides: %(for n in %provide_list; do echo -n "$n-release = %version-%release "; done) altlinux-release-%theme  branding-alt-%theme-release
Obsoletes: %obsolete_list  branding-alt-%theme-release
Conflicts: %conflicts_list
Conflicts: %(for n in %variants ; do [ "$n" = %theme ] || echo -n "branding-$n-release ";done )

%description release
Simply GNU/Linux %version release file.

%description release -l ru_RU.UTF-8
В данном пакете находится описание версии %version дистрибутива 
"Просто Линукс" (Simply GNU/Linux).

%package notes
Provides: alt-license-theme = %version alt-notes-%theme
Obsoletes: alt-license-%theme alt-notes-%theme
Summary: Distribution license and release notes
Summary(ru_RU.UTF-8): Лицензия и дополнительные сведения для дистрибутива "Просто Линукс"
License: Distributable
Group: Documentation
Conflicts: alt-notes-children alt-notes-hpc alt-notes-junior alt-notes-junior-sj alt-notes-junior-sm alt-notes-school-server alt-notes-server-lite alt-notes-skif alt-notes-terminal 
Conflicts: %(for n in %variants ; do [ "$n" = %theme ] || echo -n "branding-$n-notes ";done )

%description notes
Distribution license and release notes

%description notes -l ru_RU.UTF-8
В данном пакете находится лицензия и дополнительные сведения для версии %version 
дистрибутива "Просто Линукс" (Simply GNU/Linux).


%package slideshow
Summary: Slideshow for Simply GNU/Linux %version installer.
Summary(ru_RU.UTF-8): Изображения для организации "слайдшоу" в установщике дистрибутива "Просто Линукс"
License: Distributable
Group: System/Configuration/Other 
Conflicts: %(for n in %variants ; do [ "$n" = %theme ] || echo -n "branding-$n-slideshow ";done )

%description slideshow
Slideshow for Simply GNU/Linux %version installer.

%description slideshow -l ru_RU.UTF-8
В данном пакете находятся изображения для организации "слайдшоу" в установщике 
дистрибутива "Просто Линукс" (Simply GNU/Linux).

%package indexhtml
Summary: Simply GNU/Linux html welcome page
Summary(ru_RU.UTF-8): Стартовая страница для дистрибутива "Просто Линукс"
License: distributable
Group: System/Base
Provides: indexhtml indexhtml-%theme = %version indexhtml-Desktop = 1:5.0
Obsoletes: indexhtml-desktop indexhtml-Desktop

Conflicts: indexhtml-sisyphus
Conflicts: indexhtml-school_junior
Conflicts: indexhtml-school_lite
Conflicts: indexhtml-school_master
Conflicts: indexhtml-school_terminal
Conflicts: indexhtml-small_business
Conflicts: indexhtml-school-server

Requires: xdg-utils 
Requires(post): indexhtml-common

%description indexhtml
Simply GNU/Linux index.html welcome page.

%description indexhtml -l ru_RU.UTF-8
В данном пакете содержится стартовая страница для дистрибутива 
"Просто Линукс" (Simply GNU/Linux).


%prep
%setup -q


%build
autoconf
THEME=%theme NAME='%Name' STATUS=%status VERSION=%version ./configure 
make

#bootloader
    pushd design-bootloader-source/
    DEFAULT_LANG='--lang-to-subst--' PATH=$PATH:/usr/sbin %make
    popd

#altarator
    pushd alterator
    %make_build
    popd

%install
#bootloader
    pushd design-bootloader-source
    install -d -m 755 %buildroot/boot/splash/%theme
    install -d -m 755 %buildroot/%_datadir/gfxboot/%theme
    install -m 644 message %buildroot/boot/splash/%theme
    install -m 644 bootlogo %buildroot%_datadir/gfxboot/%theme
    popd

#bootsplash
## create directory structure
mkdir -p $RPM_BUILD_ROOT/%_sysconfdir/bootsplash/themes/%theme
cp -a bootsplash/* $RPM_BUILD_ROOT%_sysconfdir/bootsplash/themes/%theme

pushd $RPM_BUILD_ROOT%_sysconfdir/bootsplash/themes/%theme/config
#for i in 1 2 3 4 5 11; do \
for i in 1; do \
 for f in bootsplash-*.cfg; do \
    res=`echo "$f"| sed 's|.*\-\(.*\)\.cfg|\1|'`
    ln -s $f vt${i}-${res}.cfg
 done
done
popd

#alterator
pushd alterator
mkdir -p %buildroot/usr/share/alterator-browser-qt/design

install theme.rcc %buildroot/usr/share/alterator-browser-qt/design/%theme.rcc

mkdir -p %buildroot/usr/share/alterator/design/
cp -a images %buildroot/usr/share/alterator/design/
cp -a styles %buildroot/usr/share/alterator/design/
popd

mkdir -p %buildroot/%_altdir
cat >%buildroot/%_altdir/%name-browser-qt <<__EOF__
/etc/alterator/design-browser-qt	/usr/share/alterator-browser-qt/design/%theme.rcc 50
__EOF__

#graphics
mkdir -p %buildroot/%_datadir/design/{%theme,backgrounds}
mkdir -p %buildroot/%_iconsdir
install graphics/icons/altlinux.png %buildroot/%_iconsdir/altlinux.png
cp -ar graphics/* %buildroot/%_datadir/design/%theme

pushd %buildroot/%_datadir/design/%theme
    pushd backgrounds
	ln -sf ../../../wallpapers more
    popd
popd


install -d %buildroot//etc/alternatives/packages.d
cat >%buildroot/etc/alternatives/packages.d/%name-graphics <<__EOF__
%_datadir/artworks	%_datadir/design/%theme 10	
%_datadir/design-current	%_datadir/design/%theme	10
%_datadir/design/current	%_datadir/design/%theme	10
__EOF__

#release
install -pD -m644 /dev/null %buildroot%_sysconfdir/buildreqs/packages/ignore.d/%name-release
echo "%Name %version %status (%codename)" >%buildroot%_sysconfdir/altlinux-release
for n in fedora redhat system; do
	ln -s altlinux-release %buildroot%_sysconfdir/$n-release
done

#notes
pushd notes
%makeinstall
popd

#slideshow
mkdir -p %buildroot/usr/share/install2/slideshow
install slideshow/*  %buildroot/usr/share/install2/slideshow/

#indexhtml
%define _altdocsdir %_defaultdocdir/alt-docs
%define _indexhtmldir %_defaultdocdir/indexhtml
pushd indexhtml
mkdir -p %buildroot{%_indexhtmldir/,%_desktopdir/}
cp -r * %buildroot%_indexhtmldir/
rm -f %buildroot%_indexhtmldir/*.in
touch %buildroot%_indexhtmldir/index.html
popd
install -m644 indexhtml.desktop %buildroot%_desktopdir/

#bootloader
%pre bootloader
[ -s /boot/splash/%theme ] && rm -rf  /boot/splash/%theme ||:

%post bootloader
%__ln_s -nf %theme/message /boot/splash/message
. /etc/sysconfig/i18n
lang=$(echo $LANG | cut -d. -f 1)
cd boot/splash/%theme/
echo $lang > lang
[ "$lang" = "C" ] || echo lang | cpio -o --append -F message


%preun bootloader
[ $1 = 0 ] || exit 0
[ "`readlink /boot/splash/message`" != "%theme/message" ] ||
    %__rm -f /boot/splash/message

%post indexhtml
%_sbindir/indexhtml-update

%files bootloader
%_datadir/gfxboot/%theme
/boot/splash/%theme

#bootsplash
%post bootsplash
%__ln_s -nf %theme %_sysconfdir/bootsplash/themes/current

%preun bootsplash
[ $1 = 0 ] || exit 0
[ "`readlink %_sysconfdir/bootsplash/themes/current`" != %theme ] ||
    %__rm -f %_sysconfdir/bootsplash/themes/current


%files alterator
%config %_altdir/%name-browser-qt
/usr/share/alterator-browser-qt/design/%theme.rcc
/usr/share/alterator/design/*

%files graphics
%config /etc/alternatives/packages.d/%name-graphics
%_datadir/design
%_iconsdir/altlinux.png

%files bootsplash
%_sysconfdir/bootsplash/themes/%theme/


%files release
%_sysconfdir/*-*
%_sysconfdir/buildreqs/packages/ignore.d/*

%files notes
%_datadir/alt-notes/*


%files slideshow
/usr/share/install2/slideshow

%files indexhtml
%ghost %_indexhtmldir/index.html
%_indexhtmldir/*
%_desktopdir/*

%changelog
* Sun Oct 25 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0.0-alt8
- Changed colors for bootsplash.
- Changed license page fonts.
- Changed logo for slideshow.

* Sat Oct 17 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0.0-alt7
- Simply Linux 5.0 RC3 release.

* Wed Oct 14 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0.0-alt6
- Added new bootloader theme.

* Sun Oct 04 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0.0-alt5
- Simply Linux RC2.

* Tue Sep 08 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0.0-alt4
- Removed misspellings in bootsplash text for 640x480 and 800x600 modes

* Wed Aug 19 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0.0-alt3
- Added brand icon an Russian description for package.

* Thu Aug 13 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0.0-alt2
- Update for bootsplash. 

* Sat Jun 13 2009 Denis Koryavov <dkoryavov@altlinux.org> 5.0.0-alt1
- Fork from branding-altlinux-lite

* Wed Apr 01 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt5
- logo in www design fixed 

* Tue Mar 31 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt4
- www design fixed 

* Tue Mar 31 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt3
- conflicts for -alterator subpackages added
- design for web alterator changed

* Mon Mar 30 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt2
- -browser-qt subpackage remaned to -alterator as it really is

* Fri Mar 27 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0.0-alt1
- addes \%status to altlinux-release
- images for verbose bootsplash mode from one source

* Wed Mar 25 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt24
- added versioned provides for indexhtml 

* Tue Mar 24 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt23
- indexhtml subpackage added 

* Mon Mar 23 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt22
- Lite version 

* Wed Mar 18 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt21
- other images for browser-qt added
- gtkrcs added into kde4-settings
- plasma-applet-networkmanagenemt removed from kde4 by default
- conflicts bitween different brandings added

* Thu Mar 05 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt20
- steps icons added 

* Fri Feb 27 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt19
- sample slideshow added

* Wed Feb 25 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt18
- 1024x768 removed :D
- more transparent menu selection bar

* Tue Feb 24 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt17
- 1024x768 added 
- fonts changed

* Thu Feb 19 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt16
- not setup language in bootloader during install (when it is 'C') 

* Wed Feb 18 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt15
- rebuild with new bootloader-source with support of real language change 

* Tue Feb 17 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt14
- auto set default language for bootloader from /etc/sysconfig/i18n 

* Mon Feb 16 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt13
- rebuild for fix oversized /boot/splash/message 

* Fri Feb 13 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt12
- default language set to ru_RU for system boot 

* Wed Feb 11 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt11
- fixed conflict of notes subpackage with itself 

* Tue Feb 10 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt10
- more kde4 settings from zerg@ 
- alternative and obsoletes for graphics added

* Thu Feb 05 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt9
- rebuild with new translations 

* Thu Feb 05 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt8
- added kde4-settings subpackage 

* Wed Feb 04 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt7
- added conflicts for notes 

* Mon Jan 26 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt6
- xdm background fixed 

* Fri Jan 23 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt5
- added 'notes' subpackage 

* Thu Jan 15 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt4
- fixed problem with owerwritten alternative 

* Wed Jan 14 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt3
- release subpackage added 

* Fri Dec 26 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt2
- colors integration
- graphics package added

* Thu Dec 18 2008 Anton V. Boyarshinov <boyarsh@altlinux.ru> 5.0-alt1
- initial sceleton 

