Summary:	TicTacToe for WindowMaker
Summary(pl.UTF-8):   Kółko i Krzyżyk dla WindowMakera
Name:		wmtictactoe
Version:	1.1.1
Release:	5
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://atlas.ucpel.tche.br/~acamargo/%{name}-%{version}.tar.gz
# Source0-md5:	2aa54265ec60521437d676c5d251864a
Source1:	%{name}.desktop
Patch0:		%{name}-makefile.patch
Patch1:		%{name}-home_etc.patch
URL:		http://atlas.ucpel.tche.br/~acamargo/wmtictactoe.html
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
wmTicTacToe is a dock application game for Window Maker.

%description -l pl.UTF-8
wmTicTacToe jest grą w Kółko i Krzyżyk, przeznaczoną dla Doku
WindowMakera.

%prep
%setup -q -n %{name}.app
%patch0 -p0
%patch1 -p1

%build
%{__make} -C %{name} \
	CFLAGS="%{rpmcflags} -Wall" \
	LIBDIR="-L/usr/X11R6/%{_lib}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_desktopdir}/docklets}

install %{name}/%{name} $RPM_BUILD_ROOT%{_bindir}
install %{SOURCE1}	$RPM_BUILD_ROOT%{_desktopdir}/docklets


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README TODO
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/docklets/%{name}.desktop
