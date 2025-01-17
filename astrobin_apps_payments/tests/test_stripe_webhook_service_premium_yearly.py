from datetime import date

from django.contrib.auth.models import Group, User
from django.test import TestCase
from subscription.models import Subscription, Transaction

from astrobin.tests.generators import Generators
from astrobin_apps_payments.services.stripe_webhook_service import StripeWebhookService
from astrobin_apps_payments.tests.stripe_generators import StripeGenerators
from astrobin_apps_premium.services.premium_service import PremiumService, SubscriptionName


class StripeWebhookServicePremiumYearlyTest(TestCase):
    def setUp(self):
        self.subscription, created = Subscription.objects.get_or_create(
            name=SubscriptionName.PREMIUM_2020_AUTORENEW_YEARLY.value,
            currency="CHF",
            price=40,
            trial_period=0,
            trial_unit=None,
            recurrence_period=1,
            recurrence_unit='Y',
            group=Group.objects.get_or_create(name='astrobin_premium_2020')[0],
            category='premium_autorenew'
        )

    def test_first_order(self):
        user = Generators.user(email="astrobin@astrobin.com")
        e = StripeGenerators.event

        StripeWebhookService.process_event(e('premium_yearly_first_order/charge.succeeded'))
        StripeWebhookService.process_event(e('premium_yearly_first_order/payment_method.attached'))
        StripeWebhookService.process_event(e('premium_yearly_first_order/customer.created'))
        StripeWebhookService.process_event(e('premium_yearly_first_order/customer.updated'))
        StripeWebhookService.process_event(e('premium_yearly_first_order/invoice.created'))
        StripeWebhookService.process_event(e('premium_yearly_first_order/customer.subscription.created'))
        StripeWebhookService.process_event(e('premium_yearly_first_order/invoice.finalized'))
        StripeWebhookService.process_event(e('premium_yearly_first_order/invoice.updated'))
        StripeWebhookService.process_event(e('premium_yearly_first_order/invoice.paid'))
        StripeWebhookService.process_event(e('premium_yearly_first_order/invoice.payment_succeeded'))
        StripeWebhookService.process_event(e('premium_yearly_first_order/customer.subscription.updated'))
        StripeWebhookService.process_event(e('premium_yearly_first_order/payment_intent.succeeded'))
        StripeWebhookService.process_event(e('premium_yearly_first_order/payment_intent.created'))
        StripeWebhookService.process_event(e('premium_yearly_first_order/checkout.session.completed'))

        user.userprofile.refresh_from_db()

        valid_subscription = PremiumService(user).get_valid_usersubscription()
        self.assertTrue(PremiumService.is_premium_2020(valid_subscription))
        self.assertEqual(valid_subscription.expires, date(2024, 5, 26))
        self.assertFalse(valid_subscription.cancelled)
        self.assertEqual(valid_subscription.subscription, self.subscription)
        self.assertIsNotNone(user.userprofile.stripe_customer_id)
        self.assertIsNotNone(user.userprofile.stripe_subscription_id)
        self.assertEqual(
            1,
            Transaction.objects.filter(
                user=user,
                subscription=self.subscription,
                event='subscription payment',
                amount=45,
            ).count()
        )

    def test_cancellation(self):
        user = Generators.user(email="astrobin@astrobin.com")
        user.userprofile.stripe_customer_id = 'STRIPE_CUSTOMER_ID'
        user.userprofile.save()

        e = StripeGenerators.event

        user_subscription = Generators.premium_subscription(user, SubscriptionName.PREMIUM_2020_AUTORENEW_YEARLY)

        valid_subscription = PremiumService(user).get_valid_usersubscription()
        self.assertTrue(PremiumService.is_premium_2020(valid_subscription))
        self.assertEqual(valid_subscription.subscription, self.subscription)
        self.assertFalse(valid_subscription.cancelled)

        StripeWebhookService.process_event(e('premium_yearly_cancellation/billing_portal.session.created'))
        StripeWebhookService.process_event(e('premium_yearly_cancellation/customer.subscription.updated'))

        valid_subscription = PremiumService(user).get_valid_usersubscription()
        self.assertTrue(PremiumService.is_premium_2020(valid_subscription))

        user_subscription.refresh_from_db()
        self.assertTrue(user_subscription.cancelled)

    def test_upgrade(self):
        self.test_first_order()

        ultimate = Subscription.objects.create(
            name=SubscriptionName.ULTIMATE_2020_AUTORENEW_YEARLY.value,
            currency="CHF",
            price=60,
            trial_period=0,
            trial_unit=None,
            recurrence_period=1,
            recurrence_unit='Y',
            group=Group.objects.get_or_create(name='astrobin_ultimate_2020')[0],
            category='premium_autorenew'
        )

        user = User.objects.first()
        e = StripeGenerators.event

        self.assertEqual(
            1,
            Transaction.objects.filter(
                user=user,
                subscription=self.subscription,
                event='subscription payment',
                amount=45,
            ).count()
        )

        StripeWebhookService.process_event(e('premium_yearly_upgrade_to_ultimate_yearly/customer.subscription.updated'))

        user.userprofile.refresh_from_db()

        valid_subscription = PremiumService(user).get_valid_usersubscription()
        self.assertTrue(PremiumService.is_ultimate_2020(valid_subscription))
        self.assertEqual(valid_subscription.expires, date(2024, 5, 26))
        self.assertFalse(valid_subscription.cancelled)
        self.assertEqual(valid_subscription.subscription, ultimate)
        self.assertIsNotNone(user.userprofile.stripe_customer_id)
        self.assertIsNotNone(user.userprofile.stripe_subscription_id)
        self.assertEqual(
            1,
            Transaction.objects.filter(
                user=user,
                subscription=self.subscription,
                event='subscription payment',
                amount=45,
            ).count()
        )
