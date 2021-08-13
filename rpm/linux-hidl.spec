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
Patch0:         0001-hidl-Add-building-and-generating-for-HIDL-headers-src-and.patch
Patch1:         0001-libfmq-Add-building-and-generating-for-HIDL-headers-src-and.patch
Patch2:         0001-libhidl-Add-building-and-generating-for-HIDL-headers-src-and.patch
Patch3:         0001-libhwbinder-Add-building-and-generating-for-HIDL-headers-src-and.patch
Patch4:         0001-systemcore-Add-building-and-generating-for-HIDL-headers-src-and.patch
Patch5:         0002-hidl-Fix-bulding-on-gcc5.patch
Patch6:         0002-libhidl-Fix-bulding-on-gcc5.patch
Patch7:         0002-libhwbinder-Fix-bulding-on-gcc5.patch
Patch8:         0002-systemcore-Fix-bulding-on-gcc5.patch
Patch9:         0003-hidl-MakeParentHierarchy-avoid-race-condition-between-sta.patch
Patch10:        0003-libhwbinder-Make-sure-we-define-__ANDROID__-in-hwbinder.patch
Patch11:        0003-systemcore-base-define-__BIONIC__-for-properties-code.patch
Patch12:        0004-systemcore-liblog-fix-compilation-with-GCC-5.patch

%description
This builds and generates HIDL headers and binaries. This is work in progress, expect bugs and failures!

%package devel
Summary: linux-hidl devel package
Requires:  linux-hidl = %{version}-%{release}

%description devel
%{summary}

%prep
%autosetup -n %{name}-%{version}/upstream
patch0 -p1
#patch1 -p1
#patch2 -p1
#patch3 -p1
#patch4 -p1
#patch5 -p1
#patch6 -p1
#patch7 -p1
#patch8 -p1
#patch9 -p1
#patch10 -p1
#patch11 -p1
#patch12 -p1

%build
%cmake
%make_build

%install
%make install

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%{_libdir}/gstreamer-%{majorminor}/*.so
%{_libdir}/*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/gstreamer-%{majorminor}/gst/
%{_libdir}/*.so
%{_libdir}/pkgconfig/gstreamer-droid-1.0.pc
