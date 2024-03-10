Tuple => tuple is a sequence of items of possibly different types.

```python
def tuple_to_list(tuple: Tuple) -> List:
    pass
```

```python
import unittest

class TestTupleToList(unittest.TestCase):

all python notes => https://github.com/tech-with-tim/python-notes



    def test_tuple_to_list(self):
        self.assertEqual(tuple_to_list((1, 2, 3)), [1, 2, 3])
        self.assertEqual(tuple_to_list(('a', 'b', 'c')), ['a', 'b', 'c'])
        self.assertEqual(tuple_to_list((True, False, True)), [True, False, True])

