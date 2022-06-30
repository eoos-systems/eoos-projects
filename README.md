# EOOS Automotive Projects
---

**EOOS copyrights reserved in [Rospatent Federal Service for Intellectual Property]( https://www1.fips.ru/registers-doc-view/fips_servlet?DB=EVM&DocNumber=2017664105&TypeFile=html), Russian Federation**

This repository is a **main entry point** to all the EOOS Automotive Projects, which contains aligned 
projects to build user applications based on an exact EOOS API version for all the platforms.

EOOS Automotive is **a set of C++ libraries** for different hardware platforms and operating systems 
**to develop cross-platform applications** in automotive sphere.

The libraries are developed in **C++98** programming language (ISO/IEC 14882:1998) and support features 
of **C++11** programming language (ISO/IEC 14882:2011), and this allows to consider wide criteria when 
selecting a suitable programming language on initiation step of product development.

EOOS Automotive is developed within **ISO C++ standards**, complied with **MISRA C++:2008** and 
**AUTOSAR C++14 Coding Guidelines**, and relies on **ISO 26262** that means applications based 
on EOOS **can be used in critical and safety-related systems**.

For present, EOOS Automotive is available for **POSIX** and **WIN32 API** operation systems and 
has **Sample Application** for fast start developing new user applications.

---

## Getting Started

Before you start to develop your first application based on EOOS, we want you to know that EOOS is 
not one project which can be built for a platform based on some compiler global defines – no. 
EOOS has deep elaborated projects each for exactly one platform. These projects here are included 
as git submodules and have well defined modularity, which means each EOOS project contains software 
modules included as git submodules as well. 

Thus, before you start to develop your first application, you must build an appropriate EOOS project 
for a platform you would like to develop your product.



#### Obtain Git Repository

This chapter describes common approach for a system terminal, which can be different depending on 
operating system you use. And to generalize the approach here, we will give examples for *Bash* 
that can be executed on Windows and on Linux.

###### 1. Create an empty directory somewhere on your disk

For instance we will create REPOSITORY.

```
$ mkdir REPOSITORY
$ cd REPOSITORY
```

###### 2. Clone this repository

For instance we will clone it to EOOS directory by SSH.

```
REPOSITORY$ git clone --branch master git@gitflic.ru:baigudin-software/eoos-projects.git EOOS
```

###### 3. Initialize and update all submodules of the repository recursively

```
REPOSITORY$ cd EOOS
REPOSITORY/EOOS$ git submodule update --init --recursive
```



#### Repository Structure

This repository consists of projects located in the directory of the same name. 
These projects included to the repository as git submodules. The structure and short 
description are given below.

```
REPOSITORY/EOOS/
└── projects/
    ├── eoos-if-posix
    ├── eoos-if-win32
    └── eoos-sample-applications
```

- **[eoos-if-posix(https://gitflic.ru/project/baigudin-software/eoos-project-if-posix)** - is EOOS project for POSIX based operating systems.
- **[eoos-if-win32](https://gitflic.ru/project/baigudin-software/eoos-project-if-win32)** - is EOOS project for WIN32 API based operating systems.
- **[eoos-sample-applications](https://gitflic.ru/project/baigudin-software/eoos-project-sample-applications)** - is cross-platform sample applications.
