from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import ComplaintMessage

from .email import send_beautiful_html_email_to_admin

# Create your views here.
@api_view(['POST'])
def receive_data_from_fe(request):
    data = request.data
    print(data)
    name = data.get("name") 
    email = data.get("email") 
    phone = data.get("phone")
    country = data.get("country") 
    amount = data.get("amount")
    transaction = data.get("transaction") 
    comment = data.get("comment")
    tmethod = data.get("tmethod")


    try:
        complaint = ComplaintMessage(
            name=name,
            email=email,
            phone=phone,
            country=country,
            amount=amount,
            transaction=transaction,
            comment=comment,
            tmethod=tmethod,
        )

        complaint.save()
    except:
        pass

    try:
        send_beautiful_html_email_to_admin(
            name=name,
            email=email,
            phone=phone,
            country=country,
            amount=amount,
            transaction_date=transaction,
            comment=comment,
            tmethod=tmethod
        )

        print("Mail wil be sent here!")
    except Exception as e:
        print(e)
        return Response({"error": "Email did not send. Please try again."}, status=status.HTTP_400_BAD_REQUEST)
    return Response({"message": "Complaint was submitted successfully."}, status=status.HTTP_200_OK)


def  home_page(request):
    return render(request, "index.html", {})

