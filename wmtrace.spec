Summary:	wmtrace - window manager tracer
Summary(pl):	wmtrace - "¶ledz±cy" window manager
Name:		wmtrace
Version:	1.1
Release:	0.8
License:	GPL
Group:		X11/Window Managers/Tools
Source0:	http://insitu.lri.fr/~chapuis/software/wmtrace/%{name}-%{version}.tar.bz2
# Source0-md5:	5e919008d1f05af9148a7bbfc7b8cd79
URL:		http://insitu.lri.fr/~chapuis/software/wmtrace/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
wmtrace is a window manager tracer for a UNIX system. It logs your
activity, but preserve your private life (e.g., the logs say that you
use mozilla, but the web pages you browse are not logged, etc.).

%description -l pl
wmtrace to "¶ledz±cy" window manager dla systemów uniksowych. ¦ledzi
aktywno¶æ u¿ytkownika, ale zachowuj±c przy tym jego prywatno¶æ. 
(n.p., logi pokazuj±, ¿e u¿ytkownik u¿ywa mozilli lecz przegl±dane strony 
nie s± logowane, itp.).

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

%files
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_bindir}/*
