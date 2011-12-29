# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/misc/nextpage.sty
# catalog-date 2009-09-03 13:12:26 +0200
# catalog-license lppl
# catalog-version 1.1a
Name:		texlive-nextpage
Version:	1.1a
Release:	1
Summary:	Generalisations of the page advance commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/misc/nextpage.sty
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nextpage.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Provides \clearpage and \newpage variants that guarantee to end
up on even/odd numbered pages; these 4 commands all have an
optional argument whose content will be placed on any "empty"
page generated.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/nextpage/nextpage.sty

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex %{buildroot}%{_texmfdistdir}
