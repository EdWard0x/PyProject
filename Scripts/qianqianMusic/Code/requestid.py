__all__ = ['requestid']

# Don't look below, you will not understand this Python code :) I don't.

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers([])
@Js
def PyJs_anonymous_0_(e, this, arguments, var=var):
    var = Scope({'e':e, 'this':this, 'arguments':arguments}, var)
    var.registers(['i', 'r', 'e', 't', 'o', 'n'])
    #for JS loop
    var.put('t', (var.get('e') if ((Js(0.0)<var.get('arguments').get('length')) and PyJsStrictNeq(PyJsComma(Js(0.0), Js(None)),var.get('e'))) else Js(10.0)))
    var.put('n', Js('ABCDEFGHJKMNPQRSTWXYZabcdefhijkmnprstwxyz2345678'))
    var.put('i', var.get('n').get('length'))
    var.put('r', Js(''))
    var.put('o', Js(0.0))
    while (var.get('o')<var.get('t')):
        try:
            var.put('r', var.get('n').callprop('charAt', var.get('Math').callprop('floor', (var.get('Math').callprop('random')*var.get('i')))), '+')
        finally:
                (var.put('o',Js(var.get('o').to_number())+Js(1))-Js(1))
    return var.get('r')
PyJs_anonymous_0_._set_name('anonymous')
var.put('randomStr', PyJs_anonymous_0_)


# Add lib to the module scope
requestid = var.to_python()