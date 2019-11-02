Name:           cppkafka
Version:        %{VERSION}
Release:        %{RELEASE}%{?dist}
Summary:        Modern C++ Apache Kafka client library (wrapper for librdkafka)
Group:          System Environment/Libraries
License:		BSD
URL:            https://github.com/mfontanini/cppkafka
Source:         %{name}-%{version}.tar.gz      
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  cmake
BuildRequires:  librdkafka-devel

%description
Modern C++ Apache Kafka client library (wrapper for librdkafka)

%package devel
Summary:	%{name} development package
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires: 	librdkafka-devel 

%description devel
Development files for %{name}.

%prep
%setup

%build
%cmake
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT/usr/lib $RPM_BUILD_ROOT/usr/lib64

%clean
rm -rf $RPM_BUILD_ROOT

%post
ldconfig

%postun
ldconfig

%files
%defattr(-,root,root,-)
%doc LICENSE README.md 
%{_libdir}/lib%{name}.so.*


%files devel
%defattr(-,root,root,-)
%{_libdir}/*.so
%{_includedir}/%{name}

%changelog
