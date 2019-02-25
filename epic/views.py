from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def welcome(request):
    return HttpResponse('Welcome to the Moringa Tribune')

def convert_dates(dates):
    '''
    Function that gets the weekely number for the date.
    '''
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]
    '''

    Returning the actual day of the week
    '''
    day = days[day_number]
    return day
