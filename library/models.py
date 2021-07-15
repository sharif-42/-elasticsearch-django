from django.db import models
from django.utils.translation import ugettext_lazy as _


class Author(models.Model):
    first_name = models.CharField(_("First name"), max_length=200)
    last_name = models.CharField(_("Last name"), max_length=200)
    author_name = models.CharField(_("Author name"), max_length=200)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        null=True,
        blank=True,
        unique=True,
        help_text='unique email address'
    )

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")
        ordering = ("author_name",)

    def __str__(self):
        return self.author_name


class Book(models.Model):
    title = models.CharField(_("Title"), max_length=200)
    authors = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    publishing_date = models.DateField(_("Publishing date"), blank=True, null=True)
    isbn = models.CharField(_("ISBN"), blank=True, max_length=20)

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")
        ordering = ("title",)

    def __str__(self):
        return self.title
