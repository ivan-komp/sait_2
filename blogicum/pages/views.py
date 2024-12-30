from django.views.generic import TemplateView


class AboutView(TemplateView):
    """
    Отображает страницу "О роекте".
    """
    template_name = "pages/about.html"

class RulesView(TemplateView):
    """
    Отображает страницу с правилами.
    """
    template_name = "pages/rules.html"