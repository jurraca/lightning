lightning-stop -- Command to shutdown the Core Lightning node.
==============================================================

SYNOPSIS
--------

**stop**

DESCRIPTION
-----------

The **stop** is a RPC command to shut off the Core Lightning node.

EXAMPLE JSON REQUEST
------------
```json
{
  "id": 82,
  "method": "stop",
  "params": {}
}
```

RETURN VALUE
------------

[comment]: # (GENERATE-FROM-SCHEMA-START)
On success, returns a single element (string) (always "Shutdown complete")
[comment]: # (GENERATE-FROM-SCHEMA-END)

Once it has returned, the daemon has cleaned up completely, and if
desired may be restarted immediately.


AUTHOR
------

Vincenzo Palazzo <<vincenzo.palazzo@protonmail.com>> wrote the initial version of this man page, but many others did the hard work of actually implementing this rpc command.


RESOURCES
---------

Main web site: <https://github.com/ElementsProject/lightning>
[comment]: # ( SHA256STAMP:a83ac745b36e0e3d00ba11f036cec93973773f47e1265eb5c70a3d3298e58e4b)
