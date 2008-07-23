%define module  VCG
%define name    perl-%{module}
%define version 0.5
%define release %mkrel 11

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        %{module} module for perl
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/VCG/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:  perl-devel
%endif
BuildRequires:  perl(IPC::Run)
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
This module provides an interface to to the vcg graphing tool. It
supports a limited selection of options and file formats. The vcg
graphing tool homepage is currently
http://rw4.cs.uni-sb.de/users/sander/html/gsvcg1.html but is being
actively developed elsewhere. 


This module is based on Leon Brocard's GraphViz module, it tries to
provide a similar interface to offer some sense of consistency. 


VCG is now in active development and although Graph::Writer::VCG already
exists, this module provides a similar interface to graphviz and will be
more closely tied into vcg as it becomes more actively developed - see
James Micheal DuPont's announcement at
http://mail.gnome.org/archives/dia-list/2003-February/msg00029.html.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes INSTALL README
%{perl_vendorlib}/VCG.pm
%{_mandir}/*/*

