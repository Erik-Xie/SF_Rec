from flask import Blueprint, render_template, request

recommendation_bp = Blueprint("recommendation", __name__)

raw_data = [
    {
        "ZIP_CODE": "94118",
        "AVG_HOUSE_PRICE": 1379905,
        "total_AGI": 101965914908,
        "total_tax_liability": 8173725490,
        "num_businesses": 1044,
        "Population": 39275,
        "lat": 37.7749,
        "lng": -122.4194
    },
    {
        "ZIP_CODE": "94115",
        "AVG_HOUSE_PRICE": 1007448,
        "total_AGI": 90890031581,
        "total_tax_liability": 7409902951,
        "num_businesses": 882,
        "Population": 32715,
        "lat": 37.7917,
        "lng": -122.4376
    },
    {
        "ZIP_CODE": "94109",
        "AVG_HOUSE_PRICE": 849865,
        "total_AGI": 94855956339,
        "total_tax_liability": 6649443893,
        "num_businesses": 1529,
        "Population": 54397,
        "lat": 37.7989,
        "lng": -122.4210
    },
    {
        "ZIP_CODE": "94103",
        "AVG_HOUSE_PRICE": 775230,
        "total_AGI": 87022334455,
        "total_tax_liability": 5993450020,
        "num_businesses": 1675,
        "Population": 41308,
        "lat": 37.7726,
        "lng": -122.4099
    }
]


@recommendation_bp.route("/recommendation", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        for item in raw_data:
            item["formatted_price"] = "${:,.0f}".format(item["AVG_HOUSE_PRICE"])
        return render_template("recommendation.html", data=raw_data, submitted=True)

    return render_template("recommendation.html", data=[], submitted=False)
