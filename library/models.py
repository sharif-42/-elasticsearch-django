from django.db import models
from django.utils.translation import ugettext_lazy as _


class Author(models.Model):
    first_name = models.CharField(
        verbose_name=_("First name"),
        max_length=200,
        help_text=_("Author First Name")
    )
    last_name = models.CharField(
        verbose_name=_("Last name"),
        max_length=200,
        help_text=_("Author Last Name")
    )
    author_name = models.CharField(
        verbose_name=_("Author name"),
        max_length=200,
        help_text=_("Author Name"),
        unique=True,
    )
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
        ordering = ("-id",)

    def __str__(self):
        return self.author_name


class Book(models.Model):
    title = models.CharField(
        verbose_name=_("Title"),
        help_text=_("Title of the Book"),
        max_length=200
    )
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books',
        help_text=_("related author")
    )
    publishing_date = models.DateTimeField(
        verbose_name=_("Publishing datetime"),
        help_text=_("Publishing datetime"),
        blank=True,
        null=True
    )
    isbn = models.CharField(
        verbose_name=_("ISBN"),
        blank=True,
        max_length=20
    )

    class Meta:
        verbose_name = _("Book")
        verbose_name_plural = _("Books")
        ordering = ("-id",)

    def __str__(self):
        return self.title
