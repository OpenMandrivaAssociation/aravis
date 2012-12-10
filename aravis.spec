%define api	0.2
%define major	0
%define libname %mklibname %{name} %{api} %{major}
%define girname %mklibname %{name}-gir %{api}
%define devname %mklibname %{name} -d

Summary:	Glib/gobject based library implementing a Genicam interface
Name:		aravis
Version:	0.1.15
Release:	1
License:	GPLv2+
Group:		Development/GNOME and GTK+
URL:		http://www.gnome.org
Source0:	http://ftp.gnome.org/pub/GNOME/sources/aravis/%{name}-%{version}.tar.xz

BuildRequires:	intltool
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gstreamer-0.10)
BuildRequires:	pkgconfig(gstreamer-plugins-base-0.10)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libnotify)

%description
Aravis is a glib/gobject based library implementing a Genicam interface, 
which can be used for the acquisition of video streams coming from either
ethernet, firewire or USB cameras. It currently only implements an ethernet 
camera protocol used for industrial cameras.

%package -n %{libname}
Summary:	Shared library for %{name}
Group:		System/Libraries

%description -n %{libname}
Aravis is a glib/gobject based library implementing a Genicam interface, 
which can be used for the acquisition of video streams coming from either
ethernet, firewire or USB cameras. It currently only implements an ethernet 
camera protocol used for industrial cameras.

This package contains the shared library for %{name}.

%package -n %{girname}
Summary:	GObject Introspection interface description for %{name}
Group:		System/Libraries

%description -n %{girname}
GObject Introspection interface description for %{name}.

%package gstreamer
Summary:	Gstreamer support for %{name}
Group:		Sound

%description gstreamer
This package contains the gstreamer plugin for %{name}.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}
Requires:	%{girname} = %{version}

%description -n %{devname}
This package contains the development files for %{name}

%prep
%setup -q

%build
%configure2_5x \
	--disable-static \
	--enable-gst-plugin \
	--enable-viewer \
	--enable-notify

%make LIBS='-lm -lz'

%install
%makeinstall_std
rm -fr %{buildroot}%{_prefix}/doc

%find_lang %{name}-%{api}

%files -f %{name}-%{api}.lang
%{_bindir}/*
%{_datadir}/%{name}-%{api}

%files -n %{libname}
%doc AUTHORS COPYING NEWS
%{_libdir}/libaravis-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Aravis-%{api}.typelib

%files gstreamer
%{_libdir}/gstreamer-0.10/libgstaravis-%{api}.so

%files -n %{devname}
%{_includedir}/%{name}-%{api}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/Aravis-%{api}.gir
%{_datadir}/gtk-doc/html/%{name}-%{api}



%changelog
* Wed Aug 08 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.1.15-1
+ Revision: 812766
- update to new version 0.1.15

* Wed Jun 20 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.1.14-1
+ Revision: 806349
- imported package aravis

