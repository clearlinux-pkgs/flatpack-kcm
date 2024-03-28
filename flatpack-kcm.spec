#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cmake
# autospec version: v5
# autospec commit: c02b2fe
#
# Source0 file verified with key 0xD7574483BB57B18D (jr@jriddell.org)
#
Name     : flatpack-kcm
Version  : 6.0.2
Release  : 5
URL      : https://download.kde.org/stable/plasma/6.0.2/flatpak-kcm-6.0.2.tar.xz
Source0  : https://download.kde.org/stable/plasma/6.0.2/flatpak-kcm-6.0.2.tar.xz
Source1  : https://download.kde.org/stable/plasma/6.0.2/flatpak-kcm-6.0.2.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.1
Requires: flatpack-kcm-data = %{version}-%{release}
Requires: flatpack-kcm-lib = %{version}-%{release}
Requires: flatpack-kcm-license = %{version}-%{release}
Requires: flatpack-kcm-locales = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-kde
BuildRequires : extra-cmake-modules-data
BuildRequires : kconfig-dev
BuildRequires : kcoreaddons-dev
BuildRequires : ki18n-dev
BuildRequires : pkg-config
BuildRequires : pkgconfig(flatpak)
BuildRequires : qt6base-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
<!---
SPDX-License-Identifier: GPL-2.0-or-later
-->
# Flatpak Permissions Management KCM

%package data
Summary: data components for the flatpack-kcm package.
Group: Data

%description data
data components for the flatpack-kcm package.


%package lib
Summary: lib components for the flatpack-kcm package.
Group: Libraries
Requires: flatpack-kcm-data = %{version}-%{release}
Requires: flatpack-kcm-license = %{version}-%{release}

%description lib
lib components for the flatpack-kcm package.


%package license
Summary: license components for the flatpack-kcm package.
Group: Default

%description license
license components for the flatpack-kcm package.


%package locales
Summary: locales components for the flatpack-kcm package.
Group: Default

%description locales
locales components for the flatpack-kcm package.


%prep
%setup -q -n flatpak-kcm-6.0.2
cd %{_builddir}/flatpak-kcm-6.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1711663881
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%cmake ..
make  %{?_smp_mflags}
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1711663881
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/flatpack-kcm
cp %{_builddir}/flatpak-kcm-%{version}/LICENSES/BSD-2-Clause.txt %{buildroot}/usr/share/package-licenses/flatpack-kcm/07c1ab270255cf247438e2358ff0c18835b6a6ce || :
cp %{_builddir}/flatpak-kcm-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/flatpack-kcm/3630f1ffcec0e075bf446b88c7b507b1287b571d || :
cp %{_builddir}/flatpak-kcm-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/flatpack-kcm/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0 || :
cp %{_builddir}/flatpak-kcm-%{version}/LICENSES/GPL-2.0-only.txt %{buildroot}/usr/share/package-licenses/flatpack-kcm/3cb34cfc72e87654683f2894299adf912d14b284 || :
cp %{_builddir}/flatpak-kcm-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/flatpack-kcm/3cb34cfc72e87654683f2894299adf912d14b284 || :
cp %{_builddir}/flatpak-kcm-%{version}/LICENSES/GPL-3.0-only.txt %{buildroot}/usr/share/package-licenses/flatpack-kcm/e3bdbf20d43fc066a1b40a64d57d4ae5a31f177f || :
cp %{_builddir}/flatpak-kcm-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/flatpack-kcm/6f1f675aa5f6a2bbaa573b8343044b166be28399 || :
cp %{_builddir}/flatpak-kcm-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/flatpack-kcm/7d9831e05094ce723947d729c2a46a09d6e90275 || :
cp %{_builddir}/flatpak-kcm-%{version}/LICENSES/LicenseRef-KDE-Accepted-GPL.txt %{buildroot}/usr/share/package-licenses/flatpack-kcm/7d9831e05094ce723947d729c2a46a09d6e90275 || :
export GOAMD64=v2
GOAMD64=v2
pushd clr-build
%make_install
popd
%find_lang kcm_flatpak

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/applications/kcm_flatpak.desktop

%files lib
%defattr(-,root,root,-)
/usr/lib64/qt6/plugins/plasma/kcms/systemsettings/kcm_flatpak.so

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/flatpack-kcm/07c1ab270255cf247438e2358ff0c18835b6a6ce
/usr/share/package-licenses/flatpack-kcm/3630f1ffcec0e075bf446b88c7b507b1287b571d
/usr/share/package-licenses/flatpack-kcm/3cb34cfc72e87654683f2894299adf912d14b284
/usr/share/package-licenses/flatpack-kcm/6f1f675aa5f6a2bbaa573b8343044b166be28399
/usr/share/package-licenses/flatpack-kcm/7d9831e05094ce723947d729c2a46a09d6e90275
/usr/share/package-licenses/flatpack-kcm/82da472f6d00dc5f0a651f33ebb320aa9c7b08d0
/usr/share/package-licenses/flatpack-kcm/e3bdbf20d43fc066a1b40a64d57d4ae5a31f177f

%files locales -f kcm_flatpak.lang
%defattr(-,root,root,-)

