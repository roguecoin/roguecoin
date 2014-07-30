#include <Python.h>

#include <string.h>
//#include "neoscrypt.h"

typedef unsigned char uchar;

static PyObject *neoscrypt_getpowhash(PyObject *self, PyObject *args)
{
    unsigned char *output;
    PyObject *value;
    PyStringObject *input;
    
    if (!PyArg_ParseTuple(args, "S", &input)) 
        return NULL;
    Py_INCREF(input);
    output = PyMem_Malloc(32);

    neoscrypt((uchar *)PyString_AsString((PyObject*) input), output,0);
  
    Py_DECREF(input);
    value = Py_BuildValue("s#", output, 32);
    PyMem_Free(output);
    return value;
}

static PyMethodDef NeoScryptMethods[] = {
    { "getPoWHash", neoscrypt_getpowhash, METH_VARARGS, "Returns the proof of work hash using scrypt or neoscrypt" },
    { NULL, NULL, 0, NULL }
};

PyMODINIT_FUNC initneoscrypt(void) {
    (void) Py_InitModule("neoscrypt", NeoScryptMethods);
}
