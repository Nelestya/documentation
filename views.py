from django.shortcuts import get_object_or_404, render
from .models import *
# Create your views here.
from baseapp.views import FieldsView


class HomeDoc(FieldsView):
    template_name = 'documentation/docs/home.html'
    def get(self, request):
        self.fields['title'] = 'Documentation'
        self.fields['description'] = 'Documentation'
        self.fields['category'] = Category.objects.order_by('name')
        self.fields['docs'] = Documentation.objects.all()
        context = {
                    'fields': self.fields,
                   }

        return render(request, self.template_name , context)

    def post(self, request):
        pass

class CategoryPage(FieldsView):
    template_name = 'documentation/docs/category.html'
    def get(self, request, category):

        self.fields['category'] = Category.objects.order_by('name')
        self.fields['docs'] = Documentation.objects.all()
        self.fields['categorybody'] = get_object_or_404(Category, slug=category)
        self.fields['docsbody'] = Documentation.objects.filter(category=category)
        context = {
                    'fields': self.fields,
                   }
        return render(request, self.template_name , context)

    def post(self, request):
        pass

class DocumentationPage(FieldsView):
    def get(self, request, category, documentation):
        self.fields['title'] = 'Documentation'
        self.fields['category'] = Category.objects.order_by('name')
        self.fields['docs'] = Documentation.objects.all()
        self.fields['documentation'] = get_object_or_404(Documentation, pk=documentation)
        paragraphes = Paragraphe.objects.filter(documentation=doc_name)
        category = Category.objects.order_by('name')
        docs = Documentation.objects.all()


        context = {
                'category': category,
                'docs': docs,
                'doc': documentation,
                'paragraphes': paragraphes,
              }

        return render(request, 'doc/documentation.html', context)

    def post(self, request):
        pass
