# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/path.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/path.proto',
  package='WacomInkFormat',
  syntax='proto2',
  serialized_options=_b('H\003'),
  serialized_pb=_b('\n\x11protos/path.proto\x12\x0eWacomInkFormat\"\x9e\x01\n\x04Path\x12\x19\n\x0estartParameter\x18\x01 \x01(\x02:\x01\x30\x12\x17\n\x0c\x65ndParameter\x18\x02 \x01(\x02:\x01\x31\x12\x1b\n\x10\x64\x65\x63imalPrecision\x18\x03 \x01(\r:\x01\x32\x12\x12\n\x06points\x18\x04 \x03(\x11\x42\x02\x10\x01\x12\x18\n\x0cstrokeWidths\x18\x05 \x03(\x11\x42\x02\x10\x01\x12\x17\n\x0bstrokeColor\x18\x06 \x03(\x11\x42\x02\x10\x01\x42\x02H\x03')
)




_PATH = _descriptor.Descriptor(
  name='Path',
  full_name='WacomInkFormat.Path',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='startParameter', full_name='WacomInkFormat.Path.startParameter', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endParameter', full_name='WacomInkFormat.Path.endParameter', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=float(1),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='decimalPrecision', full_name='WacomInkFormat.Path.decimalPrecision', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=True, default_value=2,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='points', full_name='WacomInkFormat.Path.points', index=3,
      number=4, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strokeWidths', full_name='WacomInkFormat.Path.strokeWidths', index=4,
      number=5, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='strokeColor', full_name='WacomInkFormat.Path.strokeColor', index=5,
      number=6, type=17, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\020\001'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=38,
  serialized_end=196,
)

DESCRIPTOR.message_types_by_name['Path'] = _PATH
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Path = _reflection.GeneratedProtocolMessageType('Path', (_message.Message,), dict(
  DESCRIPTOR = _PATH,
  __module__ = 'protos.path_pb2'
  # @@protoc_insertion_point(class_scope:WacomInkFormat.Path)
  ))
_sym_db.RegisterMessage(Path)


DESCRIPTOR._options = None
_PATH.fields_by_name['points']._options = None
_PATH.fields_by_name['strokeWidths']._options = None
_PATH.fields_by_name['strokeColor']._options = None
# @@protoc_insertion_point(module_scope)
