Summary:	Nepomuk core utilities and libraries
Name:		nepomuk-core
Version:	4.14.3
Release:	8
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
BuildRequires:	pkgconfig(exiv2)
BuildRequires:	pkgconfig(libavcodec)
BuildRequires:	pkgconfig(libavdevice)
BuildRequires:	pkgconfig(libavfilter)
BuildRequires:	pkgconfig(libavformat)
BuildRequires:	pkgconfig(libavutil)
BuildRequires:	pkgconfig(libpostproc)
BuildRequires:	pkgconfig(libstreams) >= 0.7.3
BuildRequires:	pkgconfig(libswresample)
BuildRequires:	pkgconfig(libswscale)
BuildRequires:	pkgconfig(poppler)
BuildRequires:	pkgconfig(poppler-qt4)
BuildRequires:	pkgconfig(shared-desktop-ontologies) >= 0.11
BuildRequires:	pkgconfig(soprano) >= 2.7.57
BuildRequires:	pkgconfig(taglib)
BuildRequires:	qmake5
BuildRequires:	cmake(KF5I18n)
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
%optional %{_kde_libdir}/kde4/nepomukmobiextractor.so
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
Requires:	%{name}
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
# Setting PATH, MOC, QMAKE, etc. all doesn't help :/
find . -name build.make |while read r; do
	sed -i -e 's,%{_libdir}/qt5/bin/moc,%{_prefix}/lib/qt4/bin/moc,g' "$r"
done
%make

%install
%makeinstall_std -C build
