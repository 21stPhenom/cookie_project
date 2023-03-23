import datetime as dt

class PrintMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response
        print("Middleware Activated")
    
    def __call__(self, request):

        start = dt.datetime.now()

        with open("ip_addr.txt", "a+t", encoding="utf-8") as ip_file:
            formatted_ip = f"{request.META.get('REMOTE_ADDR')}\n"
            ip_file.write(formatted_ip)
        
        with open("cookie_file.txt", "a+t", encoding="utf-8") as cookie_file:
            for key, value in request.session.items():
                formatted_cookie = f"{key} ---> {value}\n"

                cookie_file.write(formatted_cookie)
            cookie_file.write("\n")
        response = self.get_response(request)
        end = dt.datetime.now()

        difference = (start - end).microseconds / 1000
        print(f"The {self.__class__.__name__} took {difference}ms")

        return response