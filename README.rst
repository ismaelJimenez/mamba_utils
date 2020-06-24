================
Mamba-Utils
================

.. image:: https://api.travis-ci.org/mamba-framework/mamba-utils.svg?branch=master
   :target: https://travis-ci.org/github/mamba-framework/mamba-utils/builds
.. image:: https://img.shields.io/codecov/c/github/mamba-framework/mamba-utils/master.svg
   :target: https://codecov.io/github/mamba-framework/mamba-utils?branch=master
   :alt: Coverage report
.. image:: https://img.shields.io/pypi/v/Mamba-Utils.svg
        :target: https://pypi.python.org/pypi/Mamba-Utils
.. image:: https://img.shields.io/readthedocs/mamba-utils.svg
        :target: https://readthedocs.org/projects/mamba-utils/builds/
        :alt: Documentation Status
.. image:: https://img.shields.io/badge/license-%20MIT-blue.svg
   :target: ../master/LICENSE

Overview
============
Utilities for Mamba Framework development

Requirements
============

* Python 3.6+
* Works on Linux, Windows, macOS, BSD

Install
=======

The quick way::

    pip install mamba-utils
    
Scripts provided
================
* mamba_udp_sniffer
* mamba_udp_client
* mamba_udp_server_mock
* mamba_tcp_sniffer
* mamba_tcp_client
* mamba_tcp_server_mock

Use "-h" to get more information about the parameters of each script.

UDP Sniffer Example
===================
    mamba_udp_server_mock 10000
    
    mamba_udp_sniffer 9999 10000
    
    mamba_udp_client 9999 asdf
    
TCP Sniffer Example
===================
    mamba_tcp_server_mock 10000
    
    mamba_tcp_sniffer 9999 10000
    
    mamba_tcp_client 9999 asdf
