
Summary:	20,000 Light Years Into Space - a real-time strategy game
Summary(pl):	20,000 Light Years Into Space - gra strategiczna
Name:		LightYears
Version:	1.2
Release:	1
License:	GPL v2
Group:		X11/Applications/Games
Source0:	http://www.jwhitham.org.uk/biscuit_games/LightYears/%{name}-%{version}.zip
# Source0-md5:	f82bb67d14153affc8d9a644cdb25d5b
Source1:	%{name}.desktop
URL:		http://www.jwhitham.org.uk/biscuit_games/LightYears/
%pyrequires_eq	python-modules
Requires:	python-pygame >= 1.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
"20,000 Light Years Into Space" is a single-player real-time strategy
game with a "Steampunk" science-fiction theme.

During the game, players must focus on building a steam delivery
network while under attack from various hazards. Once you have solved
the three difficulty levels, you can attack the high score. The game
includes an interactive tutorial and a written manual.

%prep
%setup -q -n %{name}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/%{name}/{data,code} \
		$RPM_BUILD_ROOT{%{_bindir},%{_desktopdir},%{_pixmapsdir}}

cat > $RPM_BUILD_ROOT%{_bindir}/LightYears <<EOF
#!/bin/sh

cd %{_datadir}/%{name} && python %{name}.pyc
EOF

cp LightYears.py $RPM_BUILD_ROOT%{_datadir}/%{name}
cp code/*.py $RPM_BUILD_ROOT%{_datadir}/%{name}/code
cp -r data/* $RPM_BUILD_ROOT%{_datadir}/%{name}/data

%py_comp $RPM_BUILD_ROOT%{_datadir}/%{name}
%py_ocomp $RPM_BUILD_ROOT%{_datadir}/%{name}

find $RPM_BUILD_ROOT%{_datadir} -name "*.py" -o -name "*.pyo" | xargs rm

install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop
install data/32.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt *.html
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
