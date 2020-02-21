import unittest
from app.models import Comment, User
from app import db


class TestComment(unittest.TestCase):

    def setUp(self):
        self.user = User(username='allan', password='allan',
                         email='wendy@gmail.com')
        self.new_comment = Comment(
            pitch_id=12345, pitch_comment='Wagwan', user=self.user_allan)

    def tearDown(self):
        Comment.query.delete()
        User.query.delete()

    def test_check_instance_variables(self):
        self.assertEqual(self.new_comment.pitch_id, 12345)
        self.assertEqual(self.new_comment.pitch_comment,
                         'Wagwan')
        self.assertEqual(self.new_comment.user, self.user_allan)

    def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all()) > 0)

    def test_get_comments_by_pitch_id(self):
        self.new_comment.save_comment()
        gotten_comments = Comment.get_comments_by_pitch_id(12345)
        self.assertTrue(len(gotten_comments) == 1)