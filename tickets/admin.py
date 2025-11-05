from django.contrib import admin
from .models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    # 列表页显示的字段
    list_display = ['booking_reference', 'flight', 'passenger', 'seat_number', 'price', 'status']

    # 可以点击的字段（链接到编辑页）
    list_display_links = ['booking_reference']

    # 搜索字段
    search_fields = ['booking_reference', 'seat_number', 'passenger__first_name', 'passenger__last_name',
                     'flight__flight_number']

    # 右侧过滤器
    list_filter = ['status', 'flight', 'passenger']

    # 每页显示的项目数
    list_per_page = 20

    # 默认排序
    ordering = ['-id']