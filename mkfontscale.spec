#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mkfontscale
Version  : 1.1.2
Release  : 3
URL      : http://xorg.freedesktop.org/releases/individual/app/mkfontscale-1.1.2.tar.gz
Source0  : http://xorg.freedesktop.org/releases/individual/app/mkfontscale-1.1.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: mkfontscale-bin
Requires: mkfontscale-doc
BuildRequires : pkgconfig(fontenc)
BuildRequires : pkgconfig(freetype2)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : pkgconfig(xproto)

%description
mkfontscale creates the fonts.scale and fonts.dir index files used by the
legacy X11 font system.

%package bin
Summary: bin components for the mkfontscale package.
Group: Binaries

%description bin
bin components for the mkfontscale package.


%package doc
Summary: doc components for the mkfontscale package.
Group: Documentation

%description doc
doc components for the mkfontscale package.


%prep
%setup -q -n mkfontscale-1.1.2

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/mkfontscale

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
