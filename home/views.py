from django.shortcuts import render
import os


def home(request):
	a = 5 / 0
	member1 = os.getenv("MEMBER_1")
	member2 = os.getenv("MEMBER_2")
	member3 = os.getenv("MEMBER_3")
	team = os.getenv("TEAM")

	return render(request, "home.html", locals())
