Summary:	Nepomuk core utilities and libraries
Name:		nepomuk-core
Version:	4.14.3
Release:	1
Epoch:		1
License:	GPLv2 GPLv3 LGPLv2 LGPLv3
Group:		Graphical desktop/KDE
Url:		http://www.kde.org
%define is_beta %(if test `echo %{version} |cut -d. -f3` -ge 70; then echo -n 1; else echo -n 0; fi)
%if %{is_beta}
%define ftpdir unstable
%else
%define ftpdir stable
%endif
Source0:	ftp://ftp.kde.org/pub/kde/%ftpdir/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	doxygen
BuildRequires:	kde4-macros
BuildRequires:	baloo-devel
BuildRequires:	ebook-tools-devel
BuildRequires:	kdelibs4-devel
BuildRequires:	kfilemetadata-devel
BuildRequires:	qmobipocket-devel
BuildRequires:	pkgconfig(soprano) >= 2.7.57
BuildRequires:	pkgconfig(libstreams) >= 0.7.3
BuildRequires:	pkgconfig(shared-desktop-ontologies) >= 0.11
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libavdevice)
BuildRequires:	pkgconfig(libavfilter)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libavutil)
BuildRequires:	pkgconfig(libpostproc)
BuildRequires:	pkgconfig(libswresample)
BuildRequires:	pkgconfig(libswscale)
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(poppler)
BuildRequires:	pkgconfig(poppler-qt4)
BuildRequires:	pkgconfig(taglib)
Requires:	shared-desktop-ontologies >= 0.11
Requires:	soprano >= 4:2.7.57
Conflicts:	kdebase4-runtime < 1:4.8.80

%description
Nepomuk core utilities and libraries.

%files
%doc COPYING*
%{_datadir}/dbus-1/interfaces/*.xml
%{_datadir}/dbus-1/system-services/org.kde.nepomuk.filewatch.service
%{_datadir}/polkit-1/actions/org.kde.nepomuk.filewatch.policy
%{_sysconfdir}/dbus-1/system.d/org.kde.nepomuk.filewatch.conf
%{_kde_applicationsdir}/*.desktop
%{_kde_appsdir}/fileindexerservice
%{_kde_appsdir}/nepomukfilewatch
%{_kde_appsdir}/nepomukstorage
%{_kde_bindir}/nepomuk*
%{_kde_datadir}/autostart/*.desktop
%{_kde_datadir}/ontology/kde/*
%{_kde_libdir}/kde4/nepomukepubextractor.so
%{_kde_libdir}/kde4/nepomukexiv2extractor.so
%{_kde_libdir}/kde4/nepomukffmpegextractor.so
%{_kde_libdir}/kde4/nepomukmobiextractor.so
%{_kde_libdir}/kde4/nepomukodfextractor.so
%{_kde_libdir}/kde4/nepomukoffice2007extractor.so
%{_kde_libdir}/kde4/nepomukofficeextractor.so
%{_kde_libdir}/kde4/nepomukplaintextextractor.so
%{_kde_libdir}/kde4/nepomukpopplerextractor.so
%{_kde_libdir}/kde4/nepomuktaglibextractor.so
%{_kde_libdir}/kde4/libexec/kde_nepomuk_filewatch_raiselimit
%{_kde_libdir}/libkdeinit4_nepomukserver.so
%{_kde_libdir}/libnepomukcommon.so
%{_kde_libdir}/libnepomukextractor.so
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
%rename %{libnepomuksync}

%description -n %{libnepomukcore}
Nepomuk core library.

%files -n %{libnepomukcore}
%{_kde_libdir}/libnepomukcore.so.%{nepomukcore_major}*

#----------------------------------------------------------------------------------

%define nepomukcleaner_major 4
%define libnepomukcleaner %mklibname nepomukcleaner %{nepomukcleaner_major}

%package -n %{libnepomukcleaner}
Summary:	Nepomuk cleaner library
Group:		System/Libraries

%description -n %{libnepomukcleaner}
Nepomuk cleaner library.

%files -n %{libnepomukcleaner}
%{_kde_libdir}/libnepomukcleaner.so.%{nepomukcleaner_major}*

#----------------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{name} = %{EVRD}
Requires:	%{libnepomukcore} = %{EVRD}
Requires:	%{libnepomukcleaner} = %{EVRD}
Conflicts:	kdebase4-runtime-devel < 1:4.8.80

%description devel
This package includes the header files needed to develop applications
that use Nepomuk.

%files devel
%{_kde_includedir}/nepomuk2
%{_kde_includedir}/Nepomuk2
%{_kde_libdir}/libnepomukcore.so
%{_kde_libdir}/libnepomukcleaner.so
%{_libdir}/cmake/NepomukCore

#----------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4

%install
%makeinstall_std -C build

%changelog
* Tue Jul 15 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.3-1
- New version 4.13.3

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.2-2
- Add baloo-devel and kfilemetadata-devel to BuildRequires

* Wed Jun 11 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.13.2-1
- New version 4.13.2

* Wed Apr 02 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.4-1
- New version 4.12.4

* Tue Mar 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.3-1
- New version 4.12.3

* Tue Feb 04 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.2-1
- New version 4.12.2

* Tue Jan 14 2014 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.12.1-1
- New version 4.12.1
- Add qmobipocket-devel to BuildRequires, update files

* Wed Dec 04 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.4-1
- New version 4.11.4

* Wed Nov 06 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.3-1
- New version 4.11.3

* Wed Oct 02 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.2-1
- New version 4.11.2

* Tue Sep 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.1-1
- New version 4.11.1

* Wed Aug 14 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.11.0-1
- New version 4.11.0
- Add ebook-tools-devel to BuildRequires
- New subpackage for libnepomukcleaner
- Update files list

* Wed Jul 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.5-1
- New version 4.10.5

* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3
- Update files

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Thu Feb 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- New version 4.10.0
- Obsolete libnepomuksync subpackage
- Add more BuildRequires
- Update files

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
