%define url_ver %(echo %{version}|cut -d. -f1,2)

%define gstapi	1.0
%define api	0.8
%define major	0
%define libname %mklibname %{name} %{api} %{major}
%define girname %mklibname %{name}-gir %{api}
%define devname %mklibname %{name} -d

Summary:	Glib/gobject based library implementing a Genicam interface
Name:		aravis
Version:	0.8.27
Release:	1
License:	GPLv2+
Group:		Development/GNOME and GTK+
Url:		http://www.gnome.org
Source0:	https://github.com/AravisProject/aravis/releases/download/%{version}/aravis-%{version}.tar.xz

BuildRequires:  cmake
BuildRequires:  meson
BuildRequires:	intltool
BuildRequires:	pkgconfig(gobject-introspection-1.0)
BuildRequires:	pkgconfig(gstreamer-%{gstapi})
BuildRequires:	pkgconfig(gstreamer-plugins-base-%{gstapi})
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libusb-1.0)
BuildRequires:  pkgconfig(gtk-doc)
BuildRequires:  pkgconfig(gi-docgen)

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

%package -n gstreamer%{gstapi}-%{name}
Summary:	Gstreamer support for %{name}
Group:		Sound
Obsoletes:	%{name}-gstreamer

%description -n gstreamer%{gstapi}-%{name}
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
%autopatch -p1

%build
%meson

%meson_build

%install
%meson_install

rm -fr %{buildroot}%{_prefix}/doc


%files
%{_bindir}/*
#{_datadir}/%{name}-%{api}
%{_iconsdir}/hicolor/*x*/apps/aravis-%{api}.*
%{_datadir}/applications/arv-viewer-%{api}.desktop
%{_datadir}/metainfo/arv-viewer-%{api}.appdata.xml
#{_mandir}/man1/arv-viewer*
#{_mandir}/man1/arv-tool*
%{_datadir}/locale/*/LC_MESSAGES/aravis-%{api}.mo

%files -n %{libname}
%{_libdir}/libaravis-%{api}.so.%{major}*

%files -n %{girname}
%{_libdir}/girepository-1.0/Aravis-%{api}.typelib

%files -n gstreamer%{gstapi}-%{name}
%{_libdir}/gstreamer-%{gstapi}/libgstaravis.%{api}.so

%files -n %{devname}
#doc %{_datadir}/doc/aravis-%{api}/
%{_includedir}/%{name}-%{api}
%{_libdir}/*.so
%{_libdir}/pkgconfig/*
%{_datadir}/gir-1.0/Aravis-%{api}.gir
