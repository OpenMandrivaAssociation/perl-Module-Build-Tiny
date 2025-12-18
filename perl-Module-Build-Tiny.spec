%define modname Module-Build-Tiny

Summary:	Build and install Perl modules
Name:		perl-%{modname}
Version:	0.052
Release:	1
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/pod/Module::Build
Source0:	http://www.cpan.org/modules/by-module/Module/%{modname}-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	perl(ExtUtils::Config)
BuildRequires:	perl(ExtUtils::Helpers)
BuildRequires:	perl(ExtUtils::InstallPaths)
BuildRequires:	perl(CPAN::Meta)
BuildRequires:	perl(ExtUtils::CBuilder)
BuildRequires:	perl-devel
# for %%check
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod)
Suggests:	perl-ExtUtils-CBuilder

%description
Module::Build is a system for building, testing, and installing Perl modules.
It is meant to be a replacement for ExtUtils::MakeMaker. Developers may alter
the behavior of the module through subclassing in a much more straightforward
way than with MakeMaker. It also does not require a make on your system - most
of the Module::Build code is pure-perl and written in a very cross-platform
way. In fact, you don't even need a shell, so even platforms like MacOS
(traditional) can use it fairly easily. Its only prerequisites are modules that
are included with perl 5.6.0, and it works fine on perl 5.005 if you can
install a few additional modules.

%prep
%autosetup -p1 -n %{modname}-%{version} 
perl Build.PL --installdirs=vendor

%build
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist 0

%check
AUTHOR_TESTING=1 RELEASE_TESTING=1 ./Build test

%files 
%doc Changes README
%{perl_vendorlib}/Module
%{_mandir}/*/*
