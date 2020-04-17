from django.shortcuts import redirect, render
from django.core.exceptions import ValidationError
from django.core.urlresolvers import reverse
from lists.forms import ExistingListItemForm, ItemForm
from lists.models import Item, List
from django.views.generic import FormView, CreateView, DetailView
from django.contrib.auth import get_user_model
User=get_user_model()
class HomePageView(FormView):
    template_name = 'home.html'
    form_class = ItemForm


class NewListView(CreateView):
    template_name = 'home.html'
    form_class = ItemForm

    def form_valid(self, form):
        list_ = List.objects.create()
        form.save(for_list=list_)
        return redirect(list_)


class ViewAndAddToList(DetailView):
    model = List
    template_name = 'list.html'
    form_class = ExistingListItemForm

    def get_form(self):
        self.object = self.get_object()
        return self.form_class(for_list=self.object, data=self.request.POST)


def view_list(request, list_id):

    list_ = List.objects.get(id=list_id)
    form = ExistingListItemForm(for_list=list_)
    if request.method == "POST":
        form = ExistingListItemForm(for_list=list_, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(list_)
    return render(request, 'list.html', {'list': list_, 'form': form})


def new_list(request):

    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List()
        list_.owner=request.user
        list_.save()
        form.save(for_list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})


def my_lists(request, email):
    owner=User.objects.get(email=email)

    return render(request, 'my_lists.html',{'owner':owner})
