%define timestamp() %(date -u +%%s)
%define gitclone() (git clone %1 %{_sourcedir}/%{name}-%{version}-%{release}/%2)

Name:		numix
Version:	999
Release:	%{timestamp}.git%{?dist}
Summary:	Numix Project

Group:		Application/Internet
License:	GPLv3
URL:		http://numixproject.org

BuildRequires:	git
BuildArch:	noarch

%description
blah

%package icon-theme
Group: Application/Internet
Summary: Numix Icons
%description icon-theme
Numix is the official icon theme from the Numix project. 
It is heavily inspired by, and based upon parts of the Elementary, Humanity and Gnome icon themes

%package icon-theme-circle
Group: Application/Internet
Summary: Numix Circle Icons
%description icon-theme-circle
Circle is an icon theme for Linux from the Numix project

%package gtk-theme
Group: Application/Internet
Summary: Numix Gtk Theme
BuildRequires: rubygem-sass glib2 glib2-devel gdk-pixbuf2 gdk-pixbuf2-devel
%description gtk-theme
Numix is a modern flat theme with a combination of light and dark elements. It supports Gnome, Unity, XFCE and Openbox.

%prep
%gitclone https://github.com/numixproject/numix-icon-theme.git numix-icon-theme
%gitclone https://github.com/numixproject/numix-icon-theme-circle.git numix-icon-theme-circle
%gitclone https://github.com/shimmerproject/Numix.git numix-gtk-theme

%build
cd %{_sourcedir}/%{name}-%{version}-%{release}/numix-gtk-theme
make

%install
%{__install} -d %{buildroot}%{_datadir}/icons
%{__cp} -r %{_sourcedir}/%{name}-%{version}-%{release}/numix-icon-theme/Numix %{buildroot}%{_datadir}/icons/Numix
%{__cp} -r %{_sourcedir}/%{name}-%{version}-%{release}/numix-icon-theme/Numix-Light %{buildroot}%{_datadir}/icons/Numix-Light
%{__cp} -r %{_sourcedir}/%{name}-%{version}-%{release}/numix-icon-theme-circle/Numix-Circle %{buildroot}%{_datadir}/icons/Numix-Circle
%{__cp} -r %{_sourcedir}/%{name}-%{version}-%{release}/numix-icon-theme-circle/Numix-Circle-Light %{buildroot}%{_datadir}/icons/Numix-Circle-Light
cd %{_sourcedir}/%{name}-%{version}-%{release}/numix-gtk-theme
make install DESTDIR=%{buildroot}

%files icon-theme
%doc
%{_datadir}/icons/Numix
%{_datadir}/icons/Numix-Light

%files icon-theme-circle
%doc
%{_datadir}/icons/Numix-Circle
%{_datadir}/icons/Numix-Circle-Light

%files gtk-theme
%doc
%{_datadir}/themes/Numix

%changelog
* Tue Nov 10 2015 Sascha Spreitzer <sspreitz@redhat.com>
- Repackaging
