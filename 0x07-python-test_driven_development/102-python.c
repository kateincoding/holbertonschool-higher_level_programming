#include <Python.h>

/**
 * print_python_string - function that prints Python strings
 * @p: Python string
 * Return: void
 */
void print_python_string(PyObject *p)
{
	ssize_t len;

	printf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "str") != 0)
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	len = PyUnicode_GET_LENGTH(p);
	printf("  length: %ld\n", len);
	printf("  value: %s\n", PyUnicode_AsUTF8AndSize(p, &len));
}
