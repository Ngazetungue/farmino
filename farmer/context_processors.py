from .models import Billing, Client


def billing_overdue_status(request):
    count_overdue = Billing.objects.filter(invoice_status ="Overdue").count()
    total_overdue = {"count_overdue": count_overdue}
    return total_overdue

def number_of_farmer(request):
    count_farmer = Client.objects.all().count()
    total_farmer = {"count_farmer": count_farmer}
    return total_farmer

def number_of_billing(request):
    count_billings = Billing.objects.all().count()
    total_billings = {"count_billings": count_billings}
    return total_billings

