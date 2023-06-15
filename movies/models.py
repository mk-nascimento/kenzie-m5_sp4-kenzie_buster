from django.db import models


class Rated(models.TextChoices):
    G = "G"
    PG = "PG"
    PG_13 = "PG-13"
    R = "R"
    NC_17 = "NC-17"


class Movie(models.Model):
    title = models.CharField(max_length=127)
    duration = models.CharField(max_length=10, blank=True, null=True, default=None)
    rating = models.CharField(
        max_length=20, choices=Rated.choices, blank=True, null=True, default=Rated.G
    )
    synopsis = models.TextField(blank=True, null=True, default=None)

    user = models.ForeignKey(
        "users.User", on_delete=models.PROTECT, related_name="movies"
    )
