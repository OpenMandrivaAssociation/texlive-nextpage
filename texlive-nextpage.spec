%global tl_name nextpage
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1a
Release:	%{tl_revision}.1
Summary:	Generalisations of the page advance commands
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/misc/nextpage.sty
License:	lppl1.1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nextpage.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Provides \clearpage and \newpage variants that guarantee to end up on
even/odd numbered pages; these 4 commands all have an optional argument
whose content will be placed on any "empty" page generated.

