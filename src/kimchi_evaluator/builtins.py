import src.kimchi_object.object as obj
from src.kimchi_evaluator.const import NULL


def builtin_len(*args):
    if len(args) != 1:
        return obj.Error("wrong number of arguments. got={}, want=1".format(len(args)))
    arg = args[0]
    if isinstance(arg, obj.String):
        return obj.Integer(len(arg.value))
    elif isinstance(arg, obj.Array):
        return obj.Integer(len(arg.value))
    else:
        return obj.Error("argument to `len` not supported, got {}".format(arg.type()))


def builtin_first(*args):
    if len(args) != 1:
        return obj.Error("wrong number of arguments. got={}, want=1".format(len(args)))
    arg = args[0]
    if not isinstance(arg, obj.Array):
        return obj.Error("argument to `first` must be ARRAY, got {}".format(arg.type()))
    if len(arg.elements) > 0:
        return arg.elements[0]
    else:
        return NULL


def builtin_last(*args):
    if len(args) != 1:
        return obj.Error("wrong number of arguments. got={}, want=1".format(len(args)))
    arg = args[0]
    if not isinstance(arg, obj.Array):
        return obj.Error("argument to `last` must be ARRAY, got {}".format(arg.type()))
    if len(arg.elements) > 0:
        return arg.elements[-1]
    else:
        return NULL


def builtin_rest(*args):
    if len(args) != 1:
        return obj.Error("wrong number of arguments. got={}, want=1".format(len(args)))
    arg = args[0]
    if not isinstance(arg, obj.Array):
        return obj.Error("argument to `rest` must be ARRAY, got {}".format(arg.type()))
    if len(arg.elements) > 0:
        return obj.Array(arg.elements[1:])
    else:
        return NULL


def builtin_push(*args):
    if len(args) != 2:
        return obj.Error("wrong number of arguments. got={}, want=2".format(len(args)))
    arg = args[0]
    if not isinstance(arg, obj.Array):
        return obj.Error("argument to `push` must be ARRAY, got {}".format(arg.type()))
    new_element = args[1]
    new_elements = arg.elements + [new_element]
    return obj.A(new_elements)


builtins = {
    "len": obj.Builtin(builtin_len),
    "first": obj.Builtin(builtin_first),
    "last": obj.Builtin(builtin_last),
    "rest": obj.Builtin(builtin_rest),
    "push": obj.Builtin(builtin_push),
}
