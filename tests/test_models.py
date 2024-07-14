from django.test import TestCase
from home.models import Handover,Notices,Comment
from django.contrib.auth.models import User

class HandoverModel(TestCase):
    def setUp(self):
        self.user1=User.objects.create(username="Dommy",password="123")
        self.user2=User.objects.create(username='Harry',password='456')
        self.notice=Notices.objects.create(Title='Thank you', Notice='I appreciate',Notice_by=self.user2)


    def test_handover_model(self):
        testing=Handover.objects.create(
           Shift='Day',
           Handover_From=self.user1,
           Handover_To=self.user2,
           title='General Pack',
           Tasks_In_Progress='Pack inspections',
           Important_Notes='Ensure everything is checked',
           Completed_task=True,
           completed_by=self.user1
        )

        self.assertEqual(testing.Shift,'Day'),
        self.assertEqual(testing.Handover_From,self.user1),
        self.assertEqual(testing.Handover_To,self.user2),
        self.assertEqual(testing.title,'General Pack'),
        self.assertEqual(testing.Important_Notes,'Ensure everything is checked')
        self.assertEqual(testing.Tasks_In_Progress,'Pack inspections'),
        self.assertTrue(testing.Completed_task),
        self.assertEqual(testing.completed_by,self.user1),
        self.assertIsNotNone(testing.Date),
        self.assertIsNotNone(testing.pk)

    def test_Notices_model(self):
        example=Notices.objects.create(
            Title='Welcome',
            Notice='Take your leave days',
            Notice_by=self.user1
        )

        self.assertTrue(example.Title,'Welcome'),
        self.assertTrue(example.Notice,'Take your leave days'),
        self.assertTrue(example.Notice_by,self.user1),
        self.assertIsNotNone(example.Date)

    def test_Comment_model(self):
        chat=Comment.objects.create(
            notice=self.notice,
            comment_by=self.user1,
            remarks='Noted'
        )

        self.assertEqual(chat.notice,self.notice),
        self.assertEqual(chat.comment_by,self.user1),
        self.assertEqual(chat.remarks,'Noted')
    




    
