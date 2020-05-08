import unittest
from interpretator import Interpreter


class MyTestCase(unittest.TestCase):

    def test_bubbleSorting(self):
        with open("Tests/bubbleSorting") as f:
            text = f.read()
        f.close()
        interpreter = Interpreter()
        interpreter.interpreter(program=text)
        self.assertEqual(interpreter.sym_table[0]['my_vector'][1], [-3, 1, 3, 4, 5, 7])

    def test_fibonacci(self):
        with open("Tests/fibonacci") as f:
            text = f.read()
        f.close()
        interpreter = Interpreter()
        interpreter.interpreter(program=text)
        self.assertEqual(interpreter.sym_table[0]['res'].value, 46368)

    def test_vectorsTest(self):
        with open("Tests/vectorsTest") as f:
            text = f.read()
        f.close()
        interpreter = Interpreter()
        interpreter.interpreter(program=text)
        self.assertEqual(interpreter.sym_table[0]['b'].value, False)
        self.assertEqual(interpreter.sym_table[0]['a'].value, 2)
        self.assertEqual(interpreter.sym_table[0]['d_s'][1], [[['rer']]])
        self.assertEqual(interpreter.sym_table[0]['ones'][1], [2, 3, 4, 9])
        self.assertEqual(interpreter.sym_table[0]['v_s'][1], [[['heeeey']]])
        self.assertEqual(interpreter.sym_table[0]['v1'][1], [2])
        self.assertEqual(interpreter.sym_table[0]['triple_str'][1], [[[[['heeeey']]]]])

    def test_operatorsTest(self):
        with open("Tests/operatorsTest") as f:
            text = f.read()
        f.close()
        interpreter = Interpreter()
        interpreter.interpreter(program=text)
        self.assertEqual(interpreter.sym_table[0]['v3'][1], [[[[-1]]]])
        self.assertEqual(interpreter.sym_table[0]['v1'][1], [[[[3]]]])
        self.assertEqual(interpreter.sym_table[0]['vv1'][1], [2, 3])
        self.assertEqual(interpreter.sym_table[0]['op_int_g'].value, False)
        self.assertEqual(interpreter.sym_table[0]['op_int_l'].value, True)
        self.assertEqual(interpreter.sym_table[0]['op_int_eq'].value, False)
        self.assertEqual(interpreter.sym_table[0]['op_int_neq'].value, True)
        self.assertEqual(interpreter.sym_table[0]['op_str_g'].value, False)
        self.assertEqual(interpreter.sym_table[0]['op_str_l'].value, True)
        self.assertEqual(interpreter.sym_table[0]['op_str_eq'].value, False)
        self.assertEqual(interpreter.sym_table[0]['op_str_neq'].value, True)
        self.assertEqual(interpreter.sym_table[0]['op_bool_g'].value, False)
        self.assertEqual(interpreter.sym_table[0]['op_bool_l'].value, False)
        self.assertEqual(interpreter.sym_table[0]['op_bool_eq'].value, True)
        self.assertEqual(interpreter.sym_table[0]['op_bool_neq'].value, False)
        self.assertEqual(interpreter.sym_table[0]['op_v_g'].value, True)
        self.assertEqual(interpreter.sym_table[0]['op_v_l'].value, False)
        self.assertEqual(interpreter.sym_table[0]['op_v_eq'].value, False)
        self.assertEqual(interpreter.sym_table[0]['op_v_neq'].value, True)

    def test_functions(self):
        with open("Tests/functions") as f:
            text = f.read()
        f.close()
        interpreter = Interpreter()
        interpreter.interpreter(program=text)
        self.assertEqual(interpreter.sym_table[0]['res1'].value, 2)
        self.assertEqual(interpreter.sym_table[0]['res2'].value, 15)
        self.assertEqual(interpreter.sym_table[0]['res3'].value, True)
        self.assertEqual(interpreter.sym_table[0]['res4'].value, "StayAtHome")
        self.assertEqual(interpreter.sym_table[0]['res5'].value, 1234)

    def test_priority(self):
        with open("Tests/priority") as f:
            text = f.read()
        f.close()
        interpreter = Interpreter()
        interpreter.interpreter(program=text)
        self.assertEqual(interpreter.sym_table[0]['res1'].value, True)
        self.assertEqual(interpreter.sym_table[0]['res2'].value, False)


if __name__ == '__main__':
    unittest.main()
