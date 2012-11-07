Name:		nepomuk-core
Summary:	Nepomuk core utilities and libraries
Version: 4.9.3
Release: 1
Epoch:		1
Group:		Graphical desktop/KDE
License:	GPLv2 GPLv3 LGPLv2 LGPLv3
URL:		http://www.kde.org
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	kde4-macros
BuildRequires:	kdelibs4-devel
BuildRequires:	doxygen
BuildRequires:	pkgconfig(soprano) >= 2.7.57
BuildRequires:	pkgconfig(libstreams) >= 0.7.3
BuildRequires:	pkgconfig(shared-desktop-ontologies) >= 0.9
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
%{_kde_libdir}/kde4/nepomukbackupsync.so
%{_kde_libdir}/kde4/nepomukfileindexer.so
%{_kde_libdir}/kde4/nepomukfilewatch.so
%{_kde_libdir}/kde4/nepomukqueryservice.so
%{_kde_libdir}/kde4/nepomukstorage.so
%{_kde_libdir}/libkdeinit4_nepomukserver.so
%{_kde_libdir}/libnepomukcommon.so
%{_kde_services}/*.desktop
%{_kde_servicetypes}/*.desktop

#----------------------------------------------------------------------------------

%define nepomukcore_major 4
%define libnepomukcore %mklibname nepomukcore %{nepomukcore_major}

%package -n %{libnepomukcore}
Summary:	Nepomuk core library
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libnepomukcore}
Nepomuk core library.

%files -n %{libnepomukcore}
%{_kde_libdir}/libnepomukcore.so.%{nepomukcore_major}*

#----------------------------------------------------------------------------------

%define nepomuksync_major 4
%define libnepomuksync %mklibname nepomuksync %{nepomuksync_major}

%package -n %{libnepomuksync}
Summary:	Nepomuk core library
Group:		System/Libraries
Requires:	%{name} = %{EVRD}

%description -n %{libnepomuksync}
Nepomuk core library.

%files -n %{libnepomuksync}
%{_kde_libdir}/libnepomuksync.so.%{nepomuksync_major}*

#----------------------------------------------------------------------------------

%package devel
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{libnepomuksync} = %{EVRD}
Requires:	%{libnepomukcore} = %{EVRD}
Conflicts:	kdebase4-runtime-devel < 1:4.8.80

%description devel
This package includes the header files needed to develop applications
that use Nepomuk.

%files devel
%{_kde_includedir}/nepomuk2
%{_kde_includedir}/Nepomuk2
%{_kde_libdir}/libnepomukcore.so
%{_kde_libdir}/libnepomuksync.so
%{_libdir}/cmake/NepomukCore/*.cmake

#----------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4

%install
%makeinstall_std -C build

