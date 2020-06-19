import requests
import random as rd
from django.core.management.base import BaseCommand
from filtersApis.models import *


class Command(BaseCommand):
    """
    Command to fill the database
    """

    def __init__(self):
        """
        Instance creation, we take nike exemple with 2 managers
        """
        self.manageOne = User.objects.get(username="Koyati")
        self.manageTwo = User.objects.get(username="sakanti")
        self.page = Pages.objects.get(name="Nike")

    def insert_posts(self):
        """
        Method to insert dump data in the posts model
        """
        comment = "Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique, sans que son contenu n'en soit modifié. Il a été popularisé dans les années 1960 "
        days = ["02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14",
                "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]
        hours = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11",
                 "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
        minuts = [
            "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"
        ]
        secs = [
            "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"
        ]
        poster = [self.manageOne, self.manageTwo]
        for i in days:
            # print(i)
            for x in range(6):
                p = Posts(content=comment, posted_by=rd.choice(poster), created='2020-06-{} {}:{}:{}'.format(i, rd.choice(hours), rd.choice(minuts), rd.choice(secs)), page=self.page
                          )
                p.save()

    def insert_comments(self):
        """
        Method to insert dump data in the posts model
        """
        com = "Le Lorem Ipsum est simplement du faux texte employé dans la composition et la mise en page avant impression. Le Lorem Ipsum est le faux texte standard de l'imprimerie depuis les années 1500, quand un imprimeur anonyme assembla ensemble des morceaux de texte pour réaliser un livre spécimen de polices de texte. Il n'a pas fait que survivre cinq siècles, mais s'est aussi adapté à la bureautique informatique, sans que son contenu n'en soit modifié. Il a été popularisé dans les années 1960 "
        days = ["02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14",
                "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "30"]
        hours = ["00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11",
                 "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"]
        minuts = [
            "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"
        ]
        secs = [
            "01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24"
        ]
        posts = Posts.objects.all()

        counter = 1
        for i in posts:
            for x in days:
                for j in range(35):
                    c = Comments(comment=com, post=Posts.objects.get(id=i.id), created='2020-06-{} {}:{}:{}'.format(x, rd.choice(hours), rd.choice(minuts), rd.choice(secs))
                                 )
                    c.save()

    def handle(self, *args, **options):
        """
        Method to insert categories's data in 
        categories tables in database
        """
        # Posts.objects.all().delete()
        # Comments.objects.all().delete()

        # self.insert_posts()
        # self.insert_comments()
        p = Comments.objects.filter(post=357)
        print(len(p))
