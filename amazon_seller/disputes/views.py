from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Dispute
from returns.models import Return

def dispute_list(request):
    disputes = Dispute.objects.all()
    return render(request, 'dispute_list.html', {'disputes': disputes})

def create_dispute(request):
    if request.method == 'POST':
        return_order_id = request.POST.get('return_order_id')
        dispute_reason = request.POST.get('dispute_reason')
        return_order = get_object_or_404(Return, id=return_order_id)
        dispute = Dispute.objects.create(
            return_order=return_order,
            dispute_reason=dispute_reason,
            status='open'
        )
        return render(request, 'partials/dispute_row.html', {'dispute': dispute})
    else:
        returns = Return.objects.all()
        return render(request, 'create_dispute.html', {'returns': returns})
