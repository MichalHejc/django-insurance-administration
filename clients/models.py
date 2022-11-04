from datetime import date

from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=200, verbose_name="Jméno")
    surname = models.CharField(max_length=200, verbose_name="Příjmení")
    street_address = models.CharField(max_length=200, verbose_name="Ulice a číslo popisné")
    city = models.CharField(max_length=100, verbose_name="Město")
    postal_code = models.CharField(max_length=6, verbose_name="Poštovní směrovací číslo")
    email = models.EmailField(max_length=200, verbose_name="Email")
    phone_number = models.CharField(max_length=16, verbose_name="Telefon")

    def __str__(self):
        return f"{self.name} {self.surname}"


class Insurance(models.Model):
    TYPES_OF_INSURANCE = [
        ("MAJETEK", "Pojištění majetku"),
        ("HAVARIJNI", "Havarijní pojištění"),
        ("ZIVOTNI", "Životní pojištění"),
        ("URAZOVE", "Úrazové pojištění"),
        ("ODPOVEDNOSTI", "Pojištění odpovědnosti")
    ]

    insurance_type = models.CharField(max_length=30, choices=TYPES_OF_INSURANCE, verbose_name="Typ pojištění")
    subject = models.CharField(max_length=100, verbose_name="Předmět pojištění")
    amount = models.PositiveIntegerField(verbose_name="Pojistná částka")
    date_from = models.DateField(default=date.today, verbose_name="Pojištění od")
    date_to = models.DateField(default=date.today, verbose_name="Pojištění do")
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.insurance_type}: {self.subject}, {self.amount}"