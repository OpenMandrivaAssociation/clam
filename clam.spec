%define soname 1.4
%define libname %mklibname %{name}%{soname}
%define develname %mklibname %{name} -d

Name: clam
Version: 1.4.0
Release: 2
Summary: A C++ Library for Audio and Music
URL: http://clam-project.org/
Group: System/Libraries
License: GPL
Source: http://clam-project.org/download/src/CLAM-%{version}.tar.gz
Patch0: clam-1.4.0-lib64.patch
Patch1: %{name}-1.4.0-gcc46.patch
Patch2: clam-1.4.0-link.patch
BuildRequires: scons xerces-c28-devel libid3-devel ladspa-devel
BuildRequires: libvorbis-devel libsndfile-devel libmad-devel zlib-devel
BuildRequires: fftw-devel libportaudio-devel
BuildRoot: %{_tmppath}/%{name}-%{version}-root

%description
CLAM is a full-fledged software framework for research and application
development in the Audio and Music Domain. It offers a conceptual model
as well as tools for the analysis, synthesis and processing of audio signals.

%package -n %{libname}
Group: System/Libraries
Summary: A C++ Library for Audio and Music

%description -n %{libname}
CLAM is a full-fledged software framework for research and application
development in the Audio and Music Domain. It offers a conceptual model
as well as tools for the analysis, synthesis and processing of audio signals.

This package contains the shared libraries for libclam-core,
libclam-processing and libclam-audioio.


%package -n %{develname}
Group: Development/C
Summary: Development components for CLAM
Requires: %{libname} = %{version}-%{release}
Provides: lib%{name}-devel = %{version}-%{release}

%description -n %{develname}
CLAM is a full-fledged software framework for research and application
development in the Audio and Music Domain. It offers a conceptual model
as well as tools for the analysis, synthesis and processing of audio signals.

This package contains the development components for libclam-core,
libclam-processing and libclam-audioio.


%prep
%setup -q -n CLAM-%{version}
%patch0 -p0 -b .lib64
%patch1 -p1 -b .gcc46
%patch2 -p0 -b .link

%build
mkdir -p %{buildroot}%{_prefix}
scons configure \
  prefix=%{_prefix} \
  prefix_for_packaging=%{buildroot}%{_prefix} \
  release=yes
%scons

%install
mkdir -p %{buildroot}%{_prefix}
scons install

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(0644,root,root,0755)
%doc CHANGES
%{_libdir}/*.so.1.4.0

%files -n %{develname}
%defattr(0644,root,root,0755)
%{_includedir}/CLAM
%{_libdir}/pkgconfig/*.pc
%{_datadir}/clam
%{_libdir}/*.so
%{_libdir}/*.so.1.4
