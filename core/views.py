from django.shortcuts import render, redirect
from django.http import HttpResponse

from openpyxl import Workbook

from .forms import TourFormForm
from .models import TourForm


def tour_form(request):

    if request.method == "POST":
        form = TourFormForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("tour_form")

    else:
        form = TourFormForm()

    return render(request, "index.html", {
        "form": form
    })


def export_tours(request):

    workbook = Workbook()
    worksheet = workbook.active
    worksheet.title = "Tour Forms"

    # Headers
    worksheet.append([
        "ID",
        "Name",
        "Branch",
        "Contact Number",
        "Email",
    ])

    # Database → Excel
    tours = TourForm.objects.select_related("branch").all()

    for tour in tours:
        worksheet.append([
            tour.id,
            tour.name,
            tour.branch.branch,
            tour.contact_no,
            tour.email,
        ])

    # Download response
    response = HttpResponse(
        content_type=(
            "application/vnd.openxmlformats-officedocument."
            "spreadsheetml.sheet"
        )
    )

    response["Content-Disposition"] = (
        'attachment; filename="tour_forms.xlsx"'
    )

    workbook.save(response)

    return response