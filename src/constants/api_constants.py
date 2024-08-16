# API Constants - Class which contains all the endpoints
# Keep the URLS


class APIconstants(object):

    def base_url(self):
        return "https://restful-booker.herokuapp.com"

    def url_createbooking(self):
        return "https://restful-booker.herokuapp.com/booking"

    def auth_createtoken(self):
        return "https://restful-booker.herokuapp.com/auth"

    # update,put,patch,delete-bookingid

    def url_patch_put_delete(booking_id):
        return "https://restful-booker.herokuapp.com/booking" + str(booking_id)

    

