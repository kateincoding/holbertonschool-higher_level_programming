#include <stdio.h>
#include <Python.h>
#include <string.h>

/**
 * print_python_string - function that prints Python strings
 * @p: Python string
 */
void print_python_string(PyObject *p)
{
	ssize_t length;
	wchar_t *str;

	printf("[.] string object info");

	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	length = PyUnicode_GET_LENGTH(p);
	printf("  length: %ld\n", length);

	str = PyUnicode_AsUTF8AndSize(p, &length);
	printf("  value: %ls\n", str);
}
