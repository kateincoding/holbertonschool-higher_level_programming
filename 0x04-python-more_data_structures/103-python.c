#include <Python.h>

/**
 * print_python_bytes - prints info about Python bytes (hexa ascii)
 * @p: Python Object
 * Return: void
 */
void print_python_bytes(PyObject *p)
{
	int i = 0, bsize = 0;
	char *str;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	bsize = PyBytes_Size(p);
	printf("  size: %d\n", bsize);
	str = ((PyBytesObject *)p)->ob_sval;
	printf("  trying string: %s\n", str);

	if (bsize < 10)
		printf("  first %d bytes:", bsize + 1);
	else
		printf("  first 10 bytes:");

	for (i = 0; (i <= bsize) && (i < 10); i++)
	{
			printf(" %02hhx", str[i]);
	}
	printf("\n");
}

/**
 * print_python_list_info - prints info about Python lists
 * @p: Python Object
 * Return: void
 */
void print_python_list(PyObject *p)
{
	long int list_size, alloc_list, i;
	PyObject *list_item;

	list_size = PyList_Size(p);
	alloc_list = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", alloc_list);
	for (i = 0; i < list_size; i++)
	{
		list_item = (((PyListObject *)p)->ob_item[i]);
		printf("Element %ld: %s\n", i, (list_item->ob_type)->tp_name);
        if (PyBytes_Check(list_item))
            print_python_bytes(list_item);
	}
}
