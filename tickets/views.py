# tickets/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .models import Ticket
from .forms import TicketForm


# 机票列表 - 需要登录和查看权限
@login_required
@permission_required('tickets.can_view_ticket', raise_exception=True)
def ticket_list(request):
    tickets = Ticket.objects.all().select_related('flight', 'passenger')

    # 搜索功能
    search_query = request.GET.get('search', '')
    if search_query:
        tickets = tickets.filter(
            Q(booking_reference__icontains=search_query) |
            Q(seat_number__icontains=search_query) |
            Q(passenger__first_name__icontains=search_query) |
            Q(passenger__last_name__icontains=search_query) |
            Q(flight__flight_number__icontains=search_query)
        )

    return render(request, 'ticket_list.html', {
        'tickets': tickets,
        'search_query': search_query
    })


# 机票详情 - 需要登录和查看权限
@login_required
@permission_required('tickets.can_view_ticket', raise_exception=True)
def ticket_detail(request, id):
    ticket = get_object_or_404(Ticket.objects.select_related('flight', 'passenger'), id=id)
    return render(request, 'ticket_detail.html', {'ticket': ticket})


# 创建机票 - 需要登录和添加权限
@login_required
@permission_required('tickets.can_add_ticket', raise_exception=True)
def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            messages.success(request, f'Ticket {ticket.booking_reference} created successfully!')
            return redirect('ticket_detail', id=ticket.id)
    else:
        form = TicketForm()

    return render(request, 'ticket_form.html', {
        'form': form,
        'title': 'Create Ticket'
    })


# 编辑机票 - 需要登录和修改权限
@login_required
@permission_required('tickets.can_change_ticket', raise_exception=True)
def ticket_update(request, id):
    ticket = get_object_or_404(Ticket, id=id)

    if request.method == 'POST':
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            form.save()
            messages.success(request, f'Ticket {ticket.booking_reference} updated successfully!')
            return redirect('ticket_detail', id=ticket.id)
    else:
        form = TicketForm(instance=ticket)

    return render(request, 'ticket_form.html', {
        'form': form,
        'title': 'Edit Ticket',
        'ticket': ticket
    })


# 删除机票 - 需要登录和删除权限
@login_required
@permission_required('tickets.can_delete_ticket', raise_exception=True)
def ticket_delete(request, id):
    ticket = get_object_or_404(Ticket, id=id)

    if request.method == 'POST':
        booking_ref = ticket.booking_reference
        ticket.delete()
        messages.success(request, f'Ticket {booking_ref} deleted successfully!')
        return redirect('ticket_list')

    # 如果是GET请求，直接重定向到列表页
    return redirect('ticket_list')