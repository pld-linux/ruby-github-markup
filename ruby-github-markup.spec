
%define gitrev f65c5fd
%define gitauthor github
%define gitname markup

Summary:	Ruby interface to Git
Name:		ruby-github-markup
Version:	0.5.0
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	http://download.github.com/%{gitauthor}-%{gitname}-v%{version}-1-g%{gitrev}.tar.gz
# Source0-md5:	5060ed327b71036df28ab899cf4863b4
#Patch0: %{name}-nogems.patch
URL:		http://github.com/github/markup
BuildRequires:	rpmbuild(macros) >= 1.277
BuildRequires:	ruby
BuildRequires:	ruby-modules
BuildRequires:	setup.rb >= 3.4.1
%{?ruby_mod_ver_requires_eq}
#BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Code for interfacing with many different markup engines

%prep
%setup -q -n %{gitauthor}-%{gitname}-%{gitrev}
#%patch0 -p1
cp %{_datadir}/setup.rb .
ruby setup.rb config \
	--installdirs=std
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT

ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{ruby_rubylibdir}/github
%attr(755,root,root) %{_bindir}/github-markup
%{ruby_rubylibdir}/github/markup.rb
%{ruby_rubylibdir}/github/markups.rb
%{ruby_rubylibdir}/github/markup
%{ruby_rubylibdir}/github/commands
