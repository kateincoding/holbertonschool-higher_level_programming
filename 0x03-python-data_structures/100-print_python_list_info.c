#include <stdio.h>
#include <Python.h>

/**
 * print_python_list_info - prints info about Python lists
 * @p: Python Object
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
void print_python_list_info(PyObject *p)
{
	long int list_size, alloc_list, i;
	PyObject *item;

	list_size = PyList_Size(p);
	alloc_list = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", alloc_list);
	for (i = 0; i < list_size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
