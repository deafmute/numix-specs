%define gitclone() (git clone --recursive %1 %{_sourcedir}/%{name}-%{version}-%{release})

Name:		numix
Version:	999
Release:	%{timestamp}.git%{?dist}
Summary:	Numix Project
Source0:	%{name}-%{version}-%{timestamp}.tar.gz

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

%package icon-theme-shine
Group: Application/Internet
Summary: Numix Shine Icons
%description icon-theme-shine
Shine is an icon theme for Linux from the Numix project

%package icon-theme-utouch
Group: Application/Internet
Summary: Numix uTouch Icons
%description icon-theme-utouch
uTouch is an icon theme for Linux from the Numix project

%package gtk-theme
Group: Application/Internet
Summary: Numix Gtk Theme
%if %{defined %fedora}
BuildRequires: rubygem-saas glib2 glib2-devel gdk-pixbuf2 gdk-pixbuf2-devel
%else
BuildRequires: rubygems glib2 glib2-devel gdk-pixbuf2 gdk-pixbuf2-devel
%endif
%description gtk-theme
Numix is a modern flat theme with a combination of light and dark elements. It supports Gnome, Unity, XFCE and Openbox.

%prep
%setup -q

%build
%if %{undefined %fedora}
  gem install --user-install sass
%endif
cd %{_sourcedir}/%{name}-%{version}-%{release}/numix-gtk-theme
make

%install
%{__install} -d %{buildroot}%{_datadir}/icons
%{__cp} -r %{_sourcedir}/%{name}-%{version}-%{release}/numix-icon-theme/Numix %{buildroot}%{_datadir}/icons/Numix
%{__cp} -r %{_sourcedir}/%{name}-%{version}-%{release}/numix-icon-theme/Numix-Light %{buildroot}%{_datadir}/icons/Numix-Light
%{__cp} -r %{_sourcedir}/%{name}-%{version}-%{release}/numix-icon-theme-circle/Numix-Circle %{buildroot}%{_datadir}/icons/Numix-Circle
%{__cp} -r %{_sourcedir}/%{name}-%{version}-%{release}/numix-icon-theme-circle/Numix-Circle-Light %{buildroot}%{_datadir}/icons/Numix-Circle-Light
%{__cp} -r %{_sourcedir}/%{name}-%{version}-%{release}/numix-icon-theme-shine/Numix-Shine %{buildroot}%{_datadir}/icons/Numix-Shine
%{__cp} -r %{_sourcedir}/%{name}-%{version}-%{release}/numix-icon-theme-utouch/Numix-uTouch %{buildroot}%{_datadir}/icons/Numix-uTouch
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

%files icon-theme-shine
%doc
%{_datadir}/icons/Numix-Shine

%files icon-theme-utouch
%doc
%{_datadir}/icons/Numix-uTouch

%files gtk-theme
%doc
%{_datadir}/themes/Numix

%changelog
* Tue Nov 10 2015 Sascha Spreitzer <sspreitz@redhat.com>
- Repackaging
- Adding Shine and uTouch
