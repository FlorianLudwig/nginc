nginc
=====

A small wrapper around nginx to start it as convenient as `SimpleHTTPServer <http://www.commandlinefu.com/commands/view/71/serve-current-directory-tree-at-httphostname8000>`_.

To serve the current working directory on port 8080:

  $ nginc

For more options see *nginc -h*


Why?
----

The python SimpleHTTPServer often comes quite handy.  But in some cases it is not enough.
For example if you need concurrent requests or range requests.
