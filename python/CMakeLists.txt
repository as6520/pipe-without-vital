kwiver_create_python_init(example)
kwiver_add_python_module( ${CMAKE_CURRENT_SOURCE_DIR}/sender.py
                          example
                          sender )
kwiver_add_python_module( ${CMAKE_CURRENT_SOURCE_DIR}/receiver.py
                          example
                          receiver)
kwiver_add_python_module( ${CMAKE_CURRENT_SOURCE_DIR}/type.py
                          example
                          type )
