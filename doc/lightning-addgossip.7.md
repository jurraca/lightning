lightning-addgossip -- Command for injecting a gossip message (low-level)
===============================================================

SYNOPSIS
--------

**addgossip** *message*

DESCRIPTION
-----------

The **addgossip** RPC command injects a hex-encoded gossip message into
the gossip daemon.  It may return an error if it is malformed, or may
update its internal state using the gossip message.

Note that currently some paths will still silently reject the gossip: it
is best effort.

This is particularly used by plugins which may receive channel_update
messages within error replies.

RETURN VALUE
------------

[comment]: # (GENERATE-FROM-SCHEMA-START)
On success, an empty object is returned.

[comment]: # (GENERATE-FROM-SCHEMA-END)

AUTHOR
------

Rusty Russell <<rusty@rustcorp.com.au>> is mainly responsible.

SEE ALSO
--------

lightning-pay(7)

RESOURCES
---------

Main web site: <https://github.com/ElementsProject/lightning>

[comment]: # ( SHA256STAMP:c801b02463804504c2387387a36a6739351330a2c496aaa10de2b1f49c36ed32)
