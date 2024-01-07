from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "blog/index.html")


def article(request, numero_article):
    if numero_article in ["01", "02", "03"]:
        # f = f-string. Va permettre d'insérer des variables à l'intérieur de la chaîne de caractères
        return render(request, f"blog/article_{numero_article}.html")
    return render(request, "blog/article_not_found.html")
