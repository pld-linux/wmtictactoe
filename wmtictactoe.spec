Summary:	TicTacToe for WindowMaker
Summary(pl):	K�ko i Krzy�yk dla WindowMakera
Name:		wmtictactoe
Version:	1.1.1
Release:	2
License:	GPL
Group:		X11/Window Managers/Tools
Group(de):	X11/Fenstermanager/Werkzeuge
Group(pl):	X11/Zarz�dcy Okien/Narz�dzia
Source0:	http://atlas.ucpel.tche.br/~acamargo/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-home_etc.patch
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6

%description
wmTicTacToe is a dock application game for Window Maker.

%description -l pl
wmTicTacToe jest gr� w K�ko i Krzy�yk, przeznaczon� dla Doku
WindowMakera.

%prep
%setup -q -n %{name}.app
%patch0 -p0
%patch1 -p1

%build
%{__make} -C %{name} CFLAGS="%{rpmcflags} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_applnkdir}/DockApplets}

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1}	$RPM_BUILD_ROOT%{_applnkdir}/DockApplets

gzip -9nf CHANGES README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {CHANGES,README,TODO}.gz
%attr(755,root,root) %{_bindir}/%{name}
%{_applnkdir}/DockApplets/%{name}.desktop
