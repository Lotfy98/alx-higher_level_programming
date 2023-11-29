#include <Python.h>

void print_python_string(PyObject *p)
{
 long int length;

 /* Check if p is a string */
 if (!PyUnicode_Check(p))
 {
		printf("[ERROR] Invalid String Object\n");
		return;
 }

 /* Get the length of the string */
 length = PyUnicode_GET_LENGTH(p);

 /* Print the string object info */
 printf("[.] string object info\n");
 if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
 else
		printf("  type: compact unicode object\n");
 printf("  length: %ld\n", length);
 printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
}
