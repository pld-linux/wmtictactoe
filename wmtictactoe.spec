Summary:	TicTacToe for WindowMaker
Summary(pl):	Kó³ko i Krzy¿yk dla WindowMakera
Name:		wmtictactoe
Version: 	1.0
Release:	2
Copyright:	GPL
Group:		X11/Window Managers/Tools
Group(pl):	X11/Zarz±dcy Okien/Narzêdzia
Source0:	http://atlas.ucpel.tche.br/~acamargo/%{name}-%{version}.tar.gz
Source1:	wmtictactoe.desktop
Patch:		wmtictactoe-makefile.patch
BuildPrereq:	XFree86-devel
BuildPrereq:	xpm-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define _prefix	/usr/X11R6

%description
wmTicTacToe is a dock application game for Window Maker.

%description -l pl
wmTicTacToe jest gr± w Kó³ko i Krzy¿yk, przeznaczon± dla Doku WindowMakera.

%prep
%setup -q -n %{name}.app
%patch -p0

%build
make -C %{name} CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},/etc/X11/applnk/DockApps}
install -s %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/applnk/DockApps

gzip -9nf CHANGES README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,README,TODO}.gz
%attr(755,root,root) %{_bindir}/%{name}
/etc/X11/applnk/DockApps/wmtictactoe.desktop

%changelog
* Thu Jul 8 1999 Piotr Czerwiñski <pius@pld.org.pl> 
  [1.0-2]
- added wmtictactoe.desktop file,
- fixed Makefile (wmtictactoe-makefile.patch),
- minor changes.

* Tue May 25 1999 Piotr Czerwiñski <pius@pld.org.pl> 
  [1.0-1]
- initial RPM release.
