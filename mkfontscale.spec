#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xCFDF148828C642A7 (alanc@freedesktop.org)
#
Name     : mkfontscale
Version  : 1.2.2
Release  : 17
URL      : https://www.x.org/releases/individual/app/mkfontscale-1.2.2.tar.gz
Source0  : https://www.x.org/releases/individual/app/mkfontscale-1.2.2.tar.gz
Source1  : https://www.x.org/releases/individual/app/mkfontscale-1.2.2.tar.gz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: mkfontscale-bin = %{version}-%{release}
Requires: mkfontscale-license = %{version}-%{release}
Requires: mkfontscale-man = %{version}-%{release}
BuildRequires : pkgconfig(fontenc)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)

%description
mkfontscale creates the fonts.scale and fonts.dir index files used by the
legacy X11 font system.  It now includes the mkfontdir script previously
distributed separately for compatibility with older X11 versions.

%package bin
Summary: bin components for the mkfontscale package.
Group: Binaries
Requires: mkfontscale-license = %{version}-%{release}

%description bin
bin components for the mkfontscale package.


%package license
Summary: license components for the mkfontscale package.
Group: Default

%description license
license components for the mkfontscale package.


%package man
Summary: man components for the mkfontscale package.
Group: Default

%description man
man components for the mkfontscale package.


%prep
%setup -q -n mkfontscale-1.2.2
cd %{_builddir}/mkfontscale-1.2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1649019150
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1649019150
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mkfontscale
cp %{_builddir}/mkfontscale-1.2.2/COPYING %{buildroot}/usr/share/package-licenses/mkfontscale/113de3dee0fa0a922b52ade0ee2dd98377de34b5
%make_install
## Remove excluded files
rm -f %{buildroot}*/usr/share/man/man1/mkfontdir.1
rm -f %{buildroot}*/usr/bin/mkfontdir

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mkfontscale

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mkfontscale/113de3dee0fa0a922b52ade0ee2dd98377de34b5

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/mkfontscale.1
