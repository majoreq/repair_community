"""repair_community URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from repair.views import Index, Register, Login, logoff, NewTicket, FreeTickets, MakeOffer, TicketStatus, AssignCase, MyMessages, SendMessage, ReadMessage, SendDM, MyTickets, MyRepairs


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Index.as_view(), name='index'),
    path('register', Register.as_view(), name='register'),
    path('login', Login.as_view(), name='login'),
    path('logout', logoff, name='logout'),
    path('new_ticket', NewTicket.as_view(), name='new-ticket'),
    path('free_tickets', FreeTickets.as_view(), name='free-tickets'),
    path('free_tickets/<ticket_id>', MakeOffer.as_view(), name='make-offer'),
    path('ticket/<ticket_id>', TicketStatus.as_view(), name='ticket-status'),
    path('ticket/<ticket_id>/<offer_id>', AssignCase.as_view(), name='assign'),
    path('messages', MyMessages.as_view(), name='messages'),
    path('send_message', SendMessage.as_view(), name='send-message'),
    path('message/<message_id>', ReadMessage.as_view(), name='read-message'),
    path('message/dm/<user_id>', SendDM.as_view(), name='send-dm'),
    path('my_tickets', MyTickets.as_view(), name='my-tickets'),
    path('my_repairs', MyRepairs.as_view(), name='my-repairs')
]
