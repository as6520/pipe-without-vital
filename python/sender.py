"""
Simple sender process
"""
from __future__ import absolute_import, print_function

import numpy as np
from example.type import BBoxWithMultipleDescriptors

# kwiver/sprokit imports
from sprokit.pipeline import process
from kwiver.kwiver_process import KwiverProcess
from sprokit.pipeline import datum

class SenderProcess(KwiverProcess):
    def __init__(self, conf):
        KwiverProcess.__init__(self, conf)
        # set up required flags
        required = process.PortFlags()
        required.add(self.flag_required)
        # Add the type trait
        self.add_type_trait( "BBoxWithMultipleDescriptors",
                             "BBoxWithMultipleDescriptors",
                             datum.Datum.get_datum,
                             datum.new )
        # Create a new port trait
        self.add_port_trait( "BBoxWithMultipleDescriptors",
                             "BBoxWithMultipleDescriptors",
                             "Custom python data type" )
        # Declare the port using the trait
        self.declare_output_port_using_trait("BBoxWithMultipleDescriptors", required)
        self.num_packets = 3

    def _configure(self):
        self.packet_count = 0

    def _step(self):
        if self.packet_count < self.num_packets:
            # Create the custom type for a certain iterations
            bbox = ((0,0), (0,2), (2,0), (2,2))
            descriptors = [np.zeros([10])]
            bbox_with_descriptor = BBoxWithMultipleDescriptors(bbox, descriptors)
            # Send the custom type to a port
            self.push_to_port_using_trait("BBoxWithMultipleDescriptors",
                                           bbox_with_descriptor)
            self.packet_count += 1
            print("Sent: {0}/{1}".format(self.packet_count, self.num_packets))
        else:
            # Send a complete datum and finish the process
            dat = self.push_datum_to_port_using_trait("BBoxWithMultipleDescriptors",
                                                        datum.complete())
            self.mark_process_as_complete()
            print("Finished sending")

def __sprokit_register__():
    from sprokit.pipeline import process_factory
    module_name = 'python:sender'
    if process_factory.is_process_module_loaded(module_name):
        return
    process_factory.add_process('SenderProcess', 'Process to send BBoxWithMultipleDescriptors',
                                SenderProcess)
    process_factory.mark_process_module_as_loaded(module_name)
