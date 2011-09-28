Summary:	20,000 Light Years Into Space - a real-time strategy game
Summary(pl.UTF-8):	20,000 Light Years Into Space - strategia czasu rzeczywistego
Name:		lightyears
Version:	1.4
Release:	1
License:	GPL v2+
Group:		X11/Applications/Games
Source0:	http://www.jwhitham.org/20kly/%{name}-%{version}.tar.bz2
# Source0-md5:	1211f6c9f368e3d8053965b3e42dcdcd
Source1:	%{name}.desktop
Patch0:		%{name}-config_path.patch
URL:		http://www.jwhitham.org.uk/biscuit_games/LightYears/
%pyrequires_eq	python-modules
BuildRequires:	rpm-pythonprov
BuildRequires:	unzip
Requires:	python-pygame >= 1.7
Obsoletes:	LightYears
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"20,000 Light Years Into Space" is a single-player real-time strategy
game with a "Steampunk" science-fiction theme.

During the game, players must focus on building a steam delivery
network while under attack from various hazards. Once you have solved
the three difficulty levels, you can attack the high score. The game
includes an interactive tutorial and a written manual.

%description -l pl.UTF-8
"20,000 Light Years Into Space" to przeznaczona dla jednego gracza
strategia czasu rzeczywistego z motywem science-fiction "Steampunk".

Podczas gry gracze muszą skupić się na tworzeniu sieci dostarczającej
parę będąc atakowanym przez różne niebezpieczeństwa. Po przejściu
trzech poziomów trudności można starać się o najlepszy wynik. Gra
zawiera interaktywny samouczek i napisany podręcznik.

%prep
%setup -q
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/{data,code} \
		$RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}

cat > $RPM_BUILD_ROOT%{_bindir}/lightyears <<EOF
#!/bin/sh

cd %{_datadir}/%{name} && python %{name}
EOF

cp -a lightyears $RPM_BUILD_ROOT%{_datadir}/%{name}
cp -a code/*.py $RPM_BUILD_ROOT%{_datadir}/%{name}/code
cp -a data/* $RPM_BUILD_ROOT%{_datadir}/%{name}/data

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

find $RPM_BUILD_ROOT%{_datadir} -name "*.py" -o -name "*.pyo" | xargs rm

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install data/32.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt manual/*.html
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
