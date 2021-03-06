Name:           linux-hidl
Summary:        This builds and generates HIDL headers and binaries.
Version:        0.0.1
Release:        1
Group:          Applications/Multimedia
License:        Unknown
URL:            https://gitlab.com/ubports/core/hybris-support/linux-hidl
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  cmake >= 3.10
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  protobuf-devel
BuildRequires:  openssl-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  libcap-devel
BuildRequires:  pkgconfig(android-headers)
BuildRequires:  safe-iop
Patch0:         0001-hidl-Add-building-and-generating-for-HIDL-headers-src-and.patch
Patch1:         0002-hidl-Fix-bulding-on-gcc5.patch
Patch2:         0003-hidl-MakeParentHierarchy-avoid-race-condition-between-sta.patch
Patch3:         0004-libhidl-Add-building-and-generating-for-HIDL-headers-src-and.patch
Patch4:         0005-libhidl-Fix-bulding-on-gcc5.patch
Patch5:         0006-libfmq-Add-building-and-generating-for-HIDL-headers-src-and.patch
Patch6:         0007-libhwbinder-Add-building-and-generating-for-HIDL-headers-src-and.patch
Patch7:         0008-libhwbinder-Fix-bulding-on-gcc5.patch
Patch8:         0009-libhwbinder-Make-sure-we-define-__ANDROID__-in-hwbinder.patch
Patch9:         0010-systemcore-Add-building-and-generating-for-HIDL-headers-src-and.patch
Patch10:        0011-systemcore-base-define-__BIONIC__-for-properties-code.patch
Patch11:        0012-systemcore-Fix-bulding-on-gcc5.patch
Patch12:        0013-systemcore-liblog-fix-compilation-with-GCC-5.patch
Patch13:        0014-hardware-interfaces-cmakelist.patch
Patch14:        0015-hidl-cmakelist.patch
Patch15:        0016-libfmq-cmakelist.patch
Patch16:        0017-libhidl-cmakelist.patch
Patch17:        0018-libhwbinder-cmakelist.patch
Patch18:        0019-systemcore-cmakelist.patch
Patch19:        0020-add-android-headers.patch
Patch20:        0021-system_core-libutils-remove-vector-const.patch
Patch21:        0022-system_core-libcutils-add-throw.patch

%description
This builds and generates HIDL headers and binaries. This is work in progress, expect bugs and failures!

%package devel
Summary: linux-hidl devel package
Requires:  linux-hidl = %{version}-%{release}

%description devel
%{summary}

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
%cmake
%make_build

%install
%make_install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_bindir}/*
%{_libdir}/*.so*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
