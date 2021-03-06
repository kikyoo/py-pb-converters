# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: extend.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import addressbook_pb2 as addressbook__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='extend.proto',
  package='tutorial',
  
  serialized_pb=_b('\n\x0c\x65xtend.proto\x12\x08tutorial\x1a\x11\x61\x64\x64ressbook.proto\"\x18\n\x08Hometown\x12\x0c\n\x04\x63ity\x18\x01 \x02(\t\"$\n\x06School\x12\x0c\n\x04name\x18\x01 \x02(\t\x12\x0c\n\x04\x63ity\x18\x02 \x01(\t:\x1d\n\x03\x61ge\x12\x10.tutorial.Person\x18\x64 \x01(\x05:/\n\x03sch\x12\x10.tutorial.Person\x18\x65 \x03(\x0b\x32\x10.tutorial.School:#\n\tused_name\x12\x10.tutorial.Person\x18\x66 \x03(\t:0\n\x02ht\x12\x10.tutorial.Person\x18g \x01(\x0b\x32\x12.tutorial.Hometown')
  ,
  dependencies=[addressbook__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)


AGE_FIELD_NUMBER = 100
age = _descriptor.FieldDescriptor(
  name='age', full_name='tutorial.age', index=0,
  number=100, type=5, cpp_type=1, label=1,
  has_default_value=False, default_value=0,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
SCH_FIELD_NUMBER = 101
sch = _descriptor.FieldDescriptor(
  name='sch', full_name='tutorial.sch', index=1,
  number=101, type=11, cpp_type=10, label=3,
  has_default_value=False, default_value=[],
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
USED_NAME_FIELD_NUMBER = 102
used_name = _descriptor.FieldDescriptor(
  name='used_name', full_name='tutorial.used_name', index=2,
  number=102, type=9, cpp_type=9, label=3,
  has_default_value=False, default_value=[],
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)
HT_FIELD_NUMBER = 103
ht = _descriptor.FieldDescriptor(
  name='ht', full_name='tutorial.ht', index=3,
  number=103, type=11, cpp_type=10, label=1,
  has_default_value=False, default_value=None,
  message_type=None, enum_type=None, containing_type=None,
  is_extension=True, extension_scope=None,
  options=None)


_HOMETOWN = _descriptor.Descriptor(
  name='Hometown',
  full_name='tutorial.Hometown',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='city', full_name='tutorial.Hometown.city', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=45,
  serialized_end=69,
)


_SCHOOL = _descriptor.Descriptor(
  name='School',
  full_name='tutorial.School',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='tutorial.School.name', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='city', full_name='tutorial.School.city', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
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
  
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=71,
  serialized_end=107,
)

DESCRIPTOR.message_types_by_name['Hometown'] = _HOMETOWN
DESCRIPTOR.message_types_by_name['School'] = _SCHOOL
DESCRIPTOR.extensions_by_name['age'] = age
DESCRIPTOR.extensions_by_name['sch'] = sch
DESCRIPTOR.extensions_by_name['used_name'] = used_name
DESCRIPTOR.extensions_by_name['ht'] = ht

Hometown = _reflection.GeneratedProtocolMessageType('Hometown', (_message.Message,), dict(
  DESCRIPTOR = _HOMETOWN,
  __module__ = 'extend_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.Hometown)
  ))
_sym_db.RegisterMessage(Hometown)

School = _reflection.GeneratedProtocolMessageType('School', (_message.Message,), dict(
  DESCRIPTOR = _SCHOOL,
  __module__ = 'extend_pb2'
  # @@protoc_insertion_point(class_scope:tutorial.School)
  ))
_sym_db.RegisterMessage(School)

addressbook__pb2.Person.RegisterExtension(age)
sch.message_type = _SCHOOL
addressbook__pb2.Person.RegisterExtension(sch)
addressbook__pb2.Person.RegisterExtension(used_name)
ht.message_type = _HOMETOWN
addressbook__pb2.Person.RegisterExtension(ht)

# @@protoc_insertion_point(module_scope)
