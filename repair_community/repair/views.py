from django.shortcuts import render, redirect
from django.views import View
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm, TicketForm, OfferForm
from django.contrib.auth.models import User, Group
from django.contrib.auth import authenticate, login, logout
from .models import Ticket, Offer

class Index(View):
    def get(self, request):
        return render(request, 'base.html')


class Register(View):
    def get(self, request):
        form = RegisterForm()
        return render(request, 'register.html', {
            'form':form
        })

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['password'] == form.cleaned_data['password2']:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password'],
                    first_name=form.cleaned_data['first_name'],
                    last_name=form.cleaned_data['last_name'])
                group = Group.objects.get(name=form.cleaned_data['group'])
                # print(form.cleaned_data['group'])
                # print("*")
                # print(group)
                user.save()
                user.groups.add(group)
                return HttpResponse("WORK")


class Login(View):
    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {
            'form':form
        })

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['login'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('index')
            else:
                error = "Wrong username or password"
                return render(request, 'login.html', {
                    'form': form, 'error':error
                })
        return HttpResponse("Not working")



def logoff(request):
    logout(request)
    return redirect('index')


class NewTicket(View):
    def get(self, request):
        form = TicketForm()
        return render(request, 'new_ticket.html',{
            'form':form
        })

    def post(self, request):
        form = TicketForm(request.POST)
        user = User.objects.get(id = request.user.id)
        if form.is_valid():
            Ticket.objects.create(
            device = form.cleaned_data['device'],
            description = form.cleaned_data['description'],
            author = user
            )
            return HttpResponse("ticket created")
        return HttpResponse("form is not valid")


class FreeTickets(View):
    def get(self, request):
        tickets = Ticket.objects.filter(assigned_to=None)
        return render(request, 'free_tickets.html', {
            'tickets':tickets
        })


class MakeOffer(View):
    def get(self, request, ticket_id):
        ticket = Ticket.objects.get(id = ticket_id)
        form = OfferForm()
        return render(request, 'new_offer.html', {
            'form':form,
            'ticket':ticket
        })

    def post(self, request, ticket_id):
        ticket = Ticket.objects.get(id=ticket_id)
        form = OfferForm(request.POST)
        user = User.objects.get(id = request.user.id)
        if form.is_valid():
            Offer.objects.create(
                author = user,
                price = form.cleaned_data['price'],
                ticket = ticket,
                message = form.cleaned_data['message']
            )
            return HttpResponse("wysłano ofertę")
        return HttpResponse("coś nie śmiga")


class TicketStatus(View):
    def get(self, request, ticket_id):
        ticket = Ticket.objects.get(id=ticket_id)
        offers = Offer.objects.filter(ticket=ticket)
        print(ticket.assigned_to)
        return render(request, 'ticket_status.html', {
            'ticket':ticket,
            'offers':offers,
        })

class AssignCase(View):
    def get(self, request, ticket_id, offer_id):
        ticket = Ticket.objects.get(id=ticket_id)
        offer = Offer.objects.get(id=offer_id)
        ticket.assigned_to = offer.author
        ticket.status = '01'
        offer.ticket = ticket
        offer.save()
        ticket.save()

        return render(request, 'ticket_in_progres.html', {
            'ticket': ticket,
            'offers': offer,
        })
