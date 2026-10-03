'''
RadSSH plugin loading helpers.

The default plugin modules are stored in ``core_plugins`` and copied into this
package during installation. Keeping this shim in source checkouts lets modules
import ``radssh.plugins`` before that installation merge has happened.
'''

from ..core_plugins import StarCommand, discover_plugin, load_plugin

__all__ = ['StarCommand', 'discover_plugin', 'load_plugin']