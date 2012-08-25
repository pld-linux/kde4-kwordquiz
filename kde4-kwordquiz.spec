%define		_state		stable
%define		orgname		kwordquiz

Summary:	K Desktop Environment - A flashcard and vocabulary learning program
Summary(pl_PL.UTF8):	K Desktop Environment - Program do ćwiczenia słownictwa za pomocą pokazywania kart
Name:		kde4-kwordquiz
Version:	4.9.0
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{orgname}-%{version}.tar.xz
# Source0-md5:	6e68579cd02c0b4890c6d4c92a6c1856
URL:		http://www.kde.org/
BuildRequires:	automoc4
BuildRequires:	kde4-kdelibs-devel >= %{version}
BuildRequires:	qt4-build
Obsoletes:	kde4-kdeedu-kwordquiz < 4.6.99
Obsoletes:	kwordquiz <= 4.8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KWordQuiz is the KDE version of the flashcard and vocabulary learning
program WordQuiz. It is a tool for learning the vocabulary of a new
language. Now you can start to use its power for easy vocabulary
learning.

You build vocabularies in a two-column table (or load them from
kvoctrain's .kvtml). In one column you enter the words or expressions
in one language, and in the other column the corresponding word or
expression in another language. You can also use it to practice other
things, as long as there is a pair-wise relation. Examples are medical
or legal terminology. If you look at the screenshots there is an
example with the different US states and their capitals.

KWordQuiz also features Flashcard, Multiple Choice and Question &
Answer functions. Question & Answer also has a special
Fill-in-the-blank mode.

%description -l pl.UTF-8
KWordQuiz to wersja KDE programu WordQuiz służącego do nauki
słownictwa za pomocą pokazywania kart. Jest to narzędzie do nauki
słownictwa nowego języka. Można zacząć używać jego potencjału do
łatwego uczenia się słownictwa.

Słowniki buduje się w dwukolumnowej tabeli (lub wczytuje z plików
.kvtml z kvoctraina). W jednej kolumnie wpisuje się słowa lub
wyrażenia w jednym języku, a w drugiej kolumnie ich odpowiedniki w
innym języku. Można także używać programu do ćwiczenia innych rzeczy,
jeśli tylko mają parowalną relację - na przykład terminologii
medycznej czy prawniczej. Na screenshotach widać przykład z różnymi
stanami USA i ich stolicami.

KWordQuiz zawiera także funkcje Flashcard (pokazywania kart), testu
wielokrotnego wyboru oraz pytań i odpowiedzi. Pytania i odpowiedzi
mają także specjalny tryb wypełniania luk.

%prep
%setup -q -n %{orgname}-%{version}

%build
install -d build
cd build
%cmake \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build/ install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang %{orgname} --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{orgname}.lang
%defattr(644,root,root,755)
%{_datadir}/apps/kwordquiz
%attr(755,root,root) %{_bindir}/kwordquiz
%{_desktopdir}/kde4/kwordquiz.desktop
%{_datadir}/config.kcfg/kwordquiz.kcfg
%{_datadir}/config/kwordquiz.knsrc
%{_iconsdir}/hicolor/*x*/apps/kwordquiz.png
%{_iconsdir}/hicolor/*x*/mimetypes/application-x-kwordquiz.png
