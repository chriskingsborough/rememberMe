from django.shortcuts import render, redirect
from person.forms import PersonForm
from person.models import Person
from index.models import User
from django.views.generic.edit import CreateView, UpdateView, DeleteView

import datetime
from dateutil.relativedelta import relativedelta

def create_person(request):

    # redirect to sign in not logged in
    if 'id' not in request.session.keys():
        return redirect('/sign_in/')

    # if this is a POST request we need to process the form dat
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:

        form = PersonForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form_data = form.cleaned_data
            current_user = User.objects.get(pk=request.user.id)

            new_row = Person(
                user=current_user,
                name=form_data['name'],
                message=form_data['message'],
                created=datetime.datetime.now(),
                start_date=form_data['start_date'],
                last_send=None,
                next_send=form_data['start_date'],
                interval=form_data['interval'],
                interval_type=form_data['interval_type'],
                snooze=0,
                snooze_interval=None,
                snooze_interval_type=None,
                snooze_last_send=None,
                snooze_next_send=None,
                in_deleted=0
            )
            new_row.save()
            return redirect('/view_person_list/')
    else:
        form = PersonForm()

    return render(request, 'person/create_person.html', {'form': form})


def view_person_list(request):

    if 'id' not in request.session.keys():
        return redirect('/sign_in/')

    people = Person.objects.filter(user_id=request.user.id).reverse()

    context = {'people': people}

    return render(request, 'person/view_person_list.html', context)

def edit_person(request):

    if 'id' not in request.session.keys():
        return redirect('/sign_in/')
    #TODO: check to make sure user logged in is associated with person - person ID may be public in the URL

    # get person ID from querystring
    person_id = request.GET['id']
    # pass person ID to Person model to pull current person
    current_person = Person.objects.get(pk=person_id)

    form = PersonForm(request.POST or None, instance=current_person)
    if request.POST and form.is_valid():
        form.save()

        # Save was successful
        redirect_url = '/view_person_list/'
        return redirect(redirect_url)

    context = {'form': form}

    return render(request, 'person/update_person.html', context=context)

def view_person(request):
    if 'id' not in request.session.keys():
        return redirect('/sign_in/')

    person_id = request.GET['id']
    current_person = Person.objects.get(pk=person_id)
    context = {'person': current_person}

    return render(request, 'person/view_person.html', context=context)

def delete_person(request):
    if 'id' not in request.session.keys():
        return redirect('/sign_in/')

    person_id = request.GET['id']
    current_person = Person.objects.get(pk=person_id)
    current_person.delete()

    return redirect('/view_person_list/')
