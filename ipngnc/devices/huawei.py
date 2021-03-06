"""
Handler for Huawei device specific information.

Note that for proper import, the classname has to be:

    "<Devicename>DeviceHandler"

...where <Devicename> is something like "Default", "Huawei", etc.

All device-specific handlers derive from the DefaultDeviceHandler, which implements the
generic information needed for interaction with a Netconf server.

"""

from ipngnc.xml_ import BASE_NS_1_0

from ipngnc import DefaultDeviceHandler

class HuaweiDeviceHandler(DefaultDeviceHandler):
    """
    Huawei handler for device specific information.

    In the device_params dictionary, which is passed to __init__, you can specify
    the parameter "ssh_subsystem_name". That allows you to configure the preferred
    SSH subsystem name that should be tried on your Huawei switch. If connecting with
    that name fails, or you didn't specify that name, the other known subsystem names
    will be tried. However, if you specify it then this name will be tried first.

    """
    _EXEMPT_ERRORS = []

    def __init__(self, device_params):
        super(HuaweiDeviceHandler, self).__init__(device_params)

    def get_capabilities(self):
        # Just need to replace a single value in the default capabilities
        c = super(HuaweiDeviceHandler, self).get_capabilities()
        return c

    def get_xml_base_namespace_dict(self):
        return { "xmlns":BASE_NS_1_0 }

    def get_xml_extra_prefix_kwargs(self):
        d = {
                # "xmlns":"http://www.huawei.com/netconf/vrp"
            }
        d.update(self.get_xml_base_namespace_dict())
        return d


