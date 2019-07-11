"""
Simple receiver process
"""
from __future__ import absolute_import, print_function
from example.type import BBoxWithMultipleDescriptors
import numpy as np

# kwiver/sprokit imports
from sprokit.pipeline import process
from kwiver.kwiver_process import KwiverProcess
from sprokit.pipeline import datum

class ReceiverProcess(KwiverProcess):
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
        self.declare_input_port_using_trait("BBoxWithMultipleDescriptors", required)

    def _configure(self):
        pass

    def _step(self):
        bbox_with_descriptor = self.grab_input_using_trait('BBoxWithMultipleDescriptors')
        print("Bounding box: {0}, descriptor: {1}".format(bbox_with_descriptor.bbox,
                                                          bbox_with_descriptor.descriptors))

def __sprokit_register__():
    from sprokit.pipeline import process_factory
    module_name = 'python:receiver'
    if process_factory.is_process_module_loaded(module_name):
        return
    process_factory.add_process('ReceiverProcess',
                                'Process to receive BBoxWithMultipleDescriptors',
                                ReceiverProcess)
    process_factory.mark_process_module_as_loaded(module_name)
