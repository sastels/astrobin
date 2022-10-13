from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from astrobin.enums.moderator_decision import ModeratorDecision
from astrobin.tests.generators import Generators


class ImageNavigationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user('test', 'test@test.com', 'password')

    def test_next_prev(self):
        prev = Generators.image(user=self.user, moderator_decision=ModeratorDecision.APPROVED)
        prev.save()

        current = Generators.image(user=self.user, moderator_decision=ModeratorDecision.APPROVED)
        current.save()

        next = Generators.image(user=self.user, moderator_decision=ModeratorDecision.APPROVED)
        next.save()

        response = self.client.get(reverse('image_detail', args=(prev.get_id(),)))
        self.assertContains(response, "image-prev-none")
        self.assertContains(response, "image-next-%s" % current.get_id())

        response = self.client.get(reverse('image_detail', args=(current.get_id(),)))
        self.assertContains(response, "image-prev-%s" % prev.get_id())
        self.assertContains(response, "image-next-%s" % next.get_id())

        response = self.client.get(reverse('image_detail', args=(next.get_id(),)))
        self.assertContains(response, "image-prev-%s" % current.get_id())
        self.assertContains(response, "image-next-none")

    def test_next_prev_accounts_for_wip(self):
        prev = Generators.image(user=self.user, is_wip=True, moderator_decision=ModeratorDecision.APPROVED)
        prev.save()

        current = Generators.image(user=self.user, moderator_decision=ModeratorDecision.APPROVED)
        current.save()

        response = self.client.get(reverse('image_detail', args=(current.get_id(),)))
        self.assertContains(response, "image-prev-none")

    def test_next_prev_accounts_for_unmoderated(self):
        prev = Generators.image(user=self.user, is_wip=True, moderator_decision=ModeratorDecision.UNDECIDED)
        prev.save()

        current = Generators.image(user=self.user, moderator_decision=ModeratorDecision.APPROVED)
        current.save()

        response = self.client.get(reverse('image_detail', args=(current.get_id(),)))
        self.assertContains(response, "image-prev-none")
