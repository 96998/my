import unittest


# 单元测试l

def get_formatted_name(first, last):
    """Generate a neatly formatted name."""
    full_name = first + ' ' + last
    return full_name.title()


class NamesTestCase(unittest.TestCase):
    """测试get_foramtted_name函数"""

    def test_first_last_name(self):
        """能够正确地处理像Janis Joplin这样的姓名吗？ """
        formatted_name = get_formatted_name('jains', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')


unittest.main()
