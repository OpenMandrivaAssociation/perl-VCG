%define module  VCG

Name:		perl-%{module}
Version:	0.5
Release:	15
Summary:	%{module} module for perl
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/VCG/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRequires:	perl(IPC::Run)
BuildArch:	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes INSTALL README
%{perl_vendorlib}/VCG.pm
%{_mandir}/*/*



%changelog
* Fri Sep 04 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.5-12mdv2010.0
+ Revision: 430613
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.5-11mdv2009.0
+ Revision: 242145
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Sat Sep 15 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.5-9mdv2008.0
+ Revision: 87075
- rebuild


* Tue Aug 29 2006 Guillaume Rousse <guillomovitch@mandriva.org> 0.5-8mdv2007.0
- Rebuild

* Tue Dec 20 2005 Nicolas Lécureuil <neoclust@mandriva.org> 0.5-7mdk
- Fix BuildRequires

* Tue Dec 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.5-6mdk
- spec cleanup
- better URL
- drop explicit require

* Mon Dec 20 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.5-5mdk
- fix buildrequires in a backward compatible way
- %%makeinstall_std macro

* Fri Jul 23 2004 Guillaume Rousse <guillomovitch@mandrake.org> 0.5-4mdk 
- rpmbuildupdate aware

* Wed Jan 21 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.5-3mdk
- fix upload

