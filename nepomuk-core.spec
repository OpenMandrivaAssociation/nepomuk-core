Name:		nepomuk-core
Summary:	Nepomuk core utilities and libraries
Version:	4.9.98
Release:	1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 GPLv3 LGPLv2 LGPLv3
URL:		http://www.kde.org
%define is_beta %(if test `echo %version |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %is_beta
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source:		ftp://ftp.kde.org/pub/kde/%ftpdir/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kde4-macros
BuildRequires:	kdelibs4-devel
BuildRequires:	doxygen
BuildRequires:	pkgconfig(soprano) >= 2.7.57
BuildRequires:	pkgconfig(libstreams) >= 0.7.3
BuildRequires:	pkgconfig(shared-desktop-ontologies) >= 0.9
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libavdevice)
BuildRequires:	pkgconfig(libavfilter)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libavutil)
BuildRequires:	pkgconfig(libpostproc)
BuildRequires:	pkgconfig(libswresample)
BuildRequires:	pkgconfig(libswscale)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(poppler) pkgconfig(poppler-qt4)
BuildRequires:	pkgconfig(taglib)
Requires:	shared-desktop-ontologies >= 0.9
Requires:	soprano >= 4:2.7.57
Conflicts:	kdebase4-runtime < 1:4.8.80

%description
Nepomuk core utilities and libraries.

%files
%doc COPYING*
%{_datadir}/dbus-1/interfaces/*.xml
%{_kde_applicationsdir}/*.desktop
%{_kde_appsdir}/fileindexerservice
%{_kde_appsdir}/nepomukfilewatch
%{_kde_appsdir}/nepomukstorage
%{_kde_bindir}/nepomuk*
%{_kde_datadir}/autostart/*.desktop
%{_kde_datadir}/ontology/kde/*
%{_kde_libdir}/kde4/nepomukfileindexer.so
%{_kde_libdir}/kde4/nepomukfilewatch.so
%{_kde_libdir}/kde4/nepomukstorage.so
%{_kde_libdir}/kde4/nepomukexiv2extractor.so
%{_kde_libdir}/kde4/nepomukffmpegextractor.so
%{_kde_libdir}/kde4/nepomukplaintextextractor.so
%{_kde_libdir}/kde4/nepomukpopplerextractor.so
%{_kde_libdir}/kde4/nepomuktaglibextractor.so
%{_kde_libdir}/libkdeinit4_nepomukserver.so
%{_kde_libdir}/libnepomukcommon.so
%{_kde_services}/*.desktop
%{_kde_servicetypes}/*.desktop

#----------------------------------------------------------------------------------

%define nepomukcore_major 4
%define libnepomukcore %mklibname nepomukcore %{nepomukcore_major}
%if %{nepomukcore_major} != 4
Please remove all references to libnepomuksync below -- we are not compatible
with it in any way, so we should not claim we are its successor.
%endif
%define libnepomuksync %mklibname nepomuksync %{nepomukcore_major}

%package -n %{libnepomukcore}
Summary:	Nepomuk core library
Group:		System/Libraries
Requires:	%{name} = %{EVRD}
%rename %libnepomuksync

%description -n %{libnepomukcore}
Nepomuk core library.

%files -n %{libnepomukcore}
%{_kde_libdir}/libnepomukcore.so.%{nepomukcore_major}*

#----------------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{libnepomukcore} = %{EVRD}
Requires:	%{libnepomukcore} = %{EVRD}
Conflicts:	kdebase4-runtime-devel < 1:4.8.80

%description devel
This package includes the header files needed to develop applications
that use Nepomuk.

%files devel
%{_kde_includedir}/nepomuk2
%{_kde_includedir}/Nepomuk2
%{_kde_libdir}/libnepomukcore.so
%{_libdir}/cmake/NepomukCore

#----------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4

%install
%makeinstall_std -C build

%changelog
* Wed Dec 05 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.4-1
- New version 4.9.4

* Wed Nov 07 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.3-1
- New version 4.9.3

* Thu Oct 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.2-1
- New version 4.9.2

* Sat Sep 08 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.1-1
- New version 4.9.1

* Sat Aug 04 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.9.0-1
- New version 4.9.0

* Thu Jul 12 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.97-1
- New version 4.8.97
- Convert some BuildRequires to pkgconfig style

* Thu Jun 28 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.95-1
- Update to 4.8.95

* Wed Jun 20 2012 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.8.90-1
- Initial Rosa package
