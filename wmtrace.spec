Summary:	wmtrace - window manager tracer
Summary(pl.UTF-8):	wmtrace - "śledzący" zarządca okien
Name:		wmtrace
Version:	1.1
Release:	1
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://insitu.lri.fr/~chapuis/software/wmtrace/%{name}-%{version}.tar.bz2
# Source0-md5:	5e919008d1f05af9148a7bbfc7b8cd79
URL:		http://insitu.lri.fr/~chapuis/software/wmtrace/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmtrace is a window manager tracer for a UNIX system. It logs your
activity, but preserve your private life (e.g., the logs say that you
use mozilla, but the web pages you browse are not logged, etc.).

%description -l pl.UTF-8
wmtrace to "śledzący" zarządca okien dla systemów uniksowych. Śledzi
aktywność użytkownika, ale zachowując przy tym jego prywatność (np.
logi pokazują, że użytkownik używa mozilli, lecz przeglądane strony
nie są logowane itp.).

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%banner %{name} -e << EOF
wmtrace needs the XRecord extension. You should have the line: 
		load \"record\"
in the module section of your X configuration file
EOF

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
