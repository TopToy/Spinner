# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: spinnerTypes/utils.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='spinnerTypes/utils.proto',
  package='proto.types',
  syntax='proto3',
  serialized_pb=_b('\n\x18spinnerTypes/utils.proto\x12\x0bproto.types\"\x16\n\x07Integer\x12\x0b\n\x03num\x18\x01 \x01(\x05\"\x07\n\x05\x45mptyB\x14\n\x0bproto.typesB\x05utilsb\x06proto3')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_INTEGER = _descriptor.Descriptor(
  name='Integer',
  full_name='proto.types.Integer',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='num', full_name='proto.types.Integer.num', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=41,
  serialized_end=63,
)


_EMPTY = _descriptor.Descriptor(
  name='Empty',
  full_name='proto.types.Empty',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=65,
  serialized_end=72,
)

DESCRIPTOR.message_types_by_name['Integer'] = _INTEGER
DESCRIPTOR.message_types_by_name['Empty'] = _EMPTY

Integer = _reflection.GeneratedProtocolMessageType('Integer', (_message.Message,), dict(
  DESCRIPTOR = _INTEGER,
  __module__ = 'spinnerTypes.utils_pb2'
  # @@protoc_insertion_point(class_scope:proto.types.Integer)
  ))
_sym_db.RegisterMessage(Integer)

Empty = _reflection.GeneratedProtocolMessageType('Empty', (_message.Message,), dict(
  DESCRIPTOR = _EMPTY,
  __module__ = 'spinnerTypes.utils_pb2'
  # @@protoc_insertion_point(class_scope:proto.types.Empty)
  ))
_sym_db.RegisterMessage(Empty)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('\n\013proto.typesB\005utils'))
# @@protoc_insertion_point(module_scope)
