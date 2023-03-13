# EOOS Automotive Projects
---

**EOOS copyrights reserved in [Rospatent Federal Service for Intellectual Property](https://www1.fips.ru/registers-doc-view/fips_servlet?DB=EVM&DocNumber=2017664105&TypeFile=html), Russian Federation**

This is **super repository** of all the EOOS Automotive projects and **main entry point** to build 
user applications based on an exact EOOS API version for all the platforms.

EOOS Automotive is **a set of C++ libraries** for different hardware platforms and operating systems 
**to develop cross-platform applications** in automotive sphere.

The libraries are developed in **C++98** programming language (ISO/IEC 14882:1998) and support features 
of **C++11** programming language (ISO/IEC 14882:2011), which allows to consider wide criteria when 
selecting a suitable programming language on initiation step of product development.

EOOS Automotive is developed within **ISO C++ standards**, complied with **MISRA C++:2008** and 
**AUTOSAR C++14 Coding Guidelines**, and relies on **ISO 26262** that means applications based 
on EOOS **can be used in critical and safety-related systems**.

For present, EOOS Automotive is available for **POSIX** and **WIN32 API** operation systems and 
has **Sample Applications** for fast start developing new user applications.


Quality of EOOS Automotive:

- MISRA C++ and AUTOSAR C++: **0** violations
- Unit Tests coverage: **96.5%** for POSIX and **94%** for WIN32

---


## Getting Started


### For Users

This chapter describes a way how to start developing your own application based on EOOS.

And before you start, we want you to know that EOOS is not one project which can be built 
for a platform based on some compiler global defines – no, EOOS has deep elaborated projects 
each for exactly one platform. These projects are included as git submodules and have well 
defined modularity that means each EOOS project contains software modules included as 
git submodules as well. 

Thus, before you start to develop your first application, you have to build an appropriate EOOS project 
for a operating system you would like to develop your product.



#### Obtain Git Repository

This chapter describes common approach for a system terminal, which can be different depending on 
operating system you use. And to generalize the approach here, we will give examples for *Bash* 
that can be executed on Windows and on Linux.

###### 1. Create an empty directory somewhere on your disk

For instance we will create REPOSITORY directory.

```
$ mkdir REPOSITORY
$ cd REPOSITORY
```

###### 2. Clone this repository

For instance we will clone it to EOOS directory by SSH.

```
REPOSITORY$ git clone --branch master git@gitflic.ru:baigudin-software/eoos-projects.git EOOS
```

###### 3. Initialize and update all submodules for the repository recursively

As we mention above, this super repository contains sub-repositories, and the sub-repositories also 
contain sub-repositories. Therefore `--recursive` key must be passed to the git command line.

```
REPOSITORY$ cd EOOS
REPOSITORY/EOOS$ git submodule update --init --recursive
```



#### Repository Structure

This super repository consists of projects located in the directory of the same name. 
These projects included to the super repository as git submodules. The structure and short 
description are given below.

```
REPOSITORY/EOOS/
└── projects/
    ├── eoos-if-posix
    ├── eoos-if-win32
    └── eoos-sample-applications
```

- **[eoos-if-posix](https://gitflic.ru/project/baigudin-software/eoos-project-if-posix)** - is EOOS project for POSIX based operating systems.
- **[eoos-if-win32](https://gitflic.ru/project/baigudin-software/eoos-project-if-win32)** - is EOOS project for WIN32 API based operating systems.
- **[eoos-sample-applications](https://gitflic.ru/project/baigudin-software/eoos-project-sample-applications)** - is cross-platform sample applications.



#### Build EOOS Project

Before developing your own application based on EOOS, you have to build an appropriate EOOS project 
for operating system you use and install EOOS on it. Detailed How-to Build Project chapters are 
written for each project in its root *README.md* files that you can find here:

- **[How-to Build EOOS Project for POSIX](https://gitflic.ru/project/baigudin-software/eoos-project-if-posix/blob?file=README.md)**
- **[How-to Build EOOS Project for WIN32](https://gitflic.ru/project/baigudin-software/eoos-project-if-win32/blob?file=README.md)**



#### Build EOOS Sample Application

To get a start point for developing your own application based on EOOS, you can consider 
Sample Applications, and *Hello World* especially. Thus, the Sample Applications repository 
can be modified for your needs. Detailed How-to Build Sample Applications chapter is written 
in root *README.md* files that you can find here:

- **[How-to Build Sample Applications](https://gitflic.ru/project/baigudin-software/eoos-project-sample-applications/blob?file=README.md)**




### For Developers

This chapter describes a few hits for developers who would like to be involved in EOOS developing process.

EOOS developing process is based on the `develop` branch of this repository which points to 
appropriate `master` branches of the sub-repositories. Also, main git service for developing is 
[GitFlic](https://gitflic.ru/project/baigudin-software/eoos-projects) with a mirror on 
[GitHub](https://github.com/baigudin-software/eoos-projects). To automate some routine work like 
repository initialization or integration, we have developed a few *Python* scripts that are 
located in `scripts/python` directory.

**NOTE:**  Please, follow the Prerequisites on *your OS* chapters to install all environment you need 
to successfully run the scripts and to develop EOOS by the link given in the previous chapter 
for appropriate EOOS project.



#### Prepare Git Repository

To simplify initialization of the git repositories for development purpose, we have created 
the `Begin.py` script that does all routine work for you.


###### 1. Create an empty directory somewhere on your disk

For instance we will create REPOSITORY directory.

```
$ mkdir REPOSITORY
$ cd REPOSITORY
```

###### 2. Clone this repository

We strongly recommend to do it by SSH.

```
REPOSITORY$ git clone git@gitflic.ru:baigudin-software/eoos-projects.git
```

###### 3. Go to scripts directory

This step is important as the script checks current directory set to its location.

```
REPOSITORY$ cd eoos-projects/scripts/python
```

###### 4. Initialize this repository

Execute the script to initialize all repositories for development.

```
REPOSITORY/eoos-projects/scripts/python$ python Begin.py --init
```

**All is done!** The repository and all the sub-repositories are ready to develop on them.

###### 5. See other options if it needs

To see other possible options please refer to the script help.

```
REPOSITORY/eoos-projects/scripts/python$ python Begin.py --help
```



#### Integrate Git Baranches

To be sure any system depending changes made correctly we have to build and to test them 
on all operating systems EOOS is being developed for. To simplify this process, we have created 
the `Integrate.py` script that does all for you on a host operating system it runs on.

**NOTE:** Run CMD in *Run as administrator* mode to be able to install EOOS on Windows and 
execute the commads below.

###### 1. Go to scripts directory

This step is important as the script checks current directory set to its location.

```
REPOSITORY$ cd eoos-projects/scripts/python
```

###### 2. Build and test EOOS

The `Integrate.py` script has several input arguments, but the most important execution 
commant is given below. This command builds and tests EOOS for all possible configurations, installs
EOOS on your host, and builds and runs EOOS sample applications checking their correct execution.

```
REPOSITORY/eoos-projects/scripts/python$ python Integrate.py --build ALL
```

**All is built and tested!** Zero return value by the script can be treeted by CI/CD server 
as EOOS is ready to be integrated for appropriate operating system.

###### 3. See other options if it needs

To see other possible options please refer to the script help.

```
REPOSITORY/eoos-projects/scripts/python$ python Integrate.py --help
```
