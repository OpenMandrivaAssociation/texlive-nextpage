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
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3

%description
Provides \clearpage and \newpage variants that guarantee to end
up on even/odd numbered pages; these 4 commands all have an
optional argument whose content will be placed on any "empty"
page generated.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
