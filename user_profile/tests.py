# Create your tests here.
from django.test import TestCase, Client, RequestFactory

from user_profile.views import show_main, get_profile_json, get_profile, edit_profile_ajax, edit_review_ajax, delete_review, get_reviews, get_review_json, get_forum, get_reply, get_reply_json 
from django.urls import reverse, resolve
from user_profile.models import Profile
from book.models import Book
from forum.models import Forum, Reply
from reviews.models import Review
from django.contrib.auth.models import User

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('/profile/')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('/profile/')
        self.assertTemplateUsed(response, 'profile.html')

# class UserProfileTestCase(TestCase):
#     # --------------------- URL ---------------------------- #
#     def test_show_main_url(self):
#         url = reverse("user_profile:show_main")
#         self.assertEquals(resolve(url).func, show_main)

#     def test_get_profile_json_url(self):
#         url = reverse("user_profile:get_profile_json")
#         self.assertEquals(resolve(url).func, get_profile_json)

#     def test_get_profile_url(self):
#         url = reverse("user_profile:get_profile")
#         self.assertEquals(resolve(url).func, get_profile)





    # def setUp(self):
    #     self.client = Client()

    # def test_get_profile_json(self):
    #     response = self.client.get(reverse('user_profile:get_profile_json'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response['content-type'], 'application/json')

    # def test_get_profile(self):
    #     response = self.client.get(reverse('user_profile:get_profile'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response['content-type'], 'application/json')

    # def test_edit_profile_ajax(self):
    #     response = self.client.post(reverse('user_profile:edit_profile_ajax'), {'name': 'New Name', 'description': 'New Description'})
    #     self.assertEqual(response.status_code, 201)

    # def test_get_reviews(self):
    #     response = self.client.get(reverse('user_profile:get_reviews'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response['content-type'], 'application/json')

    # def test_delete_review(self):
    #     response = self.client.post(reverse('user_profile:delete_review', args=[1]))
    #     self.assertEqual(response.status_code, 200)

    # def test_get_review_json(self):
    #     response = self.client.get(reverse('user_profile:get_review_json', args=[1]))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response['content-type'], 'application/json')

    # def test_get_forum(self):
    #     response = self.client.get(reverse('user_profile:get_forum'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response['content-type'], 'application/json')

    # def test_get_reply(self):
    #     response = self.client.get(reverse('user_profile:get_reply'))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response['content-type'], 'application/json')

    # def test_get_reply_json(self):
    #     response = self.client.get(reverse('user_profile:get_reply_json', args=[1]))
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(response['content-type'], 'application/json')

    # def test_edit_review_ajax(self):
    #     data = {
    #         'star': 5,
    #         'description': 'Updated description',
    #     }
    #     response = self.client.post(reverse('user_profile:edit_review_ajax', args=[1]), data)
    #     self.assertEqual(response.status_code, 201)
